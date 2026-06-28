# Setup

Create and activate the venv

```
python -m venv d803-env
source d803-env/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=d803-env --display-name "Python (D803 Env)"
```

# Download the Data

The notebook assumes the dataset is extracted to the project directory.

# Notes on Running

If you run every cell, the script will use Optuna to do some Bayesian hyperparameter tuning before actually doing any training. This took more than an hour on my 3090, YMMV.