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
- `core.views.index` loads `core/index.html` and supplies two in-memory product records.
- The root page displays Americano at PHP 110 and Cappuccino at PHP 140.
- `/admin/` retains Django's generated administration route.

## Installed applications

`core.apps.CoreConfig` is registered in `INSTALLED_APPS`, enabling Django's app-level template discovery for `core/templates/core/index.html`.

## Running management commands

Prepare the required Python environment as documented in `doc/wiki/python-environment.md`, then run management commands from the Django operational root:

```bash
cd /Users/jfviquiera/Desktop/ITENT45/digitalcaferoot/digitalcafe
python manage.py check
python manage.py test
python manage.py runserver
```

Initial database migrations have not yet been run.
