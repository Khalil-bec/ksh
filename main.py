import os
import sys
import subprocess
from parser import parse_command
from executor import execute_commande



while True :
    try :
        line = input("Kshell> ")
        cmd, args = parse_command(line)
        if cmd is None :
            continue
        else :
            execute_commande(cmd, args)



    #si on tappe ctrl+c
    except  KeyboardInterrupt :
        print()
    #si on tappe ctrl+d   
    except EOFError :
        print("à la prochaine !")
        sys.exit()
            