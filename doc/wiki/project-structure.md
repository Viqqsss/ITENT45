# Project Structure

## Django layout

The Digital Cafe Django project uses a nested project layout:

```text
ITENT45/
├── AGENTS.md
├── doc/
│   ├── plan/
│   ├── study/
│   └── wiki/
└── digitalcaferoot/
    ├── env/                    # Local virtual environment; not tracked
    ├── requirements.txt
    └── digitalcafe/
        ├── manage.py
        ├── core/
        │   ├── migrations/
        │   │   ├── 0001_initial.py
        │   │   ├── 0002_cartitem.py
        │   │   └── 0003_transaction_lineitem.py
        │   ├── models.py
        │   ├── templates/
        │   │   └── core/
        │   │       ├── index.html
        │   │       ├── checkout.html
        │   │       ├── login_view.html
        │   │       └── product_detail.html
        │   ├── urls.py
        │   └── views.py
        └── digitalcafe/
            ├── settings.py
            ├── urls.py
            ├── asgi.py
            └── wsgi.py
```

The outer `digitalcaferoot/` contains the Python environment and dependency record. The inner `digitalcaferoot/digitalcafe/` directory is the Django operational root containing `manage.py`.

## Current routing

- `/` is routed from `digitalcafe.urls` to `core.urls`.
- `core.views.index` loads `core/index.html` and supplies database-backed `Product` records.
- The root page displays a two-column `Name`/`Price` table with each product name linked to `/product/<id>`, requires authentication, and greets the logged-in user.
- The product detail page includes an authenticated quantity form that creates a `CartItem` and reports success on the product list.
- `core.models.Product` persists product names and whole-PHP prices in the local database.
- `core.models.CartItem` stores a user's product and quantity as a cart line item.
- `core.models.Transaction` and `core.models.LineItem` persist completed checkout records.
- `/admin/` retains Django's generated administration route.
- `core.admin` registers `Product` with the default Django admin site.
- `core.admin` also registers `CartItem` for admin management.
- `/product/<integer>` routes to `core.views.product_detail`, requires authentication, and renders the matching product name, price, and a link back to `/`.
- `/accounts/login/` renders the custom login form, reports invalid credentials, and redirects successful logins to `/`.
- `/checkout` displays the authenticated user's cart and converts it into a transaction and line items on POST.

## Installed applications

`core.apps.CoreConfig` is registered in `INSTALLED_APPS`, enabling Django's app-level template discovery for `core/templates/core/index.html`.

## Database workflow

After activating the project environment, create and apply model migrations from `digitalcaferoot/digitalcafe/`:

```bash
python manage.py makemigrations core
python manage.py migrate
```

The local `db.sqlite3` database is development state and is excluded from Git. The current `Product` model stores `name` as a maximum-50-character string and `price` as an integer.

## Admin access

Local development admin access is provisioned in the database, not in source control. The admin login is available at `/admin/`; credentials must be managed privately and changed before any shared or production deployment.

Anonymous requests to the product views redirect to `/accounts/login/` with a `next` parameter; the custom login route now handles that path.

## Running management commands

Prepare the required Python environment as documented in `doc/wiki/python-environment.md`, then run management commands from the Django operational root:

```bash
cd /Users/jfviquiera/Desktop/ITENT45/digitalcaferoot/digitalcafe
python manage.py check
python manage.py test
python manage.py runserver
```

The current application routes are `/` for the product table, `/product/<product_id>` for the dynamic integer detail demonstration, and `/admin/` for Django administration.

Initial database migrations have been applied locally; the SQLite database remains ignored.
