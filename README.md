# Npdocify - Convert any docstring to any format docstring

Transform your python docstrings with the format you want :sparkles:

Support Nympydoc, Google and ReStructuredText as output styles.
The input style should be either Numpy, Google, ReST or even a mix of both.

[![Release](https://img.shields.io/github/v/tag/valentingol/npdocify?label=Pypi&logo=pypi&logoColor=yellow)](https://pypi.org/project/npdocify/)
![PythonVersion](https://img.shields.io/badge/Python-3.7%20%7E%203.11-informational)
[![License](https://img.shields.io/github/license/valentingol/npdocify?color=999)](https://stringfixer.com/fr/MIT_license)

[![Ruff_logo](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Black_logo](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Ruff](https://github.com/valentingol/npdocify/actions/workflows/ruff.yaml/badge.svg)](https://github.com/valentingol/npdocify/actions/workflows/ruff.yaml)
[![Flake8](https://github.com/valentingol/npdocify/actions/workflows/flake.yaml/badge.svg)](https://github.com/valentingol/npdocify/actions/workflows/flake.yaml)
[![Pydocstyle](https://github.com/valentingol/npdocify/actions/workflows/pydocstyle.yaml/badge.svg)](https://github.com/valentingol/npdocify/actions/workflows/pydocstyle.yaml)
[![MyPy](https://github.com/valentingol/npdocify/actions/workflows/mypy.yaml/badge.svg)](https://github.com/valentingol/npdocify/actions/workflows/mypy.yaml)
[![PyLint](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/valentingol/5816178f37cee2c013f2e656666c898a/raw/npdocify_pylint.json)](https://github.com/valentingol/npdocify/actions/workflows/pylint.yaml)

[![Tests](https://github.com/valentingol/npdocify/actions/workflows/tests.yaml/badge.svg)](https://github.com/valentingol/npdocify/actions/workflows/tests.yaml)
[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/valentingol/6fd638b90ac10eced712b8d5ca83b04f/raw/npdocify_tests.json)](https://github.com/valentingol/npdocify/actions/workflows/tests.yaml)

## How to use

Install the library via pip:

```bash
pip install git+https://github.com/valentingol/npdocify
```

Use it like that to write the files in place:

```bash
npdocify <dir/file path> -s=<style> --indent=<n_indent> --length=<len>
```

Available styles (`style`) are:

* "numpy": Numpy doc style
* "google": Google style
* "rest": ReST style

`n_indent` is the number of indentation spaces convention of you file (generally 4 or 2). By default 4.

`len` is the maximum length of your output files. By default 88.
