# Plan: Core Product Template Rendering

## Objective

Register the `core` Django application and replace the root route's plain-text response with the requested template-rendered list of Digital Cafe products.

## Task board

- [ ] Commit this approved implementation plan on `main`.
- [ ] Create and switch to a feature branch.
- [ ] Prepare the required Python environment:
  - [ ] Source Conda shell integration.
  - [ ] Deactivate Conda.
  - [ ] Activate `digitalcaferoot/env`.
  - [ ] Verify the active Python and Django installation.
- [ ] Add `core.apps.CoreConfig` to `INSTALLED_APPS` in `digitalcaferoot/digitalcafe/digitalcafe/settings.py`.
- [ ] Create `digitalcaferoot/digitalcafe/core/templates/core/index.html` with the approved product-list template.
- [ ] Replace `core/views.py` with the approved loader-based view and two in-memory products.
- [ ] Verify the change:
  - [ ] Run `python manage.py check`.
  - [ ] Run `python manage.py test`.
  - [ ] Confirm Django can load `core/index.html`.
  - [ ] Confirm `GET /` returns HTTP 200.
  - [ ] Confirm the response contains `Americano`, `PHP 110`, `Cappuccino`, and `PHP 140`.
- [ ] Review the diff and confirm no environment, cache, or database files are tracked.
- [ ] Update this task board with execution results.
- [ ] Commit the implementation as `feat: render core product template`.
- [ ] Rendezvous:
  - [ ] Confirm the codebase is workable.
  - [ ] Merge the feature branch into `main`.
  - [ ] Sync living documentation with the template-rendering behavior.
  - [ ] Push the completed snapshot to GitHub.

## Constraints

- Use the exact two requested product records.
- Preserve the existing root URL and admin URL configuration.
- Do not introduce models or run migrations.
- Do not add unrelated templates, styling, or application behavior.
- Run every Python and Django command with Conda inactive and `digitalcaferoot/env` active.

## Expected result

The root route renders `core/index.html` and displays Americano at PHP 110 and Cappuccino at PHP 140 in an unordered list.
