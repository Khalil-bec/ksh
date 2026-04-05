import os
import sys
import readline
import subprocess
from welcome import afficher_bienvenue
from parser import parse_command
from executor import execute_commande
from completer import configurer_autocomplete
from prompt import get_prompt





afficher_bienvenue()
configurer_autocomplete()
while True :
    try :
        line = input(get_prompt())
        commandes = parse_command(line)
        if commandes is None :
            continue
        else :
            execute_commande(commandes)



    #si on tappe ctrl+c
    except  KeyboardInterrupt :
        print()
    #si on tappe ctrl+d   
    except EOFError :
        print("à la prochaine !")
        sys.exit()
            