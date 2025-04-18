import sys
import platform

def test_os():
    assert platform.system() == "Linux", "You have to use a Linux Operating System!"

def test_python_version():
    assert sys.version[:4] in ["3.12", "3.13"], "Your python version must be either 3.10 or 3.11"
