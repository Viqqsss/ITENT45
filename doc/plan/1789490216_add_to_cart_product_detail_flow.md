# Plan: Add-to-Cart Product Detail Flow

## Objective

Add an authenticated quantity form to product details, create a `CartItem` on POST, show a success message on the product list, and preserve the existing GET detail behavior.

## Task board

- [x] Commit this approved plan on `main`.
- [x] Create and switch to a feature branch.
- [x] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [x] Add `redirect`, `login`, `logout`, `authenticate`, and `messages` imports as needed, plus `CartItem` in `core/views.py`.
- [x] Replace `product_detail.html` with the requested product detail and add-to-cart form.
- [x] Extend `product_detail` with the requested POST branch that creates a `CartItem`, adds the success message, and redirects to `index`.
- [x] Add the messages block to `core/templates/core/index.html`, using `message.tags` for the current message.
- [x] Run `python manage.py check` and the test suite.
- [x] Log in as `cafeadmin` through the test client.
- [x] Verify GET detail contains the product data, form, hidden product ID, quantity input, and CSRF token.
- [x] POST a valid quantity and product ID; verify redirect to `/`, one CartItem owned by `cafeadmin`, and the success message.
- [x] Verify anonymous POSTs remain redirected by `login_required`.
- [x] Remove temporary test CartItems and confirm no migration is needed.
- [x] Review the diff and confirm no database, cache, or virtual-environment files are tracked.
- [x] Update this plan with execution results and synchronize living documentation.
- [x] Commit the implementation as `feat: add cart item from product detail`.
- [x] Rendezvous:
  - [x] Confirm the codebase is workable.
  - [x] Merge the feature branch into `main`.
  - [x] Push the completed snapshot to GitHub.

## Constraints

- Preserve `login_required` on `product_detail`.
- Use the authenticated `request.user`; do not accept a user ID from the form.
- Keep the requested redirect and success-message text.
- Do not add quantity validation, cart merging, migrations, or unrelated UI behavior.
- Do not commit test database rows or credentials.

## Expected result

An authenticated user can submit a product quantity, receive a `CartItem`, return to the product list, and see an informational confirmation message.

## Execution results

- Executed on branch `feat/add-to-cart-flow` with Conda inactive and `digitalcaferoot/env` active.
- Added the requested product detail quantity form and CSRF token.
- Added POST handling that creates a `CartItem`, adds the success message, and redirects to `index`.
- Added message rendering to the product list.
- Django checks passed, the test suite completed with no discovered tests, and no migration changes were pending.
- Authenticated POST created a temporary quantity-3 item and rendered the success message; the test item was removed.
- Anonymous POST remained protected by `login_required`.
