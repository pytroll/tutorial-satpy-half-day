#!/usr/bin/env python
import os
os.environ['OMP_NUM_THREADS'] = os.environ['MKL_NUM_THREADS'] = '2'
os.environ['PYTROLL_CHUNK_SIZE'] = '1024'

import warnings
warnings.simplefilter('ignore')

import dask
dask.config.set(scheduler='threads', num_workers=4)
