# Testing 

## Validator Testing 

### HTML

- Some errors where found in `store app` when passed through the official [W3C's HTML Validator](https://validator.w3.org/nu/?doc=https://gym-shop.herokuapp.com/) and have now been amended.

>![store.html validation](documentation/testing/validation/store.html.png)

- No errors where found in `contact app` when passed through the official [W3C's HTML Validator](https://validator.w3.org/nu/?doc=https://gym-shop.herokuapp.com/contact).

>![contact.html validation](documentation/testing/validation/contact.html.png)

- No errors where found in `profile app` when passed through the official [W3C's HTML Validator](https://validator.w3.org/nu/?doc=https://gym-shop.herokuapp.com/profile).

>![profile.html validation](documentation/testing/validation/profile.html.png)

- No errors where found in `accounts app` when passed through the official [W3C's HTML Validator](https://validator.w3.org/nu/?doc=https://gym-shop.herokuapp.com/accounts).

>![accounts.html validation](documentation/testing/validation/accounts.html.png)

- 1 error was found in `payment app` when passed through the official [W3C's HTML Validator](https://validator.w3.org/nu/?doc=https://gym-shop.herokuapp.com/payment) and has now been amended.

>![payment.html validation](documentation/testing/validation/payment.html.png)



### CSS

  - 1 errors were found in any CSS files throughout the site when passed through the official CSS validator. All errors found were related to Bootstrap documentation and not from my custom CSS files. This error was fixed:
  
>![base.css validation](documentation/testing/validation/base.css.png)

- `payment.css` was taking from stripe documentation

### JavaScript

- No errors were found when `cart.js` was passed through the official [JSHint](https://jshint.com/) JavaScript validator., just 3 warnings;

>![script.js](documentation/testing/validation/cart.js.png)

- No errors were found when `checkout.js` was passed through the official [JSHint](https://jshint.com/) JavaScript validator., just 5 warnings;

>![script.js](documentation/testing/validation/checkout.js.png)

- `payment.js` was taken from stripe documentation

- No errors were found when `stripe_elements.js` was passed through the official [JSHint](https://jshint.com/) JavaScript validator.

>![script.js](documentation/testing/validation/stripe_elements.js.png)

- All Python code was valiadated with [pep8ish](https://pep8ci.herokuapp.com//)

  - No errors were returned and all code met PEP8 compliance when `store/admin.py` file was passed through Code Institute's Python Linter

    [store/admin.py validation](documentation/testing/validation/store.admin.py.png)
  
   - No errors were returned and all code met PEP8 compliance when `store/forms.py` file was passed through Code Institute's Python Linter

    [store/forms.py validation](documentation/testing/validation/store.forms.py.png)

   - No errors were returned and all code met PEP8 compliance when `store/models.py` file was passed through Code Institute's Python Linter

    [store/models.py validation](documentation/testing/validation/store.models.py.png)

   - No errors were returned and all code met PEP8 compliance when `store/urls.py` file was passed through Code Institute's Python Linter

    [store/urls.py validation](documentation/testing/validation/store.urls.py.png)

   - No errors were returned and all code met PEP8 compliance when `store/views.py` file was passed through Code Institute's Python Linter

    [store/views.py validation](documentation/testing/validation/store.views.py.png)

   - No errors were returned and all code met PEP8 compliance when `contact/admin.py` file was passed through Code Institute's Python Linter

   [contact/admin.py validation](documentation/testing/validation/contact.admin.py.png)

   - No errors were returned and all code met PEP8 compliance when `contact/forms.py` file was passed through Code Institute's Python Linter

   [contact/forms.py validation](documentation/testing/validation/contact.forms.py.png)

   - No errors were returned and all code met PEP8 compliance when `contact/models.py` file was passed through Code Institute's Python Linter

   [contact/models.py validation](documentation/testing/validation/contact.models.py.png)

   - No errors were returned and all code met PEP8 compliance when `contact/views.py` file was passed through Code Institute's Python Linter

   [contact/views.py validation](documentation/testing/validation/contact.views.py.png)

   - No errors were returned and all code met PEP8 compliance when `contact/urls.py` file was passed through Code Institute's Python Linter

   [contact/urls.py validation](documentation/testing/validation/contact.urls.py.png)

   - No errors were returned and all code met PEP8 compliance when `profile/admin.py` file was passed through Code Institute's Python Linter

   [profile/admin.py validation](documentation/testing/profile.admin.py.png)

   - No errors were returned and all code met PEP8 compliance when `profile/forms.py` file was passed through Code Institute's Python Linter

   [profile/forms.py validation](documentation/testing/profile.forms.py.png)

   - No errors were returned and all code met PEP8 compliance when `profile/models.py` file was passed through Code Institute's Python Linter

   [profile/models.py validation](documentation/testing/profile.models.py.png)

   - No errors were returned and all code met PEP8 compliance when `profile/urls.py` file was passed through Code Institute's Python Linter

   [profile/urls.py validation](documentation/testing/profile.urls.py.png)

   - No errors were returned and all code met PEP8 compliance when `profile/views.py` file was passed through Code Institute's Python Linter

   [profile/views.py validation](documentation/testing/profile.views.py.png)

   - No errors were returned and all code met PEP8 compliance when `payment/admin.py` file was passed through Code Institute's Python Linter

   [payment/admin.py validation](documentation/testing/payment.admin.py.png)

   - No errors were returned and all code met PEP8 compliance when `payment/models.py` file was passed through Code Institute's Python Linter

   [payment/models.py validation](documentation/testing/payment.models.py.png)

   - No errors were returned and all code met PEP8 compliance when `payment/urls.py` file was passed through Code Institute's Python Linter

   [payment/urls.py validation](documentation/testing/payment.urls.py.png)

   - No errors were returned and all code met PEP8 compliance when `payment/views.py` file was passed through Code Institute's Python Linter

   [payment/views.py validation](documentation/testing/payment.views.py.png)

   - No errors were returned and all code met PEP8 compliance when `gym_shop/settings.py` file was passed through Code Institute's Python Linter

   [gym_shop/settings.py validation](documentation/testing/gym_shop.settings.py.png)

   - No errors were returned and all code met PEP8 compliance when `gym_shop/urls.py` file was passed through Code Institute's Python Linter

   [gym_shop/urls.py validation](documentation/testing/gym_shop.urls.py.png)


### Fixed Bugs

- I had many bugs during deployment but this was due to environment variables not being set properly and had trouble with aws connecting.
- I had many bugs with the implimented stripe js payment but was just passing incorrect information to the function.
- Allauth was also not working after deployment and this was due to email settings not being set correctly and debug.
- Fixed issue with comment body not loading correctly, this was due to crispy form tags not being declared at top of html file.



## Browser Compatibility

- Website launched successfully on `Firefox`

  >![Firefox](documentation/testing/browser_compatibility/firefox.png)

- Website launched successfully on `Safari`

  >![Safari](documentation/testing/browser_compatibility/safari.png)

- Website launched successfully on `Chrome`

  >>![Chrome](documentation/testing/browser_compatibility/firefox.png
  
## Responsiveness

- Website viewed on a Smartphone:

  >![Mobile view](documentation/testing/device_compatibility/smartphone.png)

- Website viewed on a tablet device:

  >![Tablet view](documentation/testing/device_compatibility/tablet.png)

- Website viewed on a laptop device:

 >![Desktop view](documentation/testing/device_compatibility/desktop.png)


## User Story Testing

A target user of the GymShop website will want to:

- [x] Register an account
   >Users can register an account at GymShop, the backend of this functionality is handled by [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html).
   >![Register](documentation/testing/user_story/register.png)

- [] Store personal default delivery information
   >Profile owners can store their default delivery information - making checkout easier as the delivery section of the order form auto-populates.
   * This wasn't met, users are still required to enter delievry information on every new order

- [x] Amend profile information
   >Default delivery information can be updated.
   >![Update profile](documentation/testing/user_story/update-profile.png)

- [x] View past orders
   >Profile owners will be able to view their previous order history.
   >![Order history](documentation/features/recent_orders_card.png)

- [x] Reset their profile password
   >Profile owners will be able to reset their password via email-authentication, this functionality is handled by [django-allauth](https://django-allauth.readthedocs.io/en/latest/
   >![Reset password](documentation/testing/user_story/password-reset.png)

- [x] Navigate the site
   >The navbar and footer make it easy for users to navigate the site as well as useful buttons and internal links throughout the website. The site is simple to navigate.
   >![Main navbar](documentation/features/nav_bar.png)
  

- [x] View products
   >All products can be viewed in the store.
   >![Store](documentation/features/store.png)

- [x] Filter Deilen products
   >Products can be searched for specific keywords in the search bar.
   >![Search](documentation/features/search.png)

- [x] Purchase products
   >Users can purchase products by adding the desired quantities to their cart and continuing with checkout to pay and finalise their order.
   >![Add product to bag](documentation/features/payment.png)

- [x] Amend their order
   >In the cart, users will be given an overview of their proposed purchase. Users can then amend quantities of an item, remove items competely and continue shopping if they desire. 
   >![Amend order](documentation/features/cart.png)

- [x] See an order summary with all cost details
   >An order summary is listed in the cart and again at checkout showing all costs and total cost of the purchase. There are no hidden costs. The amount that a user will be charged is clearly displayed before purchase.
   >![Order summary](documentation/features/checkout.png)

- [x] Checkout safely and securely
   >The site uses Stripe Payments to acheive safe and secure transactions. More can be read about this at [Stripe.com](https://stripe.com/en-gb).
   >![Stripe payment](documentation/features/stripe_confirmation.png)

- [*] Receive order confirmation
   >Once an order has been made, the user will be shown the checkout success page which informs the user that their order has been processed. Email confirmation will also be sent to the user. Additionally, if a user has a profile they will be able to see processed order in their order history on their profile.
   * This user story was not met however users are redirected to a order complete page and are able to view their recent orders

- [x] Contact GymShop
   >Store users will need to be able to contact GymShop if they have any questions or need help with their order. The website has multiple useful links in the footer which outline company policy on returns and refunds, delivery and shipping, and privacy policy as well as an FAQ section. These links are full of customer information they may wish to read before making a purchase. If store users have any other queries or concerns, there is a contact us section where a form is submitted with a customer message.
   >![Contact form](documentation/testing/user_story/contact-form.png)

- [x] Manage their account
   >Users are able to login, logout, register, confirm their email address, and reset their password. All of this functionality is handled by [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html).

An admin of the Gymshop app will want to:

- [x] Have secure access to product management
   >Login is required to access any urls regarding product management. If the user logged in is not identified as an admin of the site, they will be redirected and thrown an error. Only admins have access to admin privileges.
   
- [x] Add new products
   >Admins can easily add new products by navigating to the product management section under their account. Completing and submitting the form will result in a new product being displayed on the site.
   >![Add product](documentation/features/add.png)

- [x] Edit existing products
   >From a product's details page, an admin can easily update the details of said product.
   >![Admin controls](documentation/features/update.png)

- [x] Delete products
   >From a product's details page, an admin can easily delete said product. Before deletion a modal is triggered to ensure no accidental deletion.
   >![Delete modal](documentation/features/delete.png)

- [x] View all orders, products, product categories, and customer messages
   >All of this information can be viewed when an admin logs into the customised django admin. Django provides a built in admin interface which acts as a internal management tool. More information can be read about Django admin [here](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/). Gymshop's django admin can be accessed [here](https://gym-shop.herokuapp.com/admin/) (please note, admin login is required). 

## Defensive Programming Testing

- Code is implemented on all admin features to require user login and to verify that the logged in user has admin status. If a user is not logged in or is not an admin, they will be redirected and unable to perform admin privileges. This works even when trying to brute force a url.
  `@login_required` on admin views to require user to be logged in. The following code was used to verify admin status:
  ```
  if not request.user.is_superuser:
        messages.error(request, "Sorry, no access - admins only!")
        return redirect(reverse("home"))
  ```
  If the user is a superuser i.e., admin, then they will not be redirected and will have access to admin functionality. This functionality was manually tested and is functioning correctly.