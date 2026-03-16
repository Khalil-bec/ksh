from my_builtins import BUILTINS
import subprocess
import inspect


def execute_commande(commandes) :

    if len(commandes)>1 :
        pass
    else :
        commandes = commandes[0]
        cmd=commandes[0]
        args=commandes[1:]
        #si la commande est une commande interne on l'exécute
        if cmd in BUILTINS:
            #verifier si la fonction prend des arguments ou pas
            func = BUILTINS[cmd]
            if len(inspect.signature(func).parameters) == 0:
                func()
            else:
                func(args)
        else :
            #sinon on exécute la commande externe
            try :
                subprocess.run([cmd] + args)
            except FileNotFoundError :
                print(f"{cmd} : commande introuvable")