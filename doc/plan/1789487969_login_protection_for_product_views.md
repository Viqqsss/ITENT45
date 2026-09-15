# Plan: Login Protection for Product Views

## Objective

Require authenticated users for the existing product-list and product-detail views using Django's `login_required` decorator.

## Task board

- [ ] Commit this approved plan on `main`.
- [ ] Create and switch to a feature branch.
- [ ] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [ ] Add `from django.contrib.auth.decorators import login_required` to `core/views.py`.
- [ ] Add `@login_required` immediately above `index`.
- [ ] Add `@login_required` immediately above `product_detail`.
- [ ] Run `python manage.py check` and the test suite.
- [ ] Use an anonymous test client to verify `/` and `/product/<id>` return HTTP 302 redirects containing the original path in `next`.
- [ ] Log in through the test client as the local `cafeadmin` account and verify both views remain HTTP 200 with their existing content.
- [ ] Review the diff and confirm no database schema, cache, or virtual-environment files changed.
- [ ] Update this plan with execution results and synchronize living documentation.
- [ ] Commit the implementation as `feat: protect product views with login`
- [ ] Rendezvous:
  - [ ] Confirm the codebase is workable.
  - [ ] Merge the feature branch into `main`.
  - [ ] Push the completed snapshot to GitHub.

## Constraints

- Preserve the existing list/detail behavior for authenticated users.
- Do not add a login page or change `LOGIN_URL` in this feature.
- Do not add models, migrations, or unrelated authorization rules.
- Keep the current direct product lookup behavior unchanged.

## Expected result

Anonymous users are redirected to Django's configured login URL for both product views, while authenticated users can continue to use the product list and detail pages.
