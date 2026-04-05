import os
import sys

def cd(args) :
    if len(args) == 0 :
        os.chdir(os.path.expanduser("~"))
    else :
        try :
            os.chdir(args[0])
        except FileNotFoundError :
            print(f"cd: {args[0]}: il n'y a pas de tel fichier ou répertoire")


def pwd() :
    print(os.getcwd())

def exit() :
    print("à la prochaine !")
    sys.exit()    

AIDE_TEXTE = {
    "cd"     : "cd [répertoire]    — changer de répertoire. Sans argument, retourne au ~",
    "pwd"    : "pwd                — afficher le répertoire courant",
    "exit"   : "exit               — quitter le shell",
    "alias"  : "alias [nom=valeur]— créer/lister les alias persistants",
    "unalias": "unalias <nom>     — supprimer un alias",
    "aide"   : "aide [commande]    — afficher l'aide. Sans argument, liste tout",
}

def aide(args):
    if len(args) == 0:
        print("\n\033[1;36m=== Commandes disponibles dans ksh ===\033[0m\n")
        for commande, description in AIDE_TEXTE.items():
            print(f"  \033[1;33m{commande:<10}\033[0m {description.split('—')[1].strip()}")
        print("\nTape \033[1maide <commande>\033[0m pour plus de détails.\n")
    else:
        cmd = args[0]
        if cmd in AIDE_TEXTE:
            print(f"\n  \033[1;33m{AIDE_TEXTE[cmd]}\033[0m\n")
        else:
            print(f"aide: aucune aide disponible pour '{cmd}'")



from aliases import ALIASES, sauvegarder_aliases

def alias(args):
    if len(args) == 0:
        # Lister tous les alias
        if not ALIASES:
            print("Aucun alias défini.")
        for nom, valeur in ALIASES.items():
            print(f"alias {nom}='{valeur}'")
    else:
        # Parser "ll=ls -la" ou "ll='ls -la'"
        arg = " ".join(args)
        if "=" not in arg:
            # Afficher un alias précis
            if arg in ALIASES:
                print(f"alias {arg}='{ALIASES[arg]}'")
            else:
                print(f"alias: {arg}: alias introuvable")
            return
        nom, _, valeur = arg.partition("=")
        nom = nom.strip()
        valeur = valeur.strip().strip("'\"")
        ALIASES[nom] = valeur
        sauvegarder_aliases(ALIASES)
        print(f"Alias '{nom}' créé → '{valeur}'")

def unalias(args):
    if len(args) == 0:
        print("unalias: usage: unalias <nom>")
        return
    nom = args[0]
    if nom in ALIASES:
        del ALIASES[nom]
        sauvegarder_aliases(ALIASES)
        print(f"Alias '{nom}' supprimé.")
    else:
        print(f"unalias: {nom}: alias introuvable")


BUILTINS={
    "cd" : cd,
    "pwd" : pwd,
    "exit" : exit,
    "aide" : aide,
    "alias" : alias,
    "unalias" : unalias
}