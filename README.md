<!--
 MIT License
 Copyright (c) 2025 Terry Drymonacos
 -->

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

```

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
flask run
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

## VUE essentials

### Debugging

It is essential that we run two processes when we are debugging the Vue portion of the code. If you have `axios` calls active in your Vue environment, You will need to start the flask debugger "Python Debugger: Flask".

To debug in Vue

Starts npm with `Run npm start - tarot` which just starts Vue with `run dev` which in turn starts a fork of another process that is runnning as the debugger

- Run Script: dev
   Select from Run and Debug

```json
{
    "command": "npm run dev",
    "name": "Run npm dev - tarot",
    "request": "launch",
    "type": "node-terminal",
    "cwd": "${workspaceFolder}/frontend/src"
}
```

Start the chrome web server by running the `Launch Chrome Vue - tarot`

```json
{
    "name": "Launch Chrome Vue",
    "type": "chrome",
    "request": "launch",
    "url": "http://localhost:4000",
    "webRoot": "${workspaceFolder}/src",
    "sourceMapPathOverrides": {
        "webpack:///src/*": "${webRoot}/*",
        "webpack:///./src/*": "${webRoot}/*",
        "webpack:///*": "${webRoot}/*"
    }
}

Now you should be able to track errors in real time with the stack levels

> The name of the files that have been compiled for this debugging run will appear in the stack trace on the side. Use those files to set breakpoints in the debugger.
```

[Molecule](./docs/Vagrant-Molecule%20Integration.md)
