#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

__version__ = "1.0.1"

from Runner import Run as _Run
import pytest


@pytest.fixture(scope="session")
def Run(request):
    """
        Returns runner class Run for the use in tests.
    """
    return _Run
