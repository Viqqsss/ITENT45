# Study: Database-Backed Product Detail Links

## Objective

Align the current Digital Cafe list/detail flow with the requested implementation: query all products in `index`, link each product by database ID, and have `product_detail` retrieve the matching `Product` and return its name.

## Current state

- `core.views.index` already reads products from the database, currently ordered by price.
- `core.views.product_detail` currently returns the captured numeric ID as plain text.
- `core.urls` already maps `product/<int:product_id>` to `product_detail`.
- The template already renders a table, but currently uses `Product Name`/`Product Price` headers, displays a PHP prefix, and does not link rows to detail pages.
- `Product` is persisted and seeded with Espresso, Americano, and Cappuccino.

## Requested alignment

### View import and index query

`from .models import Product` is already present and should remain. The index view should use the requested query:

```python
products = Product.objects.all()
```

This removes the explicit price ordering. The database's default ordering is unspecified, so the template should display the queryset as returned.

### Product detail view

The requested implementation is:

```python
def product_detail(request, product_id):
    p = Product.objects.get(id=product_id)
    return HttpResponse(str(p.name))
```

The existing URL converter supplies an integer `product_id`, and the view returns the matching product name. If no product exists for that ID, `Product.DoesNotExist` will propagate as a server error; using `get_object_or_404` would be safer but would diverge from the explicitly requested code and is outside this change.

### Linked table template

The template should use `product_record.id` to construct `/product/{{ product_record.id }}` links, with the exact requested headers `Name` and `Price`. The price cell should show the stored integer without a PHP prefix, matching the supplied template.

## Feasibility

The change is directly compatible with the current route structure and model. No migrations are needed because only queries, response content, and template markup change.

## Tradeoffs

- Linking by primary key demonstrates dynamic routing and makes each row navigable.
- Returning only the product name is a minimal detail response, not a complete detail page.
- `objects.all()` follows the request exactly but gives up deterministic price ordering.
- Exact `get(id=...)` behavior is simple but produces a 500 for unknown IDs; a later hardening change can return a 404.
- Removing the PHP prefix from the table makes the output match the supplied template but weakens explicit currency labeling.

## Verification strategy

With Conda deactivated and `digitalcaferoot/env` active:

- Run `python manage.py check` and the test suite.
- Confirm `/` returns HTTP 200 and contains `Name`, `Price`, and links for seeded product IDs.
- Confirm `/product/<existing-id>` returns that product's name.
- Confirm an unknown integer currently follows the requested `get` behavior; capture this as an edge case rather than changing it.
- Confirm no database, migration, cache, or virtual-environment files change.

## Recommendation

Apply the requested exact view and template changes, preserve the existing route, verify linked product names through the database, update the plan/wiki, and complete rendezvous.
