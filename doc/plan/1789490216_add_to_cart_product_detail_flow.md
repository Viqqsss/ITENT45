# Plan: Add-to-Cart Product Detail Flow

## Objective

Add an authenticated quantity form to product details, create a `CartItem` on POST, show a success message on the product list, and preserve the existing GET detail behavior.

## Task board

- [ ] Commit this approved plan on `main`.
- [ ] Create and switch to a feature branch.
- [ ] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [ ] Add `redirect`, `login`, `logout`, `authenticate`, and `messages` imports as needed, plus `CartItem` in `core/views.py`.
- [ ] Replace `product_detail.html` with the requested product detail and add-to-cart form.
- [ ] Extend `product_detail` with the requested POST branch that creates a `CartItem`, adds the success message, and redirects to `index`.
- [ ] Add the messages block to `core/templates/core/index.html`, using `message.tags` for the current message.
- [ ] Run `python manage.py check` and the test suite.
- [ ] Log in as `cafeadmin` through the test client.
- [ ] Verify GET detail contains the product data, form, hidden product ID, quantity input, and CSRF token.
- [ ] POST a valid quantity and product ID; verify redirect to `/`, one CartItem owned by `cafeadmin`, and the success message.
- [ ] Verify anonymous POSTs remain redirected by `login_required`.
- [ ] Remove temporary test CartItems and confirm no migration is needed.
- [ ] Review the diff and confirm no database, cache, or virtual-environment files are tracked.
- [ ] Update this plan with execution results and synchronize living documentation.
- [ ] Commit the implementation as `feat: add cart item from product detail`.
- [ ] Rendezvous:
  - [ ] Confirm the codebase is workable.
  - [ ] Merge the feature branch into `main`.
  - [ ] Push the completed snapshot to GitHub.

## Constraints

- Preserve `login_required` on `product_detail`.
- Use the authenticated `request.user`; do not accept a user ID from the form.
- Keep the requested redirect and success-message text.
- Do not add quantity validation, cart merging, migrations, or unrelated UI behavior.
- Do not commit test database rows or credentials.

## Expected result

An authenticated user can submit a product quantity, receive a `CartItem`, return to the product list, and see an informational confirmation message.
