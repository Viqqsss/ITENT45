# Plan: Database-Backed Product Table

## Objective

Render products as an HTML table, add Espresso at PHP 100 to the local database, and source the index view's product data from `core.models.Product`.

## Task board

- [ ] Commit this approved plan on `main`.
- [ ] Create and switch to a feature branch.
- [ ] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [ ] Update `core/templates/core/index.html` with a table, header row, and one data row per product.
- [ ] Update `core/views.py` to query `Product.objects.order_by("price")` while preserving the `product_data` context key.
- [ ] Run `python manage.py makemigrations core` and confirm no new schema migration is needed.
- [ ] Run `python manage.py migrate` and confirm the database is current.
- [ ] Use the Django shell with `get_or_create` to add Espresso at PHP 100 without duplicates.
- [ ] Verify the queryset returns Espresso, Americano, and Cappuccino at the expected prices.
- [ ] Run `python manage.py check` and `python manage.py test`.
- [ ] Start the development server, perform one HTTP request to `/`, verify table headers and all three products, then stop the server.
- [ ] Review the diff and confirm `db.sqlite3`, caches, and `env/` remain untracked.
- [ ] Update this plan with execution results and synchronize living documentation.
- [ ] Commit the implementation as `feat: render database-backed product table`.
- [ ] Rendezvous:
  - [ ] Confirm the codebase is workable.
  - [ ] Merge the feature branch into `main`.
  - [ ] Push the completed snapshot to GitHub.

## Constraints

- Keep the existing `Product` model schema unchanged.
- Preserve the `product_data` context key and root URL.
- Use idempotent sample-data creation; do not duplicate Espresso.
- Do not add models, styling, or unrelated application behavior.
- Do not commit the local SQLite database.

## Expected result

The root page renders a two-column product table containing Espresso (PHP 100), Americano (PHP 110), and Cappuccino (PHP 140), sourced from the database.
