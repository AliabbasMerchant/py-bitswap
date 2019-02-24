#!/usr/bin/python


import contextlib
import pathlib
import os
import sys

if not hasattr(contextlib, "suppress"):
    """
    Polyfill for ``contextlib.suppress``
    """
    @contextlib.contextmanager
    def _contextlib_suppress(*exceptions):
        try:
            yield
        except exceptions:
            pass
    contextlib.suppress = _contextlib_suppress

######################
# Test configuration #
######################

# Environment name as used by `tox`
ENVNAME = "py{}{}".format(sys.version_info.major, sys.version_info.minor)

# Determine project base directory and testing path
BASE_PATH = pathlib.Path(__file__).parent.parent
TEST_PATH = BASE_PATH / "build" / "test-{}".format(ENVNAME)

###########################
# Set up test environment #
###########################

# Add project directory to PYTHONPATH
sys.path.insert(0, str(BASE_PATH))
# Switch working directory to project directory
os.chdir(str(BASE_PATH))
# Export environment variables required for testing

import bitswap

##################
# Run test suite #
##################

# PYTEST_CODE = 1
# try:
# Run test in CI-mode
os.environ["CI"] = "true"

# Make sure all required py.test plugins are loaded
# os.environ["PYTEST_PLUGINS"] = ",".join(["pytest_cov", "pytest_ordering"])

# Launch py.test in-process
import pytest

PYTEST_CODE = pytest.main([
                              "--verbose",
                          ] + sys.argv[1:])
# finally:

sys.exit(PYTEST_CODE)
