# Setup

Before attending an instructor lead version of this tutorial where you will be
executing the notebooks on your local machine (not in the cloud) the necessary
software should be installed and test data downloaded in to the correct
locations. Follow the instructions below to prepare your system.

1. Install the Anaconda (Miniconda is also fine) software distribution by
   following the links and instructions on the
   [Anaconda website](https://www.anaconda.com/distribution/). If this has
   already been installed there is no need to reinstall.


2. Add the ``conda-forge`` conda channel to your global configuration:

   ```shell
   conda config --add channels conda-forge
   ```

3. Update the ``conda`` package manager:

   ```shell
   conda update -y -n base conda
   ```

4. Create a conda sub-environment specifically for this repository and other
   future Satpy work:

   ```shell
   conda create -y -n satpy python=3.7 satpy rasterio imageio imageio-ffmpeg cartopy geoviews notebook
   ```

5. Active the new environment:

   ```shell
   conda activate satpy
   ```

   **Note**: If using older versions of conda, you may need to run
   ``source activate satpy`` (``activate satpy`` on Windows).


6. Test your installation:

   ```shell
   python -c "from satpy.config import check_satpy; check_satpy()"
   ```

   You should see output like below (`...` used for summary). If not, then your
   installation may be broken or corrupt. You may be able to use the error
   messages to determine what is missing or broken. Having "ok" for the below
   features does not guarantee that every part of this tutorial will complete
   successfully.
   
   ```plaintext
   Readers
   =======
   abi_l1b: ok
   ...
   viirs_sdr: ok
   
   Writers
   =======
   cf: ok
   geotiff: ok
   ...
   simple_image: ok

   Extras
   ======
   cartopy: ok
   geoviews: ok
   ```


7. Restart any notebooks with the new python environment activated:

   ```shell
   jupyter notebook
   ```

8. Download example data...**TODO**.