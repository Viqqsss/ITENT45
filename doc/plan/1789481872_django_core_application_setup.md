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

- [ ] Create and switch to a feature branch for this plan.
- [ ] Prepare the Python environment in the implementation shell:
  - [ ] Source Conda's shell integration.
  - [ ] Deactivate Conda.
  - [ ] Activate `digitalcaferoot/env`.
  - [ ] Verify `CONDA_PREFIX`, `VIRTUAL_ENV`, the Python executable, and Django version.
- [ ] From `digitalcaferoot/`, scaffold the nested project with `python -m django startproject digitalcafe`.
- [ ] From `digitalcaferoot/digitalcafe/`, create the application with `python manage.py startapp core`.
- [ ] Update `core/views.py` with the requested response view:

  ```python
  from django.http import HttpResponse


  def index(request):
      return HttpResponse("Hello world!")
  ```

- [ ] Create `core/urls.py` with the requested root route:

  ```python
  from django.urls import path

  from . import views  # "." means the current package; import the sibling views.py module.

  urlpatterns = [
      path("", views.index, name="index"),
  ]
  ```

- [ ] Update `digitalcaferoot/digitalcafe/digitalcafe/urls.py`:
  - [ ] Import `include` alongside `path`.
  - [ ] Preserve the generated admin route.
  - [ ] Include `core.urls` at the site root.

  ```python
  from django.contrib import admin
  from django.urls import include, path

  urlpatterns = [
      path("admin/", admin.site.urls),
      path("", include("core.urls")),
  ]
  ```

- [ ] Verify the implementation from the activated environment:
  - [ ] Run `python manage.py check`.
  - [ ] Run the Django test suite.
  - [ ] Use Django's test client to confirm `GET /` returns HTTP 200 and `Hello world!`.
- [ ] Review the diff and confirm no virtual-environment or generated cache files are tracked.
- [ ] Update this task board with execution results.
- [ ] Commit the implementation as `feat: add core hello world route`.
- [ ] Rendezvous:
  - [ ] Confirm the codebase is workable.
  - [ ] Merge the feature branch into `main`.
  - [ ] Sync living documentation with the implemented project layout and commands.
  - [ ] Push the completed snapshot to GitHub.

## Constraints

- Every Python or Django command must deactivate Conda and activate `digitalcaferoot/env` in the same shell invocation.
- Do not run initial database migrations in this implementation; migration/database initialization remains a separate change.
- Do not add unrelated views, templates, models, static files, or applications.
- Preserve the exact response text `Hello world!`.

## Expected result

The Django system check and tests pass, and requesting `/` returns a successful plain-text `Hello world!` response through `core.urls`.
