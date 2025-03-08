#. Tarot Project Outline

Tarot-root

- backend
  - .venv (virtualenv for this project)
  - tarot (source code)
  - requirements.txt(python module installation for virtualenv)
  - tests (Unit tests live there)
- frontend

## to create the virtual environment

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Prompt: `(.venv)`

```sh
# source backend/venv/bin/activate
# In the tarot-root directory
cd backend
source .venv/bin/activate
pip3 install -r requirements.txt
```


## To run the flask code


## To test the flask code
```sh
cd \tarot-root\backend\tarot
python -m unittest tests/tests.py
```



