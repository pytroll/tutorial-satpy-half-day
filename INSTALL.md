# Setup

Before attending an instructor lead version of this tutorial where you will be
executing the notebooks on your local machine (not in the cloud) the necessary
software should be installed and test data downloaded in to the correct
locations. Follow the instructions below to prepare your system.

1. Download the contents of the tutorial repository. You can either clone
   the git repository using the `git` command in a terminal window:
   
   ```shell
   git clone https://github.com/pytroll/tutorial-satpy-half-day
   ```
   
   If you do not have `git` installed it can be downloaded and installed from
   [the git SCM website](https://github.com/pytroll/tutorial-satpy-half-day).
   
   Or you can get a copy of the repository by downloading the
   `.zip` file at the URL below and unzipping it on your system:
   
   https://github.com/pytroll/tutorial-satpy-half-day/archive/master.zip

2. Install the Anaconda (Miniconda is also fine) software distribution by
   following the links and instructions on the
   [Anaconda website](https://www.anaconda.com/distribution/). If this has
   already been installed there is no need to reinstall.

3. Open a terminal (PowerShell or Command Prompt in Windows) and change to
   the root tutorial directory (where the `INSTALL.md` file is):
   
   ```shell
   cd /path/to/tutorial
   ```
    
   You will use the terminal to run the following commands.

4. Add the ``conda-forge`` conda channel to your global configuration:

   ```shell
   conda config --add channels conda-forge
   ```

5. Update the ``conda`` package manager:

   ```shell
   conda update -y -n base conda
   ```

6. Create a conda sub-environment specifically for this tutorial and other
   future Satpy work:

   ```shell
   conda create -y -n satpy python=3.7 satpy rasterio imageio imageio-ffmpeg cartopy geoviews notebook
   ```

7. Active the new environment:

   ```shell
   conda activate satpy
   ```

   **Note**: If using older versions of conda, you may need to run
   ``source activate satpy`` (``activate satpy`` on Windows).

8. Download example data:

   ```shell
   python download_data.py
   ```

   You should see `SUCCESS` as the last line of output.


9. Test your installation:

   ```shell
   python test_install.py
   ```

   You should see `SUCCESS` as the last line of output.
   
10. Start the Jupyter Notebook server from the activate python environment
    so we can run the tutorial's notebooks.

    ```shell
    jupyter notebook
    ```
    
    Your web browser should open to the local notebook server. Navigate
    to the tutorial notebooks by clicking on the "notebooks" folder in the
    browser.
