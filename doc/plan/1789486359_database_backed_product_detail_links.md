# Plan: Database-Backed Product Detail Links

## Objective

Update the product list and detail views to match the requested database-backed implementation and link each product row to its detail route.

## Task board

- [x] Commit this approved plan on `main`.
- [x] Create and switch to a feature branch.
- [x] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [x] Preserve `from .models import Product` in `core/views.py`.
- [x] Change `index` to use `Product.objects.all()` while preserving template rendering.
- [x] Change `product_detail` to retrieve `Product.objects.get(id=product_id)` and return the product name.
- [x] Update `core/templates/core/index.html` with `Name` and `Price` headers and product-ID links.
- [x] Run `python manage.py check` and the test suite.
- [x] Verify `/` returns HTTP 200, table headers, and links for existing product IDs.
- [x] Verify an existing `/product/<id>` route returns the corresponding product name.
- [x] Verify and record behavior for an unknown product ID without adding unrequested 404 handling.
- [x] Review the diff and confirm no database, migration, cache, or virtual-environment files changed.
- [x] Update this plan with execution results and synchronize living documentation.
- [x] Commit the implementation as `feat: link product list to database details`.
- [x] Rendezvous:
  - [x] Confirm the codebase is workable.
  - [x] Merge the feature branch into `main`.
  - [x] Push the completed snapshot to GitHub.

## Constraints

- Use the exact `Product.objects.all()` query and `Product.objects.get(id=product_id)` behavior requested.
- Preserve the existing URL patterns and root route.
- Do not add migrations, models, or unrelated UI behavior.
- Keep the missing-product behavior unchanged from the requested direct `.get()` implementation.

## Expected result

The root table displays `Name` and `Price`, each product name links to `/product/<id>`, and each existing detail URL returns that product's name.

## Execution results

- Executed on branch `feat/database-product-detail-links` with Conda inactive and `digitalcaferoot/env` active.
- `index` now uses `Product.objects.all()`.
- `product_detail` retrieves the model by ID and returns its name.
- The table uses the requested `Name` and `Price` headers and links each product name to its detail URL.
- Django system check passed and the test suite completed with no discovered tests.
- Existing product detail requests return the corresponding name; an unknown ID returns HTTP 500 because the requested direct `.get()` raises `Product.DoesNotExist`.
