import os
import re
import json
import pytest
from unittest.mock import patch, MagicMock
import sys
from unittest.mock import patch
import subprocess
from unittest.mock import patch, MagicMock


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arkyide.lib import netscan