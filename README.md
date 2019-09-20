# Description

The Python script `get_column_stats.py` allows the user to input a tab separated file of numerical data and find the mean and standard deviation of one of the columns. The additions made to it involve primarily modifying it to follow best practices and to implement both unit and functional tests.

# Usage

The basic usage of `get_column_stats.py` is as follows.

```
python_get_column_stats.py --file_name FILE_NAME --col_num COL_NUM
```

Where `FILE_NAME` is the file name and `COL_NUM` is the zero-indexed column number. for more information on usage do `python get_column_stats.py -h`.

# Installation

Instalation is done through Conda, to install Conda enter the following commands

```
cd $HOME
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
. $HOME/miniconda3/etc/profile.d/conda.sh
conda update --yes conda
conda config --add channels bioconda
echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> $HOME/.bashrc
```

We then create a new environment and install the supported python version. Here we simply name the Conda environment `gcsenv`.

```
conda create --yes -n gcsenv
conda install --yes python=3.6
```

Finally we go into this environment, install the needed package, `pycodestyle`, and pull the repository.

```
conda activate swe4s
conda install -y pycodestyle
git clone https://github.com/cu-swe4s-fall-2019/best-practices-f-collins.git
```

After going into the repository directory, `get_column_stats.py` may now be used as described in the usage section.
