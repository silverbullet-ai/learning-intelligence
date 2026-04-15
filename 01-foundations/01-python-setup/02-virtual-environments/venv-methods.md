# venv-methods


## venv

```bash
python -m venv myenv
myenv\Scripts\activate
```


## virtualenv

```bash
pip install virtualenv
virtualenv -p python3 venv1
venv1\Scripts\activate
```

## conda

```bash
conda create -p envs/python-core python=3.12
conda activate envs/python-core
```