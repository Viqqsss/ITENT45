# Plan: Django Admin Product Registration

## Objective

Register `Product` with Django admin and create the requested local development superuser without committing credentials or database state.

## Task board

- [ ] Commit this approved plan on `main`.
- [ ] Create and switch to a feature branch.
- [ ] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [ ] Update `digitalcaferoot/digitalcafe/core/admin.py` to import `Product` and call `admin.site.register(Product)`.
- [ ] Provision the local `cafeadmin` superuser with email `cafeadmin@gmail.com` and the user-supplied password, using Django's password hashing and without printing or storing the password in repository files.
- [ ] Make the provisioning idempotent by updating the existing local account if it already exists.
- [ ] Run `python manage.py check`.
- [ ] Verify `cafeadmin` is active, staff, and a superuser without exposing credentials.
- [ ] Verify `Product` is registered in the admin site registry.
- [ ] Start the development server and request `/admin/`, confirm the login page responds successfully, then stop the server.
- [ ] Review the diff and confirm the local database, caches, and virtual environment remain untracked.
- [ ] Update this plan with execution results and synchronize living documentation.
- [ ] Commit the implementation as `feat: register Product in Django admin`.
- [ ] Rendezvous:
  - [ ] Confirm the codebase is workable.
  - [ ] Merge the feature branch into `main`.
  - [ ] Push the completed snapshot to GitHub.

## Constraints

- Do not commit the SQLite database or any plaintext credential.
- Do not put the password in source files, documentation, or commit messages.
- Keep the admin registration minimal; custom admin columns and filters are outside this change.
- The supplied password is for local development only and should be changed before deployment.

## Expected result

`Product` is manageable through Django admin, the local `cafeadmin` account can authenticate, `/admin/` serves its login page, and the repository contains no credentials or database artifacts.
