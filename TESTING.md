# Testing 

## Validator Testing 
- HTML
- CSS

### JavaScript
- No errors were found when `cart.js` was passed through the official [JSHint](https://jshint.com/) JavaScript validator., just 3 warnings;

>![script.js](documentation/testing/validation/cart.js.png)

- No errors were found when `checkout.js` was passed through the official [JSHint](https://jshint.com/) JavaScript validator., just 5 warnings;

>![script.js](documentation/testing/validation/checkout.js.png)

- `payment.js` was taken from stripe documentation

- No errors were found when `stripe_elements.js` was passed through the official [JSHint](https://jshint.com/) JavaScript validator.

>![script.js](documentation/testing/validation/stripe_elements.js.png)





- Python

### Fixed Bugs


## Browser Compatibility


## Responsiveness


## User Story Testing


## Defensive Programming Testing

- Code is implemented on all admin features to require user login and to verify that the logged in user has admin status. If a user is not logged in or is not an admin, they will be redirected and unable to perform admin privileges. This works even when trying to brute force a url.
  `@login_required` on admin views to require user to be logged in. The following code was used to verify admin status:
  ```
  if not request.user.is_superuser:
        messages.error(request, "Sorry, no access - admins only!")
        return redirect(reverse("home"))
  ```
  If the user is a superuser i.e., admin, then they will not be redirected and will have access to admin functionality. This functionality was manually tested and is functioning correctly.