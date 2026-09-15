# Plan: Custom Login View and Template

## Objective

Add a custom `/accounts/login/` page that authenticates users, reports invalid credentials, redirects successful logins to the product list, and greets the authenticated user.

## Task board

- [ ] Commit this approved plan on `main`.
- [ ] Create and switch to a feature branch.
- [ ] Deactivate Conda and activate `digitalcaferoot/env` for every Python/Django command.
- [ ] Add the requested authentication imports and `login_view` to `core/views.py`.
- [ ] Preserve the existing `login_required` decorators on `index` and `product_detail`.
- [ ] Pass `request.user` through the index context.
- [ ] Create `core/templates/core/login_view.html` with CSRF-protected username/password form and message rendering.
- [ ] Add `accounts/login/` to `core/urls.py`.
- [ ] Add `Hi, {{ user.username }}!` to `core/templates/core/index.html`.
- [ ] Run `python manage.py check` and the test suite.
- [ ] Verify GET `/accounts/login/` returns HTTP 200 with the login form.
- [ ] Verify invalid credentials redirect back and expose `Invalid login.` through messages.
- [ ] Verify valid `cafeadmin` credentials redirect to `/` and show the authenticated greeting.
- [ ] Verify anonymous product requests redirect to the login page and authenticated product routes remain accessible.
- [ ] Review the diff and confirm no database schema, cache, or virtual-environment files changed.
- [ ] Update this plan with execution results and synchronize living documentation.
- [ ] Commit the implementation as `feat: add custom login flow`.
- [ ] Rendezvous:
  - [ ] Confirm the codebase is workable.
  - [ ] Merge the feature branch into `main`.
  - [ ] Push the completed snapshot to GitHub.

## Constraints

- Keep the view name `login_view`; do not name it `login`.
- Preserve the requested redirect-to-index behavior after successful authentication.
- Do not add logout behavior or change `LOGIN_URL` beyond adding the matching route.
- Do not add models, migrations, or unrelated UI behavior.
- Keep credentials out of source control and commit messages.

## Expected result

Users can log in at `/accounts/login/`; invalid attempts receive a message, valid `cafeadmin` credentials redirect to `/`, and the protected product pages display the logged-in username.
