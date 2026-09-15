# Study: Product Detail Template Rendering

## Objective

Create a dedicated product-detail template, render the selected `Product` instance through it, and provide a link back to the main products page.

## Current state

- `core.views.product_detail` currently retrieves a `Product` and returns only its name as plain text.
- The route `/product/<int:product_id>` is already registered.
- App template discovery is enabled through `APP_DIRS` and `core.apps.CoreConfig`.
- The product list at `/` already links product names to the detail route.

## Requested changes

Create `core/templates/core/product_detail.html` with:

```html
<a href="/">Back to products</a>

{% if product %}
    <p>Product name: {{ product.name }}</p>
    <p>Product price: {{ product.price }}</p>
{% endif %}
```

Update `product_detail` to load that template, retrieve the selected model instance, pass it as `product`, and render the response:

```python
def product_detail(request, product_id):
    template = loader.get_template("core/product_detail.html")
    p = Product.objects.get(id=product_id)
    context = {
        "product": p
    }
    return HttpResponse(template.render(context, request))
```

The existing `loader` and `Product` imports already support this implementation.

## Feasibility

The change is immediately feasible and requires no migration. The model instance exposes `name` and `price` to the template through Django's dot notation, and the existing route supplies `product_id`.

## Tradeoffs and edge cases

- A dedicated template separates presentation from the view and makes the detail page extensible.
- The requested direct `Product.objects.get(...)` behavior remains; an unknown ID will still raise `Product.DoesNotExist` and produce a server error rather than a friendly 404.
- The requested anchor uses `/` directly, which is sufficient for the current root route but less portable than a named URL reversal.
- The template is intentionally a fragment without a full HTML document or styling.

## Verification strategy

With Conda deactivated and `digitalcaferoot/env` active:

- Run `python manage.py check` and the test suite.
- Confirm `core/product_detail.html` is discoverable.
- Request an existing `/product/<id>` and verify HTTP 200, product name, product price, and `Back to products`.
- Confirm `/` remains functional.
- Confirm no migration, database, cache, or virtual-environment files change.

## Recommendation

Add the namespaced detail template, convert the view to render it with the selected `Product`, verify the existing route and back link, update the plan/wiki, and complete rendezvous.
