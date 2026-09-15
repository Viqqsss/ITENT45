# Python Environment

## Required environment

The Digital Cafe project uses the virtual environment at `digitalcaferoot/env`. The host shell may automatically activate the Anaconda base environment, so Python commands must not be run until Conda is deactivated and the project environment is activated.

Run this preparation in every new shell before using Python, pip, Django, migrations, management commands, or tests:

```bash
source /opt/anaconda3/etc/profile.d/conda.sh
conda deactivate
source /Users/jfviquiera/Desktop/ITENT45/digitalcaferoot/env/bin/activate
```

Shell activation does not persist between Codex command executions or newly opened terminals. Repeat the preparation in each shell that performs project-related Python work.

## Verification

Verify the active environment before environment-sensitive operations:

```bash
printf 'CONDA_PREFIX=%s\n' "${CONDA_PREFIX:-}"
printf 'VIRTUAL_ENV=%s\n' "$VIRTUAL_ENV"
command -v python
python -m django --version
```

The expected state is:

- `CONDA_PREFIX` is empty.
- `VIRTUAL_ENV` is `/Users/jfviquiera/Desktop/ITENT45/digitalcaferoot/env`.
- `python` resolves inside `digitalcaferoot/env/bin/`.
- Django imports successfully from the virtual environment.

## Dependency policy

- Install project packages only after activating `digitalcaferoot/env`.
- Record reproducible dependencies in `digitalcaferoot/requirements.txt`.
- Keep the `env/` directory local and excluded from Git.
- Do not install project dependencies into Conda or another global Python environment.
