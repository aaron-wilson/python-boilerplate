# python-boilerplate

### Usage

```
mypkg -c configs/default.yml
mypkg -h
```

### Install

```
conda env create -f environment.yml
source activate mypkg
pip install .
```

### Notes

- Without `pip install .`, you will see a `ModuleNotFoundError` for `from mypkg.some_class import SomeClass`. This is because the interpreter is looking for that module in `/site-packages/`, whether running the console script or `python mypkg/cli.py`.
- If import in `mypkg/cli.py` was `from some_class import SomeClass`, the module would be found without `pip install .`
