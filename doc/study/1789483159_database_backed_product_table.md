# Study: Database-Backed Product Table

## Objective

Extend the Digital Cafe product page so it renders products in an HTML table, add Espresso at PHP 100, and source the view data from the persisted `Product` model instead of a hardcoded list.

## Current state

- `core.models.Product` already exists with `name` and integer `price` fields.
- The initial migration has been applied locally.
- `core.views.index` currently uses an in-memory two-item list.
- `core/templates/core/index.html` currently renders an unordered list.
- The `core` app is registered and template discovery is active.

## Requested changes

### Template output

Replace the unordered list with a table containing:

- A header row with `Product name` and `Product price` columns.
- One data row per item in the view's `products` context.
- Product prices displayed with the `PHP` prefix.

A table is more semantically appropriate for product/price records than a list and gives the page a stable two-column structure.

### Database seed

Create Espresso in the local database with a price of 100 using the Django shell. The seed operation should be idempotent with `get_or_create` so repeated verification does not create duplicates.

### Database-backed view

Replace the hardcoded list in `core.views.index` with a query such as:

```python
products = Product.objects.order_by("price")
```

The existing context key `product_data` can remain unchanged, so the template continues to iterate over `product_data` while receiving model instances from the database.

## Migration implications

Adding Espresso is a data change, not a schema change. No new migration file should be generated. Execution should still run:

```bash
python manage.py makemigrations --check
python manage.py migrate
```

`makemigrations --check` should report no changes, while `migrate` should report that the database is already up to date. The local SQLite database remains ignored by Git.

## Feasibility

The change is immediately feasible. The model and database table already exist, and Django templates can iterate over `Product` model instances using the same dot notation (`product_record.name`, `product_record.price`) currently used for dictionaries.

## Tradeoffs

- Querying the database makes the page reflect persisted products and removes duplicated product data from the view, but introduces database dependency for the page.
- Ordering by price makes the output deterministic and places Espresso before Americano and Cappuccino.
- Seeding through the shell is useful for local development but is not a deployment-safe fixture strategy; later work may add fixtures or an admin workflow.
- A table improves semantic structure but still needs a complete document, styling, and accessibility enhancements in a later UI-focused change.

## Verification strategy

All Python/Django commands must deactivate Conda and activate `digitalcaferoot/env` in the same shell invocation. Verify:

- `python manage.py check` passes.
- `python manage.py makemigrations --check` reports no pending schema changes.
- `python manage.py migrate` succeeds without new schema work.
- The shell seed returns Espresso at 100 and does not duplicate existing rows.
- A database queryset returns Espresso, Americano, and Cappuccino with their expected prices.
- The development server returns HTTP 200 and the response contains a table, both header labels, and all three products/prices.

## Recommendation

Implement the template and database-backed query as one feature snapshot, seed Espresso idempotently through the Django shell, run migration checks plus `migrate`, verify the live response, update the plan/wiki, and complete rendezvous.
