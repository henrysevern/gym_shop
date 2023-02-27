from datetime import datetime
from django.conf import settings
from django.http import Http404, JsonResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
import stripe

from payments.models import Currency, Payment
from store.models import Order


stripe.api_key = settings.STRIPE_API_KEY_HIDDEN


@require_http_methods(["GET"])
def payment_view(request):

    localhost = 'http://localhost:8000'
    heroku = 'gym-shop.herokuapp.com'

    redirect_hostname = localhost if settings.DEBUG else heroku

    context = {
        "stripe_public_key": settings.STRIPE_API_KEY_PUBLISHABLE,
        # the url stripe sends the user to when the payment is completed
        "stripe_redirect_url": redirect_hostname + reverse('payment_complete')
    }

    return render(request, "payments/payment.html", context=context)


@require_http_methods(["POST"])
def payment_start(request):
    """ called by stripe from payment.js when the payment starts """
    customer = request.user.customer

    order = get_object_or_404(
        Order,
        customer=customer,
        complete=False
    )

    try:
        currency = Currency.GBP
        intent = stripe.PaymentIntent.create(
            amount=order.cart_total_integer,
            currency=currency,

            # this allows you to control what payment
            # methods are available to the customer
            # from your stripe dashboard
            automatic_payment_methods={
                'enabled': True,
            },

            # not required, just saves our local order_id in stripe's database
            metadata={
                "order_id": order.id
            },

        )

        Payment.objects.update_or_create(
            complete=False,
            customer=customer,
            amount=order.cart_total_integer,
            currency=currency,
            order=order,
            defaults={
                "payment_intent_id": intent['id']
            }
        )

        return JsonResponse(data={'clientSecret': intent['client_secret']})

    except Exception as error:
        # something went wrong
        print("Error during payment creation", error)

        return JsonResponse(status=500, data={"error": "Server Error"})


def get_payment_status_message(payment_intent):
    status = payment_intent['status']
    if status == 'succeeded':
        return "Payment succeeded"
    if status == "processing":
        return "Payment is being processed"
    if status == "requires_payment_method":
        return "Payment failed, please try again"
    
    return "Something went wrong with your payment."

@require_http_methods(["GET"])
def payment_complete(request):
    """Redirected here if stripe payment is successful"""

    payment_intent_id = request.GET.get('payment_intent')

    if payment_intent_id:
        
        payment = get_object_or_404(
            Payment,
            customer=request.user.customer,
            payment_intent_id=payment_intent_id
        )

        # get the payment object from stripe
        payment_intent = stripe.PaymentIntent.retrieve(
                payment_intent_id)
        
        payment_status_message = get_payment_status_message(payment_intent)

        if not payment.complete:
            
            customer = request.user.customer

            if not customer.stripe_customer_id:
                #  customer has not been created in stripe so create one
                stripe_customer = stripe.Customer.create(
                    email=request.user.email,
                    metadata={
                        'id': request.user.id
                    }
                )
                customer.stripe_customer_id = stripe_customer['id']
                customer.save()
            else:
                stripe_customer = stripe.Customer.retrieve(
                    customer.stripe_customer_id)

            # attach the payment to the customer in stripe
            stripe.PaymentIntent.modify(
                payment_intent['id'],
                customer=stripe_customer
            )

            payment.complete = True
            payment.order.complete = True

            payment.save()

            payment.order.date_ordered = timezone.now()
            payment.order.save()

        context = {
            "payment": payment,
            "order": payment.order,
            "payment_status_message": payment_status_message
        }

        return render(request, 'payments/payment_complete.html', context=context)

    # if no payment_intent parameter in the url, return them to the main page
    return redirect(reverse('item_list'))