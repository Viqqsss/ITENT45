# Plan: Database-Backed Product Detail Links

## Objective

Update the product list and detail views to match the requested database-backed implementation and link each product row to its detail route.

## Task board

- [ ] Commit this approved plan on `main`.
- [ ] Create and switch to a feature branch.
- [ ] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [ ] Preserve `from .models import Product` in `core/views.py`.
- [ ] Change `index` to use `Product.objects.all()` while preserving template rendering.
- [ ] Change `product_detail` to retrieve `Product.objects.get(id=product_id)` and return the product name.
- [ ] Update `core/templates/core/index.html` with `Name` and `Price` headers and product-ID links.
- [ ] Run `python manage.py check` and the test suite.
- [ ] Verify `/` returns HTTP 200, table headers, and links for existing product IDs.
- [ ] Verify an existing `/product/<id>` route returns the corresponding product name.
- [ ] Verify and record behavior for an unknown product ID without adding unrequested 404 handling.
- [ ] Review the diff and confirm no database, migration, cache, or virtual-environment files changed.
- [ ] Update this plan with execution results and synchronize living documentation.
- [ ] Commit the implementation as `feat: link product list to database details`.
- [ ] Rendezvous:
  - [ ] Confirm the codebase is workable.
  - [ ] Merge the feature branch into `main`.
  - [ ] Push the completed snapshot to GitHub.

## Constraints

- Use the exact `Product.objects.all()` query and `Product.objects.get(id=product_id)` behavior requested.
- Preserve the existing URL patterns and root route.
- Do not add migrations, models, or unrelated UI behavior.
- Keep the missing-product behavior unchanged from the requested direct `.get()` implementation.

## Expected result

The root table displays `Name` and `Price`, each product name links to `/product/<id>`, and each existing detail URL returns that product's name.
