# Study: Django Project Initialization

## Objective

Initialize the Digital Cafe Django project within the existing `digitalcaferoot` project root while preserving the established virtual-environment and documentation workflows.

## Current state

- Repository root: `/Users/jfviquiera/Desktop/ITENT45`
- Django project root: `digitalcaferoot/`
- Virtual environment: `digitalcaferoot/env/`
- Pinned framework version: Django 6.1.1
- The virtual environment is excluded from Git.
- No Django project scaffold has been generated yet.

## Naming

Django project package names must be valid Python identifiers, so the human-facing name “Digital Cafe” should be represented as `digitalcafe` in code. The existing outer directory remains `digitalcaferoot`.

Recommended structure:

```text
digitalcaferoot/
├── env/
├── manage.py
├── requirements.txt
└── digitalcafe/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Recommended initialization

From `digitalcaferoot/`, deactivate Conda, activate `env`, and initialize the Django configuration package into the current directory:

```bash
source /opt/anaconda3/etc/profile.d/conda.sh
conda deactivate
source env/bin/activate
python -m django startproject digitalcafe .
```

Using the trailing `.` places `manage.py` directly in `digitalcaferoot/` and avoids an unnecessary second project-root directory.

## Feasibility

The setup is immediately feasible. Django is installed in the project virtual environment, `digitalcafe` is a valid Python package name, and the target directory does not currently contain conflicting Django scaffold files.

## Tradeoffs

### Project package in the current root

- Keeps `manage.py` and `requirements.txt` together at the operational project root.
- Produces a conventional Django layout with minimal nesting.
- Requires running management commands from `digitalcaferoot/` unless paths are supplied explicitly.

### Nested project root

Running `django-admin startproject digitalcafe` without the trailing `.` would create another outer `digitalcafe/` directory. This separates the scaffold from environment files but adds nesting and makes the existing `digitalcaferoot` directory less useful as the application root.

### Generated secret key

Django generates a development `SECRET_KEY` in `settings.py`. Committing it is acceptable only for local development. Before production deployment, configuration secrets should move to environment variables and production settings should disable debug mode.

### Initial database

Project creation does not require running migrations. Deferring migrations keeps this change limited to the scaffold; database initialization can be planned as a separate Conventional Commit.

## Verification strategy

After scaffolding, verify from the activated environment:

```bash
python manage.py check
```

The command should report no system-check issues. The generated files should then be reviewed, committed as one `feat:` change, and pushed to the repository.

## Recommendation

Initialize `digitalcafe` into the existing `digitalcaferoot/` directory using `python -m django startproject digitalcafe .`, verify it with `python manage.py check`, and do not run migrations or create an application in the same implementation commit.
