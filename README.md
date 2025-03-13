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

## To run the flask code

```sh {"promptEnv":"never"}
source .venv/bin/activate
cd backend
flask run --debug 
```

## to run continous unittests

```sh
source .venv/bin/activate
cd backend
ptw
```

```sh

```

## To test the flask code

```sh {"background":"false"}
source .venv/bin/activate
cd backend
pytest  -v 
```



