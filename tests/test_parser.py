from parser import parse_command

def test_simple():
    # Test 1: Commande simple sans pipe
    command = "ls -l"
    expected = [["ls", "-l"]]
    assert parse_command(command) == expected
def test_pipe():
    # Test 2: Commande avec un pipe
    command = "ls -l | grep py"
    expected = [["ls", "-l"], ["grep", "py"]]
    assert parse_command(command) == expected
def test_mutiple_pipes():
    # Test 3: Commande avec plusieurs pipes
    command = "cat file.txt | grep error | sort"
    expected = [["cat", "file.txt"], ["grep", "error"], ["sort"]]
    assert parse_command(command) == expected
def test_espaces_supp():
    # Test 4: Commande avec des espaces supplémentaires
    command = "   ls   -l   |   grep   py   "
    expected = [["ls", "-l"], ["grep", "py"]]
    assert parse_command(command) == expected
def test_commandes_vides():
    # Test 5: Commande vide
    command = "   "
    expected = None
    assert parse_command(command) == expected
def test_guillemets():    
    # Test 6: Commande avec des guillemets
    command = 'echo "Hello World" | grep Hello'
    expected = [["echo", "Hello World"], ["grep", "Hello"]]
    assert parse_command(command) == expected   

    print("Tous les tests sont passés avec succès !")
