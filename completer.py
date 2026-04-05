import os
import readline
from my_builtins import BUILTINS
from aliases import ALIASES


def get_commandes_disponibles():
    #Récupère toutes les commandes exécutables dans le PATH
    commandes = set()
    for dossier in os.environ.get("PATH", "").split(":"):
        try:
            for fichier in os.listdir(dossier):
                chemin = os.path.join(dossier, fichier)
                if os.access(chemin, os.X_OK):
                    commandes.add(fichier)
        except (FileNotFoundError, PermissionError):
            pass
    return commandes


# On calcule ça une seule fois au démarrage, pas à chaque Tab
COMMANDES_PATH = get_commandes_disponibles()


def completer(text, state):
  
    ligne = readline.get_line_buffer()
    mots = ligne.split()

    # --- Complétion de commande (premier mot) ---
    if len(mots) == 0 or (len(mots) == 1 and not ligne.endswith(" ")):
        toutes = COMMANDES_PATH | set(BUILTINS.keys()) | set(ALIASES.keys())
        matches = sorted(c for c in toutes if c.startswith(text))

    # --- Complétion de fichier/dossier (arguments) ---
    else:
        # Expand ~ si besoin
        chemin = os.path.expanduser(text) if text.startswith("~") else text

        dossier = os.path.dirname(chemin) or "."
        prefixe = os.path.basename(chemin)

        try:
            entrees = os.listdir(dossier)
        except OSError:
            entrees = []

        matches = []
        for entree in sorted(entrees):
            if entree.startswith(prefixe):
                if dossier == ".":
                    complet = entree
                else:
                    complet = os.path.join(dossier, entree)
                if os.path.isdir(os.path.join(dossier, entree)):
                    complet += "/"
                matches.append(complet)

    return matches[state] if state < len(matches) else None


def configurer_autocomplete():
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")
    readline.set_completer_delims(" \t\n;|&")