# Plan: Product Model Migration and Query Verification

## Objective

Add the requested persistent `Product` model to `core`, import it in `core/views.py`, generate and apply migrations, then verify the database with an idempotent sample queryset and a development-server request.

## Task board

- [x] Commit this approved plan on `main`.
- [x] Create and switch to a feature branch.
- [x] In every Python/Django shell, deactivate Conda and activate `digitalcaferoot/env`.
- [x] Update `digitalcaferoot/digitalcafe/core/models.py` with:

  ```python
  from django.db import models


  class Product(models.Model):
      name = models.CharField(max_length=50)
      price = models.IntegerField()

      def __str__(self):
          return f"{self.name}"
  ```

- [x] Add `from .models import Product` to `digitalcaferoot/digitalcafe/core/views.py` while preserving the current template-rendering behavior.
- [x] Run `python manage.py makemigrations core`.
- [x] Run `python manage.py migrate`.
- [x] Verify the schema with `python manage.py check` and `python manage.py makemigrations --check`.
- [x] Execute an idempotent sample queryset using `get_or_create` for Americano (PHP 110) and Cappuccino (PHP 140), then query them ordered by price.
- [x] Start the development server with the required environment active, perform one sample request to `/`, record the HTTP result, and stop the server.
- [x] Review the diff and ensure `db.sqlite3`, caches, and `env/` remain untracked.
- [x] Update this plan with execution results and synchronize living documentation.
- [x] Commit the implementation as `feat: add Product model and migrations`.
- [x] Rendezvous:
  - [x] Confirm migrations and verification succeeded.
  - [x] Merge the feature branch into `main`.
  - [x] Push the completed snapshot to GitHub.

## Constraints

- Preserve the requested `CharField(max_length=50)`, `IntegerField`, and `__str__` behavior.
- Do not replace the existing template view with database-backed rendering in this change; only add the requested model import.
- Do not commit the local SQLite database.
- Do not add unrelated models, fields, or migrations.

## Expected result

The `Product` model is migrated successfully, the requested import is present in `core/views.py`, the sample queryset returns both products with their prices, and the development server responds successfully at `/`.

## Execution results

- Executed on branch `feat/product-model-migrations` with Conda inactive and `digitalcaferoot/env` active.
- Added `Product` with `name`, `price`, and the requested string representation.
- Added the requested `from .models import Product` import to `core/views.py`.
- Created and applied `core/migrations/0001_initial.py`.
- `python manage.py check` reported no issues.
- `python manage.py makemigrations --check` reported no pending changes.
- The idempotent sample queryset returned Americano at 110 and Cappuccino at 140.
- The development server returned HTTP 200 for `/` and rendered the expected product list.
- The temporary server was stopped after verification; local `db.sqlite3` remains ignored.
