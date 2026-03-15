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



BUILTINS={
    "cd" : cd,
    "pwd" : pwd,
    "exit" : exit
}