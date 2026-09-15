# Plan: Login Protection for Product Views

## Objective

Require authenticated users for the existing product-list and product-detail views using Django's `login_required` decorator.

## Task board

- [x] Commit this approved plan on `main`.
- [x] Create and switch to a feature branch.
- [x] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [x] Add `from django.contrib.auth.decorators import login_required` to `core/views.py`.
- [x] Add `@login_required` immediately above `index`.
- [x] Add `@login_required` immediately above `product_detail`.
- [x] Run `python manage.py check` and the test suite.
- [x] Use an anonymous test client to verify `/` and `/product/<id>` return HTTP 302 redirects containing the original path in `next`.
- [x] Log in through the test client as the local `cafeadmin` account and verify both views remain HTTP 200 with their existing content.
- [x] Review the diff and confirm no database schema, cache, or virtual-environment files changed.
- [x] Update this plan with execution results and synchronize living documentation.
- [x] Commit the implementation as `feat: protect product views with login`.
- [x] Rendezvous:
  - [x] Confirm the codebase is workable.
  - [x] Merge the feature branch into `main`.
  - [x] Push the completed snapshot to GitHub.

## Constraints

- Preserve the existing list/detail behavior for authenticated users.
- Do not add a login page or change `LOGIN_URL` in this feature.
- Do not add models, migrations, or unrelated authorization rules.
- Keep the current direct product lookup behavior unchanged.

## Expected result

Anonymous users are redirected to Django's configured login URL for both product views, while authenticated users can continue to use the product list and detail pages.

## Execution results

- Executed on branch `feat/protect-product-views` with Conda inactive and `digitalcaferoot/env` active.
- Added `login_required` to both product views.
- Django system check passed and the test suite completed with no discovered tests.
- Anonymous requests to `/` and `/product/<id>` returned HTTP 302 redirects with `next` parameters.
- The local `cafeadmin` account authenticated successfully; both protected views returned HTTP 200.
- No database schema or local environment files changed.
