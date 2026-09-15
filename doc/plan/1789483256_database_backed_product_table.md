# Plan: Database-Backed Product Table

## Objective

Render products as an HTML table, add Espresso at PHP 100 to the local database, and source the index view's product data from `core.models.Product`.

## Task board

- [x] Commit this approved plan on `main`.
- [x] Create and switch to a feature branch.
- [x] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [x] Update `core/templates/core/index.html` with a table, header row, and one data row per product.
- [x] Update `core/views.py` to query `Product.objects.order_by("price")` while preserving the `product_data` context key.
- [x] Run `python manage.py makemigrations core` and confirm no new schema migration is needed.
- [x] Run `python manage.py migrate` and confirm the database is current.
- [x] Use the Django shell with `get_or_create` to add Espresso at PHP 100 without duplicates.
- [x] Verify the queryset returns Espresso, Americano, and Cappuccino at the expected prices.
- [x] Run `python manage.py check` and `python manage.py test`.
- [x] Start the development server, perform one HTTP request to `/`, verify table headers and all three products, then stop the server.
- [x] Review the diff and confirm `db.sqlite3`, caches, and `env/` remain untracked.
- [x] Update this plan with execution results and synchronize living documentation.
- [x] Commit the implementation as `feat: render database-backed product table`.
- [x] Rendezvous:
  - [x] Confirm the codebase is workable.
  - [x] Merge the feature branch into `main`.
  - [x] Push the completed snapshot to GitHub.

## Constraints

- Keep the existing `Product` model schema unchanged.
- Preserve the `product_data` context key and root URL.
- Use idempotent sample-data creation; do not duplicate Espresso.
- Do not add models, styling, or unrelated application behavior.
- Do not commit the local SQLite database.

## Expected result

The root page renders a two-column product table containing Espresso (PHP 100), Americano (PHP 110), and Cappuccino (PHP 140), sourced from the database.

## Execution results

- Executed on branch `feat/database-backed-product-table` with Conda inactive and `digitalcaferoot/env` active.
- Replaced the unordered list with a semantic two-column table and header row.
- Switched `core.views.index` to `Product.objects.order_by("price")`.
- `makemigrations core` reported no schema changes; `migrate` reported no migrations to apply.
- Idempotently seeded Espresso at PHP 100; the queryset returned Espresso, Americano, and Cappuccino ordered by price.
- Django checks passed and the test suite completed with no discovered tests.
- The development server returned HTTP 200; table and all requested products/prices were verified in the response.
- Local database state remains ignored and the temporary server was stopped.
