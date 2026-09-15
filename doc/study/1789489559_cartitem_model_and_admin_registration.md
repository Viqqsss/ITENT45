# Study: CartItem Model and Admin Registration

## Objective

Add a `CartItem` model representing a user's product and quantity, create its database migration, and register it with Django admin so staff can manage cart line items.

## Requested model

The model belongs in `core/models.py` and should use Django's built-in `User` model:

```python
from django.contrib.auth.models import User


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product} (User: {self.user.username})"
```

Each row is one line item. The current assumption is that a user has one conceptual cart composed of many `CartItem` rows; no separate `Cart` model is introduced.

## Admin registration

Update `core/admin.py` to import `CartItem` and register it alongside `Product`:

```python
from .models import CartItem

admin.site.register(CartItem)
```

The default `ModelAdmin` will expose user, product, and quantity fields for CRUD management.

## Feasibility

The project already has migrated auth and product tables, and `core` is installed. Django can create foreign-key constraints to `auth.User` and `core.Product` in a new `core` migration. Admin is already enabled and available to the local superuser.

## Migration strategy

After activating the project environment:

```bash
python manage.py makemigrations core
python manage.py migrate
```

This is a schema change and should produce a new migration file. The local SQLite database is updated for development but remains ignored by Git.

## Tradeoffs and edge cases

- `on_delete=models.CASCADE` removes cart items when their user or product is deleted, matching the requested ownership semantics.
- `quantity` is an unconstrained integer as requested; negative or zero quantities are not prevented at the model layer yet.
- No uniqueness constraint prevents duplicate rows for the same user/product pair. A later refinement could add a database constraint or merge quantities in application logic.
- The one-cart-per-user assumption is represented by the `user` foreign key without a separate cart entity.
- The string representation is useful in admin but depends on both related objects remaining available.

## Verification strategy

- Run `python manage.py check`.
- Run `python manage.py makemigrations --check` after creating the migration.
- Run `python manage.py migrate`.
- Confirm `CartItem` appears in the admin site's registry.
- Create a sample CartItem through Django shell and verify its string representation without committing database state.
- Request `/admin/` as needed and confirm the admin site remains available.
- Confirm no plaintext credentials, cache files, or virtual-environment files are tracked.

## Recommendation

Implement the requested model and admin registration, generate/apply the migration, verify the model registry and string representation, update the plan/wiki, and complete rendezvous.
