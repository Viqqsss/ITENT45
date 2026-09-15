# Study: Django Admin Product Registration

## Objective

Register the existing `Product` model with Django admin and create a local development superuser using the supplied credentials.

## Requested admin change

Update `digitalcaferoot/digitalcafe/core/admin.py` to import and register `Product`:

```python
from django.contrib import admin

from .models import Product

admin.site.register(Product)
```

The generated project already enables the Django admin application and routes `/admin/`, so no settings or URL changes are expected.

## Superuser strategy

Create the local superuser with:

- Username: `cafeadmin`
- Email: `cafeadmin@gmail.com`
- Password: supplied by the human

The account is stored in the local SQLite database, which is excluded from Git. Credentials will not be written to source files, documentation, shell history artifacts, or commit messages.

The command should be non-interactive and idempotent in implementation: first check whether `cafeadmin` exists, then create or update the local account as needed. The password should be set through Django's password-hashing API, never stored in plaintext.

## Feasibility

The `Product` model and migrations already exist, and the admin/auth applications are migrated. Registering the model will make Products manageable through `/admin/`; creating the superuser will permit access to that interface.

## Tradeoffs and security

- The requested password is suitable only for local development and should be changed before any shared or deployed environment.
- The admin registration uses Django's default `ModelAdmin`, which is sufficient for basic CRUD but does not yet customize columns, search, filtering, or validation.
- The local superuser is database state rather than repository state; a fresh clone will require separate environment-specific account provisioning.

## Verification strategy

With Conda deactivated and `digitalcaferoot/env` active:

- Run `python manage.py check`.
- Confirm `cafeadmin` exists, is staff, and is a superuser without printing the password.
- Confirm the admin registry contains `Product`.
- Start the development server and request `/admin/`, expecting an HTTP 200 login page.
- Stop the temporary server and ensure `db.sqlite3`, caches, and `env/` remain untracked.

## Recommendation

Implement the minimal admin registration, provision the local superuser without committing credentials, verify admin availability, update the plan and wiki, and complete rendezvous as one feature snapshot.
