# Plan: CartItem Model and Admin Registration

## Objective

Add the `CartItem` line-item model, migrate its user/product/quantity schema, and register it with Django admin.

## Task board

- [x] Commit this approved plan on `main`.
- [x] Create and switch to a feature branch.
- [x] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [x] Import Django's `User` model in `core/models.py`.
- [x] Add `CartItem` with the requested user and product foreign keys, quantity integer, and string representation.
- [x] Import `CartItem` in `core/admin.py` and register it with `admin.site.register(CartItem)`.
- [x] Run `python manage.py check`.
- [x] Run `python manage.py makemigrations core` and inspect the generated migration.
- [x] Run `python manage.py migrate`.
- [x] Run `python manage.py makemigrations --check` to confirm no pending schema changes.
- [x] Verify `CartItem` is present in the admin registry.
- [x] Create a temporary sample CartItem through the Django shell and verify its string representation, without adding seed data to source control.
- [x] Confirm `/admin/` remains available to the local superuser.
- [x] Review the diff and confirm no database, cache, or virtual-environment files are tracked.
- [x] Update this plan with execution results and synchronize living documentation.
- [x] Commit the implementation as `feat: add CartItem model and admin registration`.
- [x] Rendezvous:
  - [x] Confirm the codebase is workable.
  - [x] Merge the feature branch into `main`.
  - [x] Push the completed snapshot to GitHub.

## Constraints

- Use `on_delete=models.CASCADE` and `null=False` for both foreign keys.
- Keep `quantity` as an unconstrained `IntegerField` as requested.
- Do not add a separate Cart model, uniqueness constraint, validation, or cart UI.
- Do not commit the local SQLite database or sample credentials/data.

## Expected result

The new migration creates the `CartItem` table, the model is manageable through Django admin, and its string representation identifies quantity, product, and username.

## Execution results

- Executed on branch `feat/cartitem-model-admin` with Conda inactive and `digitalcaferoot/env` active.
- Added `CartItem` with cascading user/product foreign keys, quantity, and the requested string representation.
- Registered `CartItem` with the default admin site.
- Created and applied `core/migrations/0002_cartitem.py`.
- `makemigrations --check` reported no pending changes.
- Admin registry verification passed; a temporary CartItem rendered as `2 of Americano (User: cafeadmin)` and was removed.
- Authenticated `/admin/` returned HTTP 200.
