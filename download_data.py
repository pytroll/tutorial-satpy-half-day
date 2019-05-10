#!/usr/bin/env python
"""Download test data and ancillary data for running this tutorial."""


def download_pyspectral_luts():
    print("Downloading lookup tables used by pyspectral...")
    from pyspectral.utils import download_luts, download_rsr
    download_luts()
    download_rsr()
    return True


def download_test_data():
    return False


def main():
    ret = True
    ret &= download_pyspectral_luts()
    ret &= download_test_data()
    if ret:
        print("SUCCESS")
    else:
        print("FAIL")
    return ret


if __name__ == "__main__":
    import sys
    sys.exit(main())
