# Plan: Django Core Application Setup

## Objective

Create the nested `digitalcafe` Django project requested by the human, add a `core` application, expose a plain-text `Hello world!` view at `/`, and connect the application URL configuration to the project URL configuration.

## Approved layout

The human specified the project URL file at `digitalcaferoot/digitalcafe/digitalcafe/urls.py`. Implementation will therefore use Django's nested project layout:

```text
digitalcaferoot/
├── env/
├── requirements.txt
└── digitalcafe/
    ├── manage.py
    ├── core/
    │   ├── views.py
    │   └── urls.py
    └── digitalcafe/
        └── urls.py
```

## Task board

- [x] Create and switch to a feature branch for this plan.
- [x] Prepare the Python environment in the implementation shell:
  - [x] Source Conda's shell integration.
  - [x] Deactivate Conda.
  - [x] Activate `digitalcaferoot/env`.
  - [x] Verify `CONDA_PREFIX`, `VIRTUAL_ENV`, the Python executable, and Django version.
- [x] From `digitalcaferoot/`, scaffold the nested project with `python -m django startproject digitalcafe`.
- [x] From `digitalcaferoot/digitalcafe/`, create the application with `python manage.py startapp core`.
- [x] Update `core/views.py` with the requested response view:

  ```python
  from django.http import HttpResponse


  def index(request):
      return HttpResponse("Hello world!")
  ```

- [x] Create `core/urls.py` with the requested root route:

  ```python
  from django.urls import path

  from . import views  # "." means the current package; import the sibling views.py module.

  urlpatterns = [
      path("", views.index, name="index"),
  ]
  ```

- [x] Update `digitalcaferoot/digitalcafe/digitalcafe/urls.py`:
  - [x] Import `include` alongside `path`.
  - [x] Preserve the generated admin route.
  - [x] Include `core.urls` at the site root.

  ```python
  from django.contrib import admin
  from django.urls import include, path

  urlpatterns = [
      path("admin/", admin.site.urls),
      path("", include("core.urls")),
  ]
  ```

- [x] Verify the implementation from the activated environment:
  - [x] Run `python manage.py check`.
  - [x] Run the Django test suite.
  - [x] Use Django's test client to confirm `GET /` returns HTTP 200 and `Hello world!`.
- [x] Review the diff and confirm no virtual-environment or generated cache files are tracked.
- [x] Update this task board with execution results.
- [x] Commit the implementation as `feat: add core hello world route`.
- [x] Rendezvous:
  - [x] Confirm the codebase is workable.
  - [x] Merge the feature branch into `main`.
  - [x] Sync living documentation with the implemented project layout and commands.
  - [x] Push the completed snapshot to GitHub.

## Constraints

- Every Python or Django command must deactivate Conda and activate `digitalcaferoot/env` in the same shell invocation.
- Do not run initial database migrations in this implementation; migration/database initialization remains a separate change.
- Do not add unrelated views, templates, models, static files, or applications.
- Preserve the exact response text `Hello world!`.

## Expected result

The Django system check and tests pass, and requesting `/` returns a successful plain-text `Hello world!` response through `core.urls`.

## Execution results

- Executed on branch `feat/django-core-hello-world` with Conda inactive and `digitalcaferoot/env` active.
- Django 6.1.1 generated the nested project and `core` application.
- `python manage.py check` reported no issues.
- `python manage.py test` completed successfully with no discovered tests.
- Django's test client confirmed `GET /` returned HTTP 200 with `Hello world!`.
- Initial database migrations were intentionally not run.
- Living project documentation was synchronized in `doc/wiki/project-structure.md`.
