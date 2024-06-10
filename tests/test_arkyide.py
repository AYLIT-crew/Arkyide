# test_arkyide.py
import os
import json
import pytest
from unittest.mock import patch, MagicMock
import sys
from termcolor import colored as cl
from unittest.mock import patch
import subprocess
from unittest.mock import patch, MagicMock


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from arkyide import Arkyide

@pytest.fixture
def arkyide_instance():
    return Arkyide()

def test_load_settings_existing_file(tmp_path, arkyide_instance):
    settings_data = {"disclaimer": "enabled"}  
    settings_file = tmp_path / "settings.json"
    with open(settings_file, 'w') as file:
        json.dump(settings_data, file)
    
    arkyide_instance.settings_file = str(settings_file)
    settings = arkyide_instance.load_settings()
    assert settings == settings_data

def test_load_settings_non_existing_file(tmp_path, arkyide_instance):
    
    settings_file = tmp_path / "settings.json"
    
    arkyide_instance.settings_file = str(settings_file)
    
    settings = arkyide_instance.load_settings()
    
    assert settings == {"disclaimer": "enabled"}


def test_save_settings(tmp_path, arkyide_instance):
    settings_data = {"disclaimer": "disabled"}
    
    settings_file = tmp_path / ".settings.json"
    
    arkyide_instance.settings = settings_data
    
    arkyide_instance.settings_file = str(settings_file)
    
    arkyide_instance.save_settings()
    
    with open(settings_file, 'r') as file:
        saved_settings = json.load(file)
    
    assert saved_settings == settings_data


def test_show_curses_disclaimer(capfd, monkeypatch, arkyide_instance):
    pass
def test_disclaimer_start_existing_settings(tmp_path, monkeypatch, arkyide_instance):
    pass
def test_menu(capfd, monkeypatch, arkyide_instance):
    pass
