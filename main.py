import os
import sys
import subprocess
from parser import parse_command



while True :
    try :
        line = input("Kshell> ")
        cmd, args = parse_command(line)
        if cmd is None :
            continue
        #si la commande est quit on quitte le shell
        if cmd == "quit" :
            print("à la prochaine !")
            break



    #si on tappe ctrl+c
    except  KeyboardInterrupt :
        print()
    #si on tappe ctrl+d   
    except EOFError :
        print("à la prochaine !")
        sys.exit()
            