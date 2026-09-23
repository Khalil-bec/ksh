from my_builtins import BUILTINS
import subprocess
import inspect
from aliases import ALIASES

def execute_commande(commandes) :

    if len(commandes)>1 :
        precedente = None
        procs=[]
        for i,cmd in enumerate(commandes) :
            if i == 0 :
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            elif i == len(commandes)-1 :
                p = subprocess.Popen(cmd, stdin=precedente.stdout)
            else :
                p = subprocess.Popen(cmd, stdin=precedente.stdout, stdout=subprocess.PIPE)
                
            if precedente is not None:
                precedente.stdout.close()   # le parent n'a plus besoin de lire la sortie du processus précédent

            # On ajoute le processus à la liste des processus pour pouvoir attendre leur fin plus tard
            procs.append(p)
            precedente = p # On met à jour le processus précédent pour le prochain tour de boucle

        for proc in procs:
            proc.wait()
    else :
        commandes = commandes[0]
        cmd=commandes[0]
        args=commandes[1:]
        if cmd in ALIASES:
            from parser import parse_command
            nouvelle_ligne = ALIASES[cmd] + (" " + " ".join(args) if args else "")
            commandes = parse_command(nouvelle_ligne)
            if commandes:
                execute_commande(commandes)
            return
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