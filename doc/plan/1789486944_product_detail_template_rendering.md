# Plan: Product Detail Template Rendering

## Objective

Render each product detail route through a dedicated template containing the product name, price, and a link back to the product list.

## Task board

- [ ] Commit this approved plan on `main`.
- [ ] Create and switch to a feature branch.
- [ ] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [ ] Create `digitalcaferoot/digitalcafe/core/templates/core/product_detail.html` with the requested back link and conditional product fields.
- [ ] Update `core.views.product_detail` to load `core/product_detail.html`, pass the selected `Product` as `product`, and render the response.
- [ ] Run `python manage.py check` and the test suite.
- [ ] Verify the detail template is discoverable.
- [ ] Verify an existing `/product/<id>` response contains the product name, price, and `Back to products` link.
- [ ] Verify `/` remains functional.
- [ ] Review the diff and confirm no database, migration, cache, or virtual-environment files changed.
- [ ] Update this plan with execution results and synchronize living documentation.
- [ ] Commit the implementation as `feat: render product detail template`.
- [ ] Rendezvous:
  - [ ] Confirm the codebase is workable.
  - [ ] Merge the feature branch into `main`.
  - [ ] Push the completed snapshot to GitHub.

## Constraints

- Use the requested template loader and context key `product`.
- Preserve the existing product-detail URL and direct `Product.objects.get(...)` behavior.
- Do not add migrations, models, styling, or unrelated route changes.

## Expected result

An existing product detail URL renders the product name and price in `product_detail.html` and provides a working link back to `/`.
