# test_arkyide.py
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
# - -
import re

def test_credits(capfd, arkyide_instance, monkeypatch):
    """Tests if the Credits method of arkyide_instance prints the expected output.

    Args:
        capfd: A pytest fixture for capturing output.
        arkyide_instance: An instance of the class containing the Credits method.
        monkeypatch: A pytest fixture for mocking functions.
    """

    # Mock input to avoid interactive call
    monkeypatch.setattr('builtins.input', lambda _: '')

    arkyide_instance.Credits()  # Call the Credits method

    # Capture the output
    captured = capfd.readouterr()
    output = captured.out

    # Remove escape sequences
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    output = ansi_escape.sub('', output)

    # Print captured output for debugging
    print(f"Captured Output:\n{output}")

    # Remove extra characters and leading/trailing spaces from the expected text
    expected_credits = """Project Arkyide
Project Arkyide, made by: 
Director Komrade - Project creator, Developer 
VenDis - Project Co-owner, Developer, Main Coder 
Thomas Waytec - Developer, Main Coder 
Sreesa - Developer
Kyyomaa - Developer
Allen Rodger - Developer, Project Manager"""
    expected_credits = expected_credits.strip()  # Remove leading/trailing whitespace

    # Print expected credits for debugging
    print(f"Expected Credits:\n{expected_credits}")

    # Assert the captured output matches the expected credits text (multiline string)
    assert output.strip() == expected_credits

#TODO: Define what we expect from Settings on arkyide menu
def test_setting(arkyide_instance, monkeypatch):
    pass

def test_invalid_selection(capfd, arkyide_instance):
    """Tests if invalid_selection prints the expected message.

    This test assumes invalid_selection directly prints the message.
    Adapt it if it triggers the message through other mechanisms.
    """

    arkyide_instance.invalid_selection()  # Call the invalid_selection method

    # Capture the output
    captured = capfd.readouterr()
    output = captured.out

    # Assert the captured output contains "Invalid selection"
    assert "Invalid selection" in output.strip()
