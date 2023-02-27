// moved these to checkout.html
// var shipping = '{{order.shipping}}'
// var total = '{{order.get_cart_total}}'

if (shipping == 'False') {
    document.getElementById('shipping-info').innerHTML = ''
}

if (user != 'AnonymousUser') {
    document.getElementById('user-info').innerHTML = ''
}

// Hides entire form if user is logged in and shipping is false.
if (shipping == 'False' && user != 'AnonymousUser') {
    document.getElementById('form-wrapper').classList.add("hidden")
    document.getElementById('payment-info').classList.remove("hidden")
}
// Gets the payment button displayed once the form has been filled, removes submit form button 
var form = document.getElementById('form')

// var csrftoken = form.getElementsByTagName("input")[0].value

form.addEventListener('submit', function (e) {
    e.preventDefault()
    console.log('Form submitted...')
    submitFormData()
})

function submitFormData() {
    console.log('Payment button clicked')

    var userFormData = {
        'name': null,
        'email': null,
        'total': total,
    }

    var shippingInfo = {
        'address': null,
        'city': null,
        'country': null,
        'postcode': null,

    }

    if (shipping != 'False') {
        shippingInfo.address = form.address.value
        shippingInfo.city = form.city.value
        shippingInfo.country = form.country.value
        shippingInfo.postcode = form.postcode.value
    }

    if (user == 'AnonymousUser') {
        userFormData.name = form.name.value
        userFormData.email = form.email.value
    }

    var url = '/process_order/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'form': userFormData,
            'shipping': shippingInfo
        })
    })

        .then((response) => response.json())
        .then((data) => {
            console.log('Success', data);
            alert('Shipping adress added!');
            window.location.href = "/payments"
        })
}