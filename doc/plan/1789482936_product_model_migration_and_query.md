# Plan: Product Model Migration and Query Verification

## Objective

Add the requested persistent `Product` model to `core`, import it in `core/views.py`, generate and apply migrations, then verify the database with an idempotent sample queryset and a development-server request.

## Task board

- [ ] Commit this approved plan on `main`.
- [ ] Create and switch to a feature branch.
- [ ] In every Python/Django shell, deactivate Conda and activate `digitalcaferoot/env`.
- [ ] Update `digitalcaferoot/digitalcafe/core/models.py` with:

  ```python
  from django.db import models


  class Product(models.Model):
      name = models.CharField(max_length=50)
      price = models.IntegerField()

      def __str__(self):
          return f"{self.name}"
  ```

- [ ] Add `from .models import Product` to `digitalcaferoot/digitalcafe/core/views.py` while preserving the current template-rendering behavior.
- [ ] Run `python manage.py makemigrations core`.
- [ ] Run `python manage.py migrate`.
- [ ] Verify the schema with `python manage.py check` and `python manage.py makemigrations --check`.
- [ ] Execute an idempotent sample queryset using `get_or_create` for Americano (PHP 110) and Cappuccino (PHP 140), then query them ordered by price.
- [ ] Start the development server with the required environment active, perform one sample request to `/`, record the HTTP result, and stop the server.
- [ ] Review the diff and ensure `db.sqlite3`, caches, and `env/` remain untracked.
- [ ] Update this plan with execution results and synchronize living documentation.
- [ ] Commit the implementation as `feat: add Product model and migrations`.
- [ ] Rendezvous:
  - [ ] Confirm migrations and verification succeeded.
  - [ ] Merge the feature branch into `main`.
  - [ ] Push the completed snapshot to GitHub.

## Constraints

- Preserve the requested `CharField(max_length=50)`, `IntegerField`, and `__str__` behavior.
- Do not replace the existing template view with database-backed rendering in this change; only add the requested model import.
- Do not commit the local SQLite database.
- Do not add unrelated models, fields, or migrations.

## Expected result

The `Product` model is migrated successfully, the requested import is present in `core/views.py`, the sample queryset returns both products with their prices, and the development server responds successfully at `/`.
