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
#Validating...
def test_credits(self, capfd, arkyide_instance, monkeypatch):
    with capfd.capture() as output:
        arkyide_instance.Credits()

    # Assert the captured output matches the expected credits text (multiline string)
    assert output.captured[0].out == """Project Arkyide\nProject Arkyide, made by: \nDirector Komrade - Project creator, Developer \nVenDis - Project Co-owner, Developer, Main Coder \nThomas Waytec - Developer, Main Coder \nSreesa - Developer\nKyyomaa - Developer\nAllen Rodger - Developer, Project Manager\n"""
    
#Validating...
def test_setting(self, arkyide_instance, monkeypatch):
    # Patch time.sleep to avoid actual delay during testing
    mock_sleep = monkeypatch.patch('time.sleep')

    arkyide_instance.setting()

    # Assert that time.sleep was called
    assert mock_sleep.called

    # Assert that time.sleep was called with the expected argument (3 seconds)
    mock_sleep.assert_called_once_with(3)

#Validating...
def test_invalid_selection(self, capfd, arkyide_instance):
    with capfd.capture() as output:
        arkyide_instance.invalid_selection()

    assert output.captured[0].out == "Invalid selection\n"
