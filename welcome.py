import pyfiglet
from colorama import Fore, Style

def afficher_bienvenue():
    print("\n\n\n\n" + Fore.CYAN + pyfiglet.figlet_format("K SHELL", font="doom") + Style.RESET_ALL)
    print(Style.BRIGHT+"Bienvenue dans Kshell votre shell simple en Français!" + Style.RESET_ALL+ Fore.RED + " \nTapez 'exit' pour quitter." + Style.RESET_ALL)
    print("Tapez 'aide' pour afficher les commandes disponibles." )
    print(Style.DIM + "crée par Mohamed Khalil BECHEIKH" + Style.RESET_ALL  + "\n")
    print("----------------------------------------------------------------------\n\n")
