from my_builtins import BUILTINS
import os

def test_cd_sans_arg():
    # Test 1: Changer de répertoire
    BUILTINS['cd']( [])
    expected = os.getcwd()
    home = os.path.expanduser("~")
    assert expected == home
    
def test_cd_parent():
    # Test 2: Changer de répertoire vers un dossier spécifique
    BUILTINS['cd']( [".."] )
    expected = os.getcwd()
    parent = os.path.dirname(os.path.expanduser("~"))
    assert expected == parent
def test_cd_dossier_existent():
    # Test 3: Changer de répertoire vers un dossier qui existe
    BUILTINS['cd']( ["/"] )
    expected = os.getcwd()
    assert expected == "/"

def test_cd_non_existent():
    # Test 4: Changer de répertoire vers un dossier qui n'existe pas 
    avant=os.getcwd()
    BUILTINS['cd']( ["non_existent_directory"] )
    assert os.getcwd() == avant
    
        