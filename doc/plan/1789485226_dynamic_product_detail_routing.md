# Plan: Dynamic Product Detail Routing

## Objective

Add a dynamic integer product-detail route while preserving the existing product list at `/`.

## Task board

- [ ] Commit this approved plan on `main`.
- [ ] Create and switch to a feature branch.
- [ ] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [ ] Add `product_detail(request, product_id)` to `digitalcaferoot/digitalcafe/core/views.py`, returning `HttpResponse(str(product_id))`.
- [ ] Add `path("product/<int:product_id>", views.product_detail, name="product_detail")` to `core/urls.py` while preserving the index route.
- [ ] Run `python manage.py check` and the test suite.
- [ ] Verify `/` still returns HTTP 200 and the product table.
- [ ] Verify `/product/123` returns HTTP 200 with body `123`.
- [ ] Verify a non-integer route such as `/product/abc` returns HTTP 404.
- [ ] Review the diff and confirm no database, cache, or virtual-environment files changed.
- [ ] Update this plan with execution results and synchronize living documentation.
- [ ] Commit the implementation as `feat: add dynamic product detail route`.
- [ ] Rendezvous:
  - [ ] Confirm the codebase is workable.
  - [ ] Merge the feature branch into `main`.
  - [ ] Push the completed snapshot to GitHub.

## Constraints

- Preserve the existing database-backed product list and root URL.
- Use the exact integer converter and plain-text response requested.
- Do not fetch a `Product` record or add 404 object handling in this change.
- Do not add migrations, models, templates, or unrelated routes.

## Expected result

The root page remains the product list, `/product/123` returns `123`, and non-integer product paths do not match.
