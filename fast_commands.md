# Commands that i am currentlu using

## Some notes on ususla stuff

- In the pre-commit config file, we can remove hooks that are done by ruff. Some people use ruff while other combine pylint, flake8 and black.
- VSCode has a setting to follow the versions of the installed linters in virtual enviroment. Usefull so we can all use the same versions. Even better when all tools are in the pre-commit.yaml file.
- In the pre-commit file we can hook the `--config=./pyproject.toml` to use the config file in the root of the project. This is usefull since we can have all the configuration in one file.
- At the same time, the version of the tools can be specified in the pre-commit.yaml file hook from the github repo i am pulling the tool.
- It is important, if i experiment locally, to follow the versions of the `pre-commit.yaml` file and use same configurations.

## Python Packaging and installing my own package

The pip looks in the current directory a pyproject.toml file and installs the package in development mode.

- This allows you to make changes to your package and have them reflected immediately without needing to reinstall.
- I can import any module from my package in any python script or notebook and it will use the latest version of the code.
- File hierarchy is not affected how to import the modules since they are in the lib folder of the package. Sys can find them.
- When I make a package I use `absolute import statements` since `sys.path()` is used to find the modules.
- From where the package starts. From `package.subpackage.module` or `package.module` or `package.subpackage.subsubpackage.module` etc.. I do not use relative imports like `from .module import CONSTANT` or `from ..subpackage.module import CONSTANT` since they are not needed and can cause issues if the package is used in different contexts.
- The `build` cli tool is used to parse the `pyproject.toml` file and build the package. Nowadays we use `wheel` format for packaging pre-compiled binaries.
- The sdist will be usefull for end users that want to OS different than mine. The wheel format is faster to install since it is pre-compiled binaries.
- Data files like `json` or `config` files can be included in the package using the `MANIFEST.in` file or by specifying it in the `pyproject.toml` file.
- For dependency check, i can use the package `pipdeptree` to see the dependency tree of the installed packages. It can be used to check for conflicts or to see which packages are installed as dependencies of other packages.

```bash
# the old approach to build the bin files
python setup.py build sdist

# and i will install the package in my virtual environment
pip install dist/packaging-0.0.0.tar.gz

# Install the current package in development mode
pip install -e .

# run the wheel format
pip install wheel
pip install build
python setup.py bdist_wheel # pre-compiled binaries and it is faster to install.

# running a cript with import style
python -m my_package.states_info # no.py extention here

# shows where pip thinks the package is installed
python -m pip show my_package

# use pip within conda for important STUFF HERE
python -m build --sdist --wheel # build both sdist and wheel source distributions
python -m pip install -e . # install the package in development mode
python -m pip install . # installs local package normally with its dependencies
python -m pip uninstall my-package

# plot dependency tree of installed packages
pipdeptree -p my-package --graph-output png > my-package-dependencies.png
conda install -c conda-forge graphviz # install graphviz to view the dependency tree
```

I can also run my tools using the config file in `.toml`, except .flake8 which has led to drama in the past. </br>

```bash
ruff check . --config ./pyproject.toml

# remember to stage and commit changes.
$ pre-commit run --all-files # run all pre-commit hooks on all files
```

**MONITORING DEPENDENCIES**
As we develop it is more prudent to slowly add the `requirements.txt` file or the `pyproject.toml` file with the dependencies that are needed. </br>
Then we just run `python -m pip install -e .` to install the package in development mode and it will install the dependencies as well. </br>
If everything operates well, run the pre-commit hooks and then build the package with `python -m build --sdist --wheel`.

Find shit installed by pip in my conda

```bash
where conda

find /c/Users/gpano/miniconda3 -type d -name "bioenv"

find /c/Users/gpano/miniconda3/bioenv -type f -name "*.json"

find /c/Users/gpano/miniconda3/envs/bioenv/Lib/site-packages/my_package -type f -name "*.json"

$ conda list | grep my-package # only works with "-" in the package name instead of "_" in the package name. This is a bug in conda, also this istalled by pip and better deleted by pip.
my-package                       0.1.0                  pypi_0                   pypi


```
