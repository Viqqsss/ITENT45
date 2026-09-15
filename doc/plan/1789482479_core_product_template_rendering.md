# Plan: Core Product Template Rendering

## Objective

Register the `core` Django application and replace the root route's plain-text response with the requested template-rendered list of Digital Cafe products.

## Task board

- [x] Commit this approved implementation plan on `main`.
- [x] Create and switch to a feature branch.
- [x] Prepare the required Python environment:
  - [x] Source Conda shell integration.
  - [x] Deactivate Conda.
  - [x] Activate `digitalcaferoot/env`.
  - [x] Verify the active Python and Django installation.
- [x] Add `core.apps.CoreConfig` to `INSTALLED_APPS` in `digitalcaferoot/digitalcafe/digitalcafe/settings.py`.
- [x] Create `digitalcaferoot/digitalcafe/core/templates/core/index.html` with the approved product-list template.
- [x] Replace `core/views.py` with the approved loader-based view and two in-memory products.
- [x] Verify the change:
  - [x] Run `python manage.py check`.
  - [x] Run `python manage.py test`.
  - [x] Confirm Django can load `core/index.html`.
  - [x] Confirm `GET /` returns HTTP 200.
  - [x] Confirm the response contains `Americano`, `PHP 110`, `Cappuccino`, and `PHP 140`.
- [x] Review the diff and confirm no environment, cache, or database files are tracked.
- [x] Update this task board with execution results.
- [x] Commit the implementation as `feat: render core product template`.
- [x] Rendezvous:
  - [x] Confirm the codebase is workable.
  - [x] Merge the feature branch into `main`.
  - [x] Sync living documentation with the template-rendering behavior.
  - [x] Push the completed snapshot to GitHub.

## Constraints

- Use the exact two requested product records.
- Preserve the existing root URL and admin URL configuration.
- Do not introduce models or run migrations.
- Do not add unrelated templates, styling, or application behavior.
- Run every Python and Django command with Conda inactive and `digitalcaferoot/env` active.

## Expected result

The root route renders `core/index.html` and displays Americano at PHP 110 and Cappuccino at PHP 140 in an unordered list.

## Execution results

- Executed on branch `feat/core-product-template` with Conda inactive and `digitalcaferoot/env` active.
- Registered `core.apps.CoreConfig` in `INSTALLED_APPS`.
- Added the namespaced `core/index.html` template and loader-based view.
- `python manage.py check` reported no issues.
- `python manage.py test` completed successfully with no discovered tests.
- Django resolved the template from the `core` application.
- Django's test client confirmed HTTP 200 and all four expected product/price strings.
- No models were added and no migrations were run.
- Living project documentation was synchronized.
