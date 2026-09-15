# Plan: CartItem Model and Admin Registration

## Objective

Add the `CartItem` line-item model, migrate its user/product/quantity schema, and register it with Django admin.

## Task board

- [ ] Commit this approved plan on `main`.
- [ ] Create and switch to a feature branch.
- [ ] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [ ] Import Django's `User` model in `core/models.py`.
- [ ] Add `CartItem` with the requested user and product foreign keys, quantity integer, and string representation.
- [ ] Import `CartItem` in `core/admin.py` and register it with `admin.site.register(CartItem)`.
- [ ] Run `python manage.py check`.
- [ ] Run `python manage.py makemigrations core` and inspect the generated migration.
- [ ] Run `python manage.py migrate`.
- [ ] Run `python manage.py makemigrations --check` to confirm no pending schema changes.
- [ ] Verify `CartItem` is present in the admin registry.
- [ ] Create a temporary sample CartItem through the Django shell and verify its string representation, without adding seed data to source control.
- [ ] Confirm `/admin/` remains available to the local superuser.
- [ ] Review the diff and confirm no database, cache, or virtual-environment files are tracked.
- [ ] Update this plan with execution results and synchronize living documentation.
- [ ] Commit the implementation as `feat: add CartItem model and admin registration`.
- [ ] Rendezvous:
  - [ ] Confirm the codebase is workable.
  - [ ] Merge the feature branch into `main`.
  - [ ] Push the completed snapshot to GitHub.

## Constraints

- Use `on_delete=models.CASCADE` and `null=False` for both foreign keys.
- Keep `quantity` as an unconstrained `IntegerField` as requested.
- Do not add a separate Cart model, uniqueness constraint, validation, or cart UI.
- Do not commit the local SQLite database or sample credentials/data.

## Expected result

The new migration creates the `CartItem` table, the model is manageable through Django admin, and its string representation identifies quantity, product, and username.
