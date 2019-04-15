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
locations. Follow the instructions below to prepare your system.

1. Install the Anaconda (Miniconda is also fine) software distribution by
following the links and instructions on the
`Anaconda website <https://www.anaconda.com/distribution/>`_. If this has
already been installed there is no need to reinstall.

2. Add the ``conda-forge`` conda channel to your global configuration:

.. code-block:: console

    conda config --add channels conda-forge

3. Update the ``conda`` package manager:

.. code-block:: console

    conda update -y -n base conda

3. Create a conda sub-environment specifically for this repository and other
future Satpy work:

.. code-block:: console

    conda create -y -n satpy python=3.7 satpy rasterio imageio imageio-ffmpeg geoviews

4. Active the new environment:

.. code-block:: console

    conda activate satpy

.. note::

    If using older versions of conda, you may need to run
    ``source activate satpy`` (``activate satpy`` on Windows).

5. Download example data...TODO.
