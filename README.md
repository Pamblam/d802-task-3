# Setup

Create and activate the venv

```
python -m venv d803-env
source d803-env/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=d803-env --display-name "Python (D803 Env)"
```

# Note to self

don't forget to save your environment after adding new stuff to it.

```
pip freeze > requirements.txt
```