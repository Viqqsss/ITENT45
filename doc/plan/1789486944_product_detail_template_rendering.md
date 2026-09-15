# Plan: Product Detail Template Rendering

## Objective

Render each product detail route through a dedicated template containing the product name, price, and a link back to the product list.

## Task board

- [x] Commit this approved plan on `main`.
- [x] Create and switch to a feature branch.
- [x] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [x] Create `digitalcaferoot/digitalcafe/core/templates/core/product_detail.html` with the requested back link and conditional product fields.
- [x] Update `core.views.product_detail` to load `core/product_detail.html`, pass the selected `Product` as `product`, and render the response.
- [x] Run `python manage.py check` and the test suite.
- [x] Verify the detail template is discoverable.
- [x] Verify an existing `/product/<id>` response contains the product name, price, and `Back to products` link.
- [x] Verify `/` remains functional.
- [x] Review the diff and confirm no database, migration, cache, or virtual-environment files changed.
- [x] Update this plan with execution results and synchronize living documentation.
- [x] Commit the implementation as `feat: render product detail template`.
- [x] Rendezvous:
  - [x] Confirm the codebase is workable.
  - [x] Merge the feature branch into `main`.
  - [x] Push the completed snapshot to GitHub.

## Constraints

- Use the requested template loader and context key `product`.
- Preserve the existing product-detail URL and direct `Product.objects.get(...)` behavior.
- Do not add migrations, models, styling, or unrelated route changes.

## Expected result

An existing product detail URL renders the product name and price in `product_detail.html` and provides a working link back to `/`.

## Execution results

- Executed on branch `feat/product-detail-template` with Conda inactive and `digitalcaferoot/env` active.
- Added `core/templates/core/product_detail.html` with product fields and the back link.
- Converted `product_detail` to render the template with the selected `Product` context.
- Django system check passed and the test suite completed with no discovered tests.
- Template discovery succeeded; an existing detail route returned HTTP 200 with the expected name, price, and link.
- The root product list continued to return HTTP 200.
