Anaconda is a virtual environment manager for python data science libraries.

# Install and Configuration

1. anaconda can be [downloaded here](https://www.continuum.io/downloads).
2. [how to mange python versions](http://conda.pydata.org/docs/py2or3.html)

## Useful commands:

```bash
# create env with python2 and anaconda
conda create -n py2conda python=2.7 anaconda
# create env with python3 and anaconda
conda create -n py35conda python=3.5 anaconda
source activate py35conda # activate env just created
source deactivate # deactivate env
# list all envs
conda info --envs
conda-env list
conda list # list all packages in current env
```

# Jupyter Notebook

Jupyter notebook is included in anaconda.

```bash
jupyter notebook # start notebook server in current directory
# extract python code from notebook
jupyter nbconvert --to script <notebook.ipynb>
```
You can set up a post save hook as indicated [at this link](http://jupyter-notebook.readthedocs.io/en/latest/extending/savehooks.html). If you do not already have a `jupyter_notebook_config.py` file in your home directory `~/.jupyter/`, you can generate one with `jupyter notebook --generate-config`.

# Resources

- [official docs](https://docs.continuum.io/anaconda/)
- [conda test drive tutorial](http://conda.pydata.org/docs/test-drive.html)
- [cheatsheet](http://conda.pydata.org/docs/using/cheatsheet.html)
