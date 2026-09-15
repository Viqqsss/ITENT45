# Plan: Dynamic Product Detail Routing

## Objective

Add a dynamic integer product-detail route while preserving the existing product list at `/`.

## Task board

- [x] Commit this approved plan on `main`.
- [x] Create and switch to a feature branch.
- [x] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [x] Add `product_detail(request, product_id)` to `digitalcaferoot/digitalcafe/core/views.py`, returning `HttpResponse(str(product_id))`.
- [x] Add `path("product/<int:product_id>", views.product_detail, name="product_detail")` to `core/urls.py` while preserving the index route.
- [x] Run `python manage.py check` and the test suite.
- [x] Verify `/` still returns HTTP 200 and the product table.
- [x] Verify `/product/123` returns HTTP 200 with body `123`.
- [x] Verify a non-integer route such as `/product/abc` returns HTTP 404.
- [x] Review the diff and confirm no database, cache, or virtual-environment files changed.
- [x] Update this plan with execution results and synchronize living documentation.
- [x] Commit the implementation as `feat: add dynamic product detail route`.
- [x] Rendezvous:
  - [x] Confirm the codebase is workable.
  - [x] Merge the feature branch into `main`.
  - [x] Push the completed snapshot to GitHub.

## Constraints

- Preserve the existing database-backed product list and root URL.
- Use the exact integer converter and plain-text response requested.
- Do not fetch a `Product` record or add 404 object handling in this change.
- Do not add migrations, models, templates, or unrelated routes.

## Expected result

The root page remains the product list, `/product/123` returns `123`, and non-integer product paths do not match.

## Execution results

- Executed on branch `feat/dynamic-product-detail` with Conda inactive and `digitalcaferoot/env` active.
- Added `product_detail` and the `product/<int:product_id>` URL pattern.
- Django system check passed and the test suite completed with no discovered tests.
- Test client confirmed `/` returns HTTP 200 with the product table.
- Test client confirmed `/product/123` returns HTTP 200 with body `123`.
- Test client confirmed `/product/abc` returns HTTP 404.
