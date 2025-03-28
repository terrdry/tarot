# Tarot Project Outline

Tarot-root

- backend

   - .venv (virtualenv for this project)
   - config (Configuration for development)
   - instance (where .db are being stored; either tarot.db or test.db)
   - routes (subdirectory should contain mapping files)
   - requirements.txt(python module installation for virtualenv)
   - app.py (main instigator)
   - models.py (database table definitions ORM style)
   - extensions.py (export db from there )
   - tests (Unit tests live there)

- frontend

   - Under construction

## to create the virtual environment

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Prompt: `(.venv)`

```sh
source .venv/bin/activate
cd backend
pip3 install -r requirements.txt
```

## To create the documentation

This will be created in the `tarot/backend/docs`

```sh
source .venv/bin/activate
cd backend
pdoc ./*.py routes tests -o ./docs 
```

## To run the flask code

```sh {"language":"sh","promptEnv":"never"}
source .venv/bin/activate
cd backend
flask run  --debug 
```

## To test the flask code

```sh {"background":"false","language":"sh"}
source .venv/bin/activate
# cd backend
pytest -v -o log_file=test-tarot.log
```

### Pytest Coverage

```sh
source .venv/bin/activate
pytest --cov . --cov-config backend/.coveragerc.ini -cov-report=html 
```

### pyTest Continuous

```sh
source .venv/bin/activate
# cd backend
pytest -v --cov-config backend/.coveragerc.ini -o log_file=test-tarot.log
ptw
```



