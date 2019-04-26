===================================
Tutorial: Satpy Overview - Half day
===================================

This repository contains Jupyter notebooks to walk the user through the basic
functionality of the Satpy Python library. The notebooks are meant to be
stepped through in order as lessons in a tutorial. When lead by an instructor
in a class, the lessons should take about 4 hours to complete.

In addition to the lessons in the `notebooks/` directory, this repository is
configured to run from Pangeo's binder instance. This allows users to run
the notebook examples from the cloud, with no need to install software or
download data to their local machine. See http://pangeo.io for more information.

Try these notebooks on pangeo.binder.io_ : |Binder|

.. _pangeo.binder.io: http://binder.pangeo.io/

.. |Binder| image:: http://binder.pangeo.io/badge.svg
    :target: http://binder.pangeo.io/v2/gh/pytroll/tutorial-satpy-half-day/master

Prerequisites
-------------

This tutorial requires only basic python and numpy experience. Any additional
experience with xarray or dask is not required but will make the lessons
easier to understand and more effective.

Lessons
-------

All lesson notebooks are in the `notebooks/` directory. See the first
notebook,
`01_introduction.ipynb <https://github.com/pytroll/tutorial-satpy-half-day/blob/master/notebooks/01_introduction.ipynb>`_,
for details on the lessons as a whole and to start the tutorial.

Local Installation
------------------

Before attending an instructor lead version of this tutorial where you will be
executing the notebooks on your local machine (not in the cloud) the necessary
software should be installed and test data downloaded in to the correct
locations. Follow the `INSTALL <./INSTALL.md>`_ instructions for how to create
the proper conda environment. Once completed and your new environment is
activated, verified, and test data downloaded you can open these lessons by
starting Jupyter Notebook and navigating to the `notebooks/` directory.

.. code-block:: bash

    jupyter notebook

Run individual code cells in the notebook by typing "Shift+Enter" for each
cell.
