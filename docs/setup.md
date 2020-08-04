# Set up your computer

## Anaconda
It is recommended to install Python via the [Anaconda Distribution](https://www.anaconda.com/products/individual#Downloads). We will use the Conda Package Management System included in the Anaconda Distribution. From the [documentation](https://conda.io/docs):
> Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer. 

After installing Anaconda, run `python --version` in a terminal (if you're on Windows, use the "Anaconda Prompt"). If the output contains "Python 3.8" and "Anaconda" then you're ready for the next step.

## GitHub
The course material is hosted on the code-sharing platform GitHub (where you're currently reading this). If you're not already registered at GitHub, make a user account now. https://github.com/join. It is recommended to use the platform for your own projects during the course. 

## Kaggle
[Kaggle](https://www.kaggle.com) is an online community of "data scientists", arranging data science competitions and hosting a large number of data sets. We'll make use of Kaggle in DAT158, both for course projects and as a source of data. Make an account here: https://www.kaggle.com. 

## Install and test the course environment
After installing Anaconda, run through the following steps (on Windows, use the "Anaconda Prompt").

### Install Git
```bash
conda install git
```

### Download the course repository: 
```bash
git clone https://github.com/alu042/DAT158ML
cd DAT158ML
```

### Configure the Python environemnt
```bash
conda env update
```

### Activate the environment
```bash
conda activate dat158
```
If you're using Linux or MacOS and the above command fails, run
```bash 
source ~/.bash_profile
``` 
and try again: `conda activate dat158`.

### Install a Jupyter kernel
```bash
python -m ipykernel install --user --name dat158 --display-name "DAT158"
```

### Test your installation
Go through the notebook `notebooks/0.0-test.ipynb`:
```bash
jupyter notebook
```
You can alternatively use [JupyterLab](https://github.com/jupyterlab/jupyterlab): 
```bash
jupyter lab
```

## Updating
The code and environment will be updated throughout the course. Run the following commands regularly: 
* Update code: `git pull`
* Update environment: 
```bash
conda activate dat158
conda env update
```


# Troubleshooting
* If you're on a Mac and the `conda env update` command fails with a `gcc` error, install [Xcode](https://developer.apple.com/xcode/resources/) through the App store and use it to install **command line tools**. 
