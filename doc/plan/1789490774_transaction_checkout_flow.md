# Plan: Transaction and Checkout Flow

## Objective

Add `Transaction` and `LineItem` persistence, create the authenticated checkout page, and convert a user's cart items into a transaction on POST.

## Task board

- [ ] Commit this approved plan on `main`.
- [ ] Create and switch to a feature branch.
- [ ] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [ ] Import `datetime as dt`, `Transaction`, and `LineItem` in `core/models.py`/`core/views.py` as appropriate.
- [ ] Add `Transaction` and `LineItem` models with the requested fields and foreign keys.
- [ ] Create and apply the new core migration.
- [ ] Register the checkout route at `checkout`.
- [ ] Create `core/templates/core/checkout.html` with cart rows, checkout form, empty-cart message, greeting, and back link.
- [ ] Add the `/checkout` link to the authenticated index template.
- [ ] Implement authenticated checkout GET rendering and POST conversion to a `Transaction` and `LineItem` rows.
- [ ] Delete converted CartItems, add the thank-you message, and redirect to `index`.
- [ ] Run `python manage.py check`, `makemigrations --check`, and the test suite.
- [ ] Verify authenticated GET checkout with cart items and empty cart behavior.
- [ ] Seed temporary cart items, POST checkout, and verify transaction/line-item creation and cart clearing.
- [ ] Verify the thank-you message and anonymous checkout protection.
- [ ] Clean up temporary verification rows and confirm no database, cache, or virtual-environment files are tracked.
- [ ] Update this plan with execution results and synchronize living documentation.
- [ ] Commit the implementation as `feat: add transaction checkout flow`.
- [ ] Rendezvous:
  - [ ] Confirm the codebase is workable.
  - [ ] Merge the feature branch into `main`.
  - [ ] Push the completed snapshot to GitHub.

## Constraints

- Use the requested UTC-aware `created_at` value.
- Preserve the existing cart and authentication behavior.
- Do not add totals, payment processing, transaction status, or atomic transaction handling in this change.
- Do not commit test data, credentials, or the SQLite database.

## Expected result

An authenticated user can view their cart at `/checkout`, submit checkout, receive a persisted transaction with matching line items, have cart items removed, and see a thank-you message after redirect.
