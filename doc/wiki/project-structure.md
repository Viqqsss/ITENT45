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
        │   │   └── 0001_initial.py
        │   ├── models.py
        │   ├── templates/
        │   │   └── core/
        │   │       └── index.html
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
- `core.views.index` loads `core/index.html` and supplies database-backed `Product` records ordered by price.
- The root page displays a two-column table with Espresso at PHP 100, Americano at PHP 110, and Cappuccino at PHP 140.
- `core.models.Product` persists product names and whole-PHP prices in the local database.
- `/admin/` retains Django's generated administration route.

## Installed applications

`core.apps.CoreConfig` is registered in `INSTALLED_APPS`, enabling Django's app-level template discovery for `core/templates/core/index.html`.

## Database workflow

After activating the project environment, create and apply model migrations from `digitalcaferoot/digitalcafe/`:

```bash
python manage.py makemigrations core
python manage.py migrate
```

The local `db.sqlite3` database is development state and is excluded from Git. The current `Product` model stores `name` as a maximum-50-character string and `price` as an integer.

## Running management commands

Prepare the required Python environment as documented in `doc/wiki/python-environment.md`, then run management commands from the Django operational root:

```bash
cd /Users/jfviquiera/Desktop/ITENT45/digitalcaferoot/digitalcafe
python manage.py check
python manage.py test
python manage.py runserver
```

Initial database migrations have not yet been run.
