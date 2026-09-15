# Study: Custom Login View and Template

## Objective

Add a project login page at `/accounts/login/`, authenticate submitted credentials with Django, display invalid-login messages, redirect successful logins to the product list, and greet the authenticated user on the index page.

## Current state

- `index` and `product_detail` are protected with `login_required`.
- Those decorators currently redirect anonymous users to `/accounts/login/`.
- `core.urls` currently contains product routes but no login route.
- Django authentication middleware and messages middleware are enabled.
- The local `cafeadmin` account is available for verification.

## Requested implementation

### View and imports

Add a function named `login_view` (not `login`) to avoid colliding with Django's imported `login` function. The view will use:

- `redirect` from `django.shortcuts`
- `login`, `logout`, and `authenticate` from `django.contrib.auth`
- `messages` from `django.contrib`
- Existing `loader` and `HttpResponse` imports

GET requests render `core/login_view.html`. POST requests authenticate the submitted username and password, add an `Invalid login.` message and redirect back on failure, or log the user in and redirect to the named `index` route on success.

The supplied `logout` import is not used by this view yet, but can be included to match the requested authentication import group for future logout behavior.

### URL route

Add this route to `core/urls.py`:

```python
path("accounts/login/", views.login_view, name="login_view"),
```

Because the project URL configuration already includes `core.urls` at the root, this resolves to `/accounts/login/`, matching Django's default `LOGIN_URL`.

### Login template

Create `core/templates/core/login_view.html` with a username/password form, CSRF token, and message list. The message class condition should use `message.tags` for the current message; this corrects the supplied `messages.tags` typo while preserving the requested intent.

### Authenticated greeting

Pass `request.user` in the index context and add `Hi, {{ user.username }}!` to `core/index.html`. The existing `login_required` decorator guarantees that `request.user` is authenticated when the page renders.

## Feasibility

The change fits the current project without database schema changes. Django's session and messages infrastructure is already configured and migrated, and the existing login-protected routes will now have a matching login endpoint.

## Tradeoffs and edge cases

- Credentials are handled by Django's authentication backend; plaintext passwords are not stored.
- The form's `action="#"` posts to the current login path, which is sufficient for this page.
- The view redirects invalid submissions back to the current path and displays a message through Django's messages framework.
- The requested code does not preserve a `next` URL from the decorator redirect; successful login always redirects to the named `index` route. A later improvement could honor `next`.
- `logout` is imported but unused until a logout route is added.
- The login page itself remains publicly accessible, while the product pages stay protected.

## Verification strategy

With Conda deactivated and `digitalcaferoot/env` active:

- Run `python manage.py check` and the test suite.
- Confirm GET `/accounts/login/` returns HTTP 200 and contains the form.
- POST invalid credentials and confirm redirect plus `Invalid login.` message.
- POST valid `cafeadmin` credentials and confirm redirect to `/` plus authenticated greeting.
- Confirm anonymous `/` redirects to the login page and authenticated product routes remain accessible.
- Confirm no database schema, cache, or virtual-environment files change.

## Recommendation

Implement the custom login view, template, route, and authenticated greeting as one feature snapshot, verify both authentication paths, update the plan/wiki, and complete rendezvous.
