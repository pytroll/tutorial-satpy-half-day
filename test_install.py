#!/usr/bin/env python
"""Test that the installation steps for this tutorial were successful.

1. Check that Satpy features are available and all dependencies are importable.
2. Check that data has been downloaded.

"""

import io
import os
from contextlib import redirect_stdout

try:
    from satpy.config import check_satpy
except ImportError:
    print("FAIL: Satpy is not importable")
    raise


TUTORIAL_ROOT = os.path.dirname(os.path.abspath(__file__))


def check_satpy_features():
    print("Checking Satpy features...\n")
    readers = ['abi_l1b', 'viirs_sdr']
    writers = ['cf', 'geotiff', 'simple_image']
    extras = ['cartopy', 'geoviews']
    out = io.StringIO()
    with redirect_stdout(out):
        check_satpy(readers=readers, writers=writers, extras=extras)
    out_str = out.getvalue()
    print(out_str)

    for feature in readers + writers + extras:
        if feature + ":  ok" not in out_str:
            print("FAIL: Missing or corrupt Satpy dependency (see above for details).")
            return False
    return True


def check_data_download():
    abi_exists = os.path.isdir(os.path.join(TUTORIAL_ROOT, 'data', 'abi_l1b'))
    viirs_exists = os.path.isdir(os.path.join(TUTORIAL_ROOT, 'data', 'viirs_sdr'))
    all_ok = all([abi_exists, viirs_exists])
    if not all_ok:
        print("FAIL: Missing test data files.")
    return all([abi_exists, viirs_exists])


def main():
    ret = True
    ret &= check_satpy_features()
    ret &= check_data_download()
    if ret:
        print("SUCCESS")
    else:
        print("FAIL")
    return ret


if __name__ == "__main__":
    import sys
    sys.exit(main())
