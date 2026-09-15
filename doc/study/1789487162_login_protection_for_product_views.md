# Study: Login Protection for Product Views

## Objective

Require authentication before users can access the existing product-list and product-detail views.

## Requested implementation

Import Django's decorator:

```python
from django.contrib.auth.decorators import login_required
```

Then decorate both views:

```python
@login_required
def index(request):
    ...


@login_required
def product_detail(request, product_id):
    ...
```

The decorator preserves the existing view logic for authenticated users and redirects anonymous users to Django's configured login URL.

## Current authentication state

- Django authentication middleware is already enabled in the generated project.
- The local `cafeadmin` superuser exists for development verification.
- No application login page has been added yet.
- Django's default `LOGIN_URL` is `/accounts/login/` unless overridden. The current URL configuration does not include an accounts login route, so anonymous requests will redirect there but following that redirect may return 404 until a login route/template is added.

## Feasibility

The change is small and requires no model or migration changes. Adding the import and decorators to `core/views.py` is sufficient to enforce authentication at both endpoints.

## Tradeoffs and edge cases

- `login_required` is the standard Django mechanism and preserves the original requested URL using the `next` query parameter.
- Anonymous clients receive HTTP 302 rather than the product content.
- Authenticated clients, including `cafeadmin`, continue to receive the existing list and detail responses.
- Protecting the views before adding a user-facing login route may temporarily make anonymous access redirect to an unavailable `/accounts/login/`; a later authentication UI change can add that route.
- No authorization distinction is introduced: any authenticated user can access both views.

## Verification strategy

With Conda deactivated and `digitalcaferoot/env` active:

- Run `python manage.py check` and the test suite.
- Use Django's test client without a session to confirm `/` and `/product/<id>` redirect with HTTP 302 and a `next` parameter.
- Log in as the local `cafeadmin` user through the test client and confirm both views return HTTP 200 with their existing content.
- Confirm no database schema, cache, or virtual-environment files change.

## Recommendation

Apply only the `login_required` import and decorators, verify anonymous redirects and authenticated access, document the current login URL limitation, and complete rendezvous.
