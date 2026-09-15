# Study: Dynamic Product Detail Routing

## Objective

Keep the existing product-list page at `/` and add a dynamic product-detail route at `/product/<product_id>` that returns the captured integer identifier as plain text.

## Requested implementation

Add this view to `core/views.py`:

```python
def product_detail(request, product_id):
    return HttpResponse(str(product_id))
```

Register it in `core/urls.py` alongside the existing index route:

```python
urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:product_id>", views.product_detail, name="product_detail"),
]
```

The `<int:product_id>` converter restricts matching URLs to integer identifiers and passes the converted value to the view as `product_id`.

## Feasibility

The change is immediately feasible. The root URL already includes `core.urls`, and the existing index route remains unchanged. Adding a second route and view requires no model, migration, or database change.

## URL behavior

- `/` continues to render the database-backed product table.
- `/product/1` returns `1` with HTTP 200.
- `/product/42` returns `42` with HTTP 200.
- Non-integer identifiers such as `/product/abc` do not match this route and should return HTTP 404.
- The requested route pattern has no trailing slash; verification will use that exact form.

## Tradeoffs

- Returning the ID as plain text is a minimal routing demonstration and does not yet fetch or display the corresponding `Product` record.
- The route accepts any integer, including IDs that do not exist in the database; later work can use `get_object_or_404(Product, pk=product_id)` when a real detail page is desired.
- Keeping the route in `core.urls` preserves application-level URL ownership and the existing project URL structure.

## Verification strategy

With Conda deactivated and `digitalcaferoot/env` active:

- Run `python manage.py check` and the test suite.
- Use Django's test client to confirm `/` remains HTTP 200.
- Confirm `/product/123` returns HTTP 200 with body `123`.
- Confirm a non-integer path returns HTTP 404.
- Optionally verify the same dynamic route through the temporary development server.
- Ensure no database, cache, or virtual-environment files are changed.

## Recommendation

Add only the requested view and route, preserve the existing list page, verify integer conversion and non-integer rejection, update the plan/wiki, and complete rendezvous as one feature snapshot.
