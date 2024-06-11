import os
import re
import json
import pytest
from unittest.mock import patch, MagicMock
import sys
import subprocess


from lib.net_scan import NetScan


# Ignore this test, it's just for testing purpose
def test_net_scan():
    assert 1 == 1