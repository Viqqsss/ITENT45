# Study: Transaction and Checkout Flow

## Objective

Add persistent `Transaction` and `LineItem` models, provide a checkout page showing the current user's cart, and convert cart items into transaction line items when the user submits checkout.

## Requested models

Add to `core/models.py`:

```python
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField()


class LineItem(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField()
```

The existing `User` and `Product` models are reused. Each transaction belongs to one user, and each line item belongs to one transaction and product.

## Checkout template and route

Create `core/templates/core/checkout.html` with:

- Checkout heading and link back to `/`
- Authenticated username greeting
- A table of the user's cart items and quantities
- A CSRF-protected POST checkout form when cart items exist
- A `No cart items.` message when the cart is empty

Register `path("checkout", views.checkout, name="checkout")` in `core/urls.py` and link to `/checkout` from the authenticated index page.

## Checkout behavior

The checkout view is protected by `login_required` and has two branches:

- GET: query `CartItem.objects.filter(user=request.user)`, pass the list and user context to the template.
- POST: query the user's cart items, create a UTC-aware `Transaction`, create one `LineItem` per cart item, delete each cart item, display a thank-you message, and redirect to `index`.

The requested implementation uses `datetime as dt` and `dt.datetime.now(tz=dt.timezone.utc)`. Django's timezone-aware configuration supports this value.

## Feasibility

The change fits the existing authenticated cart flow. `CartItem` already links users and products, messages and redirects are already imported in `core/views.py`, and the project has migrated auth/session infrastructure.

## Migration strategy

This introduces two new tables and requires:

```bash
python manage.py makemigrations core
python manage.py migrate
```

The generated migration and model changes are committed; local SQLite data remains ignored.

## Tradeoffs and edge cases

- Checkout creates a transaction even when the cart is empty if a client POSTs directly; the requested flow does not guard against this.
- Deleting cart items after each line-item save can leave a partial transaction if an unexpected error occurs. A later hardening change could wrap checkout in `transaction.atomic()`.
- No prices, totals, payment processing, or transaction status are modeled yet.
- `created_at` has no automatic default and is set explicitly at checkout.
- The requested direct cart-item iteration creates one line item per row and preserves duplicate product rows if they exist.

## Verification strategy

With Conda deactivated and `digitalcaferoot/env` active:

- Run `python manage.py check`, `makemigrations --check`, and the test suite.
- Verify authenticated GET `/checkout` renders cart rows and the checkout form; empty carts show `No cart items.`.
- Seed temporary cart items, POST checkout as `cafeadmin`, and verify a transaction and matching line items are created.
- Verify cart items are removed, the thank-you message appears after redirect, and `/checkout` then shows an empty cart.
- Verify anonymous checkout access remains protected.
- Clean up only temporary verification rows and confirm no credentials or database files are tracked.

## Recommendation

Implement the requested models, checkout template/view/route, and index link, run migrations, verify the complete checkout conversion flow, update the plan/wiki, and complete rendezvous.
