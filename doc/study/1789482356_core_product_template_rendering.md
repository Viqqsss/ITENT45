# Study: Core Product Template Rendering

## Objective

Replace the root route's plain-text response with a Django template that renders two in-memory Digital Cafe products, and register the `core` application so Django can discover its app-level templates.

## Requested changes

1. Add `core.apps.CoreConfig` to `INSTALLED_APPS` in `digitalcaferoot/digitalcafe/digitalcafe/settings.py`.
2. Create the namespaced template at `digitalcaferoot/digitalcafe/core/templates/core/index.html`.
3. Replace `core.views.index` with the requested loader-based template rendering and product context.

## Feasibility

The change is immediately feasible with the current Django 6.1.1 project:

- `core/apps.py` already defines `CoreConfig` from the generated application scaffold.
- The generated template backend has `APP_DIRS` enabled, so registering `core` in `INSTALLED_APPS` allows Django to discover `core/templates/core/index.html`.
- The current root URL already points to `core.views.index`; no URL changes are required.
- The product records are ordinary dictionaries and Django templates support dot-style dictionary-key lookup for `product_record.name` and `product_record.price`.

## Template namespacing

Using `core/templates/core/index.html` allows the loader name `core/index.html`. The repeated `core` directory is intentional: the outer directory is Django's app template location, while the inner directory namespaces the template and avoids filename collisions with templates from other applications.

## Rendering behavior

The view will pass this context shape:

```python
{
    "product_data": [
        {"name": "Americano", "price": 110},
        {"name": "Cappuccino", "price": 140},
    ]
}
```

The template condition suppresses the list when `product_data` is empty or missing. With the requested data, the response will contain an unordered list with both product names and PHP prices.

## Tradeoffs

### Explicit template loader

- Matches the requested implementation and makes the load/render steps visible.
- Is more verbose than Django's `render(request, "core/index.html", context)` shortcut.
- Returns the rendered content through an explicit `HttpResponse`, which is appropriate for this introductory implementation.

### In-memory product data

- Requires no model or database migration and keeps this feature small.
- Resets on every request and cannot be managed through Django admin.
- Serves as a temporary presentation example; persistent products should later use a model and database query.

### Application registration

- Enables app-template discovery and prepares `core` for models, management hooks, and other Django app features.
- Loads the app at Django startup, which is standard and has negligible overhead here.

### Minimal HTML fragment

- Exactly matches the requested template and is sufficient to verify Django template rendering.
- Does not yet provide a complete HTML document, styling, accessibility landmarks, or an empty-state message.

## Verification strategy

All Python and Django commands must run after Conda is deactivated and `digitalcaferoot/env` is activated. The implementation should then be verified with:

- `python manage.py check`
- `python manage.py test`
- Django's test client confirming `GET /` returns HTTP 200
- Response-content assertions for `Americano`, `PHP 110`, `Cappuccino`, and `PHP 140`
- Template-discovery confirmation for `core/index.html`

No migrations are required because this change introduces no models.

## Recommendation

Implement the three requested file changes as one feature commit, preserve the existing root URL route, verify rendered response content through Django's test client, and document the template structure during rendezvous.
