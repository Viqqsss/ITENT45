# Study: Add-to-Cart Product Detail Flow

## Objective

Add a quantity form to the product detail page and handle authenticated POST requests by creating a `CartItem`, displaying a success message, and redirecting back to the product list.

## Current state

- `Product` detail is rendered by `core/product_detail.html`.
- `product_detail` is already protected by `login_required` and currently handles GET only.
- `CartItem` exists and is registered in admin with user, product, and quantity fields.
- Django messages middleware is enabled.
- The index template does not yet render queued messages.

## Requested changes

### Detail template

Replace `core/templates/core/product_detail.html` with a product-details heading, back link, product fields, and a CSRF-protected POST form containing:

- Hidden `product_id`
- Numeric `quantity` input defaulting to `1`
- `Add to cart` submit button

### Product-detail POST handling

Extend `product_detail` with a POST branch that:

1. Reads submitted quantity and product ID.
2. Retrieves the product.
3. Uses `request.user` as the cart owner.
4. Creates and saves a `CartItem`.
5. Adds an informational message: `Added {submitted_quantity} of {product.name} to your cart`.
6. Redirects to the named `index` route.

The view will need `redirect` and `messages` imports, plus `CartItem` alongside `Product`.

### Index messages

Add the supplied message-list block to `core/templates/core/index.html`. The message class condition should use `message.tags` for the current message; this corrects the supplied `messages.tags` typo while preserving the intended styling behavior.

## Feasibility

The change fits the current authenticated flow. Existing login protection ensures `request.user` is authenticated for POSTs, the `CartItem` table is migrated, and the named index route exists for the redirect.

## Tradeoffs and edge cases

- The requested code creates a new line item for every submission; it does not merge with an existing item for the same user/product.
- Quantity is accepted as submitted text and stored in an integer field; invalid or negative input may raise a validation/database error. Input constraints and validation can be hardened later.
- The hidden product ID is user-controlled, so the view must continue retrieving the product from the database and assigning the authenticated request user rather than trusting a user ID from the form.
- Redirect-after-POST prevents duplicate submissions on refresh and allows the success message to display on the index page.

## Verification strategy

With Conda deactivated and `digitalcaferoot/env` active:

- Run `python manage.py check` and the test suite.
- Log in as `cafeadmin` through the test client.
- GET an existing product detail page and verify the form fields and CSRF token.
- POST a quantity and product ID; verify redirect to `/`, one `CartItem` owned by `cafeadmin`, and the success message on the index page.
- Confirm anonymous POSTs remain redirected by `login_required`.
- Confirm no migration is needed and no database, cache, or virtual-environment files are tracked.

## Recommendation

Implement the requested template and POST behavior, correct the message-tag reference, verify CartItem creation and redirect messaging, update the plan/wiki, and complete rendezvous.
