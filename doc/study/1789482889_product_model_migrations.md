# Study: Product Model and Migrations

## Objective

Add a persistent `Product` model to the `core` application, generate and apply its migration, and verify the resulting database through a sample queryset and a running development server.

## Requested model

The intended model is:

```python
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
```

The supplied text has compressed whitespace and visually escaped underscores; implementation will use valid Python syntax for `__str__` and preserve the requested fields and behavior.

## Feasibility

The change is feasible with the current project:

- `core.apps.CoreConfig` is already registered in `INSTALLED_APPS`.
- The project uses Django 6.1.1 with the generated SQLite database configuration.
- `core/migrations/__init__.py` already exists, so `makemigrations core` can create the first model migration.
- Applying migrations will create the `core_product` table and the standard Django auth/admin/session tables that have not yet been initialized.

## Migration strategy

From `digitalcaferoot/digitalcafe/`, after deactivating Conda and activating `digitalcaferoot/env`:

```bash
python manage.py makemigrations core
python manage.py migrate
```

`makemigrations` records the model schema in source control. `migrate` applies all pending migrations to the local SQLite database. The generated `db.sqlite3` file is local development state and remains excluded by `.gitignore`.

## Sample queryset strategy

To make the result deterministic and demonstrate both creation and retrieval, the implementation can use Django's shell to create two sample products if they do not already exist, then query them in price order:

```python
Product.objects.get_or_create(name="Americano", defaults={"price": 110})
Product.objects.get_or_create(name="Cappuccino", defaults={"price": 140})
list(Product.objects.order_by("price").values("name", "price"))
```

The returned result should be:

```python
[
    {"name": "Americano", "price": 110},
    {"name": "Cappuccino", "price": 140},
]
```

Using `get_or_create` makes repeat verification safe and avoids duplicate sample rows.

## Server verification

The development server should be started with the required environment active, bound to localhost, and queried at `/`. The current view renders the in-memory product list, so the server check verifies that migrations did not break the application while the shell queryset verifies the new database model. The server process should be stopped after the sample request.

## Tradeoffs and risks

- An integer price stores whole PHP units and matches the requested `IntegerField`; a production commerce system may need `DecimalField` for fractional prices and currency rules.
- The model is not yet wired into `views.py`; that is intentionally outside this requested model/migration change.
- Applying migrations changes local database state but does not require committing `db.sqlite3`.
- Sample data improves verification but is development data, not a fixture or production seed.
- Running the development server is appropriate for local verification only.

## Verification requirements

- `python manage.py check` reports no issues.
- `python manage.py makemigrations --check` reports no model changes pending after the migration is created.
- `python manage.py migrate` completes successfully.
- The sample queryset returns both requested products and prices.
- A sample HTTP request to `/` returns HTTP 200.
- No `db.sqlite3`, cache files, or virtual-environment files are tracked.

## Recommendation

Implement the model exactly as specified, create and apply the migration, verify with idempotent sample queryset data, run the development server for one HTTP check, document the result, and complete rendezvous as one feature snapshot.
