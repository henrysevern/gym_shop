
// modified code from https://stripe.com/docs/payments/quickstart

const stripe = Stripe(stripe_public_key)

let elements;

initialize();

document
    .querySelector("#payment-form")
    .addEventListener("submit", handleSubmit);

async function initialize() {
    const response = await fetch("/payments/payment_start", {
        method: "POST",
        headers: { "Content-Type": "application/json", "X-CSRFToken": csrftoken },
    });
    const { clientSecret } = await response.json();

    const appearance = {
        theme: 'stripe',
    };
    elements = stripe.elements({ appearance, clientSecret });

    const paymentElementOptions = {
        layout: "tabs",

    };

    // email from global userEmail variable declared in store/templates/store/base.html
    if (userEmail !== "") {
        paymentElementOptions.defaultValues = {
            billingDetails: {
                email: userEmail,
            }
        }
    }

    const paymentElement = elements.create("payment", paymentElementOptions);
    paymentElement.mount("#payment-element");
    paymentElement.on("ready", function () {
        // fade in the submit button once the form has loaded
        document.getElementById("payment-submit").classList.remove("hidden")
    })
}

async function handleSubmit(e) {

    e.preventDefault();

    setLoading(true);

    const confirmParams = {
        return_url: stripe_redirect_url,
    }

    const { error } = await stripe.confirmPayment({
        elements,
        confirmParams: confirmParams
    });

    // This point will only be reached if there is an immediate error when
    // confirming the payment. Otherwise, your customer will be redirected to
    // your `return_url`. 

    if (error.type === "card_error" || error.type === "validation_error") {
        showMessage(error.message);
    } else {
        showMessage("An unexpected error occurred.");
    }

    setLoading(false);
}

function showMessage(messageText) {
    const messageContainer = document.querySelector("#payment-message");

    messageContainer.classList.remove("hidden");
    messageContainer.textContent = messageText;

    setTimeout(function () {
        messageContainer.classList.add("hidden");
        messageText.textContent = "";
    }, 4000);
}

// Show a spinner on payment submission
function setLoading(isLoading) {
    if (isLoading) {
        // Disable the button and show a spinner
        document.querySelector("#payment-submit").disabled = true;
        document.querySelector("#spinner").classList.remove("hidden");
        document.querySelector("#button-text").classList.add("hidden");
    } else {
        document.querySelector("#payment-submit").disabled = false;
        document.querySelector("#spinner").classList.add("hidden");
        document.querySelector("#button-text").classList.remove("hidden");
    }
}