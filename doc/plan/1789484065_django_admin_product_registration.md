# Plan: Django Admin Product Registration

## Objective

Register `Product` with Django admin and create the requested local development superuser without committing credentials or database state.

## Task board

- [x] Commit this approved plan on `main`.
- [x] Create and switch to a feature branch.
- [x] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [x] Update `digitalcaferoot/digitalcafe/core/admin.py` to import `Product` and call `admin.site.register(Product)`.
- [x] Provision the local `cafeadmin` superuser with email `cafeadmin@gmail.com` and the user-supplied password, using Django's password hashing and without printing or storing the password in repository files.
- [x] Make the provisioning idempotent by updating the existing local account if it already exists.
- [x] Run `python manage.py check`.
- [x] Verify `cafeadmin` is active, staff, and a superuser without exposing credentials.
- [x] Verify `Product` is registered in the admin site registry.
- [x] Start the development server and request `/admin/`, confirm the login page responds successfully, then stop the server.
- [x] Review the diff and confirm the local database, caches, and virtual environment remain untracked.
- [x] Update this plan with execution results and synchronize living documentation.
- [x] Commit the implementation as `feat: register Product in Django admin`.
- [x] Rendezvous:
  - [x] Confirm the codebase is workable.
  - [x] Merge the feature branch into `main`.
  - [x] Push the completed snapshot to GitHub.

## Constraints

- Do not commit the SQLite database or any plaintext credential.
- Do not put the password in source files, documentation, or commit messages.
- Keep the admin registration minimal; custom admin columns and filters are outside this change.
- The supplied password is for local development only and should be changed before deployment.

## Expected result

`Product` is manageable through Django admin, the local `cafeadmin` account can authenticate, `/admin/` serves its login page, and the repository contains no credentials or database artifacts.

## Execution results

- Executed on branch `feat/django-admin-product` with Conda inactive and `digitalcaferoot/env` active.
- Registered `Product` with the default Django admin site.
- Created/updated the local `cafeadmin` account with hashed password storage; credentials were not written to repository files.
- Django system check passed and the admin registry contains `Product`.
- `/admin/` redirected to the login page as expected; the login form returned HTTP 200.
- The temporary server was stopped and local database/cache/environment files remain ignored.
