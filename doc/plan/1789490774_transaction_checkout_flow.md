# Plan: Transaction and Checkout Flow

## Objective

Add `Transaction` and `LineItem` persistence, create the authenticated checkout page, and convert a user's cart items into a transaction on POST.

## Task board

- [x] Commit this approved plan on `main`.
- [x] Create and switch to a feature branch.
- [x] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [x] Import `datetime as dt`, `Transaction`, and `LineItem` in `core/models.py`/`core/views.py` as appropriate.
- [x] Add `Transaction` and `LineItem` models with the requested fields and foreign keys.
- [x] Create and apply the new core migration.
- [x] Register the checkout route at `checkout`.
- [x] Create `core/templates/core/checkout.html` with cart rows, checkout form, empty-cart message, greeting, and back link.
- [x] Add the `/checkout` link to the authenticated index template.
- [x] Implement authenticated checkout GET rendering and POST conversion to a `Transaction` and `LineItem` rows.
- [x] Delete converted CartItems, add the thank-you message, and redirect to `index`.
- [x] Run `python manage.py check`, `makemigrations --check`, and the test suite.
- [x] Verify authenticated GET checkout with cart items and empty cart behavior.
- [x] Seed temporary cart items, POST checkout, and verify transaction/line-item creation and cart clearing.
- [x] Verify the thank-you message and anonymous checkout protection.
- [x] Clean up temporary verification rows and confirm no database, cache, or virtual-environment files are tracked.
- [x] Update this plan with execution results and synchronize living documentation.
- [x] Commit the implementation as `feat: add transaction checkout flow`.
- [x] Rendezvous:
  - [x] Confirm the codebase is workable.
  - [x] Merge the feature branch into `main`.
  - [x] Push the completed snapshot to GitHub.

## Constraints

- Use the requested UTC-aware `created_at` value.
- Preserve the existing cart and authentication behavior.
- Do not add totals, payment processing, transaction status, or atomic transaction handling in this change.
- Do not commit test data, credentials, or the SQLite database.

## Expected result

An authenticated user can view their cart at `/checkout`, submit checkout, receive a persisted transaction with matching line items, have cart items removed, and see a thank-you message after redirect.

## Execution results

- Executed on branch `feat/transaction-checkout-flow` with Conda inactive and `digitalcaferoot/env` active.
- Added `Transaction` and `LineItem` models and applied `core/migrations/0003_transaction_lineitem.py`.
- Added the checkout route, template, index link, and authenticated GET/POST checkout logic.
- Checkout conversion created two line items, cleared the temporary cart, redirected to the index, and rendered the thank-you message.
- Empty-cart state rendered `No cart items.` and anonymous checkout returned HTTP 302.
- Django checks passed, no migration changes remained, and the test suite completed with no discovered tests.
- Temporary transaction and line-item verification data was removed.
