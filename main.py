import os
import sys
import subprocess




while True :
    try :
        cmd = input("Kshell> ")
    


    #si on tappe ctrl+c
    except  KeyboardInterrupt :
        print()
    #si on tappe ctrl+d   
    except EOFError :
        print("à la prochaine !")
        sys.exit()
            