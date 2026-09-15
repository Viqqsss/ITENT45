# Plan: Custom Login View and Template

## Objective

Add a custom `/accounts/login/` page that authenticates users, reports invalid credentials, redirects successful logins to the product list, and greets the authenticated user.

## Task board

- [x] Commit this approved plan on `main`.
- [x] Create and switch to a feature branch.
- [x] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [x] Add the requested authentication imports and `login_view` to `core/views.py`.
- [x] Preserve the existing `login_required` decorators on `index` and `product_detail`.
- [x] Pass `request.user` through the index context.
- [x] Create `core/templates/core/login_view.html` with CSRF-protected username/password form and message rendering.
- [x] Add `accounts/login/` to `core/urls.py`.
- [x] Add `Hi, {{ user.username }}!` to `core/templates/core/index.html`.
- [x] Run `python manage.py check` and the test suite.
- [x] Verify GET `/accounts/login/` returns HTTP 200 with the login form.
- [x] Verify invalid credentials redirect back and expose `Invalid login.` through messages.
- [x] Verify valid `cafeadmin` credentials redirect to `/` and show the authenticated greeting.
- [x] Verify anonymous product requests redirect to the login page and authenticated product routes remain accessible.
- [x] Review the diff and confirm no database schema, cache, or virtual-environment files changed.
- [x] Update this plan with execution results and synchronize living documentation.
- [x] Commit the implementation as `feat: add custom login flow`.
- [x] Rendezvous:
  - [x] Confirm the codebase is workable.
  - [x] Merge the feature branch into `main`.
  - [x] Push the completed snapshot to GitHub.

## Constraints

- Keep the view name `login_view`; do not name it `login`.
- Preserve the requested redirect-to-index behavior after successful authentication.
- Do not add logout behavior or change `LOGIN_URL` beyond adding the matching route.
- Do not add models, migrations, or unrelated UI behavior.
- Keep credentials out of source control and commit messages.

## Expected result

Users can log in at `/accounts/login/`; invalid attempts receive a message, valid `cafeadmin` credentials redirect to `/`, and the protected product pages display the logged-in username.

## Execution results

- Executed on branch `feat/custom-login-flow` with Conda inactive and `digitalcaferoot/env` active.
- Added `login_view`, authentication imports, the login route, and the CSRF-protected login template.
- Added the authenticated-user greeting to the product list context/template.
- Django system check passed and the test suite completed with no discovered tests.
- Login GET returned HTTP 200; invalid credentials displayed `Invalid login.`; valid credentials redirected to `/` and displayed `Hi, cafeadmin!`.
- Anonymous product access redirected to login, while authenticated list/detail routes returned HTTP 200.
