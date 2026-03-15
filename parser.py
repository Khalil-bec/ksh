import shlex

# diviser la commende en tokens
def parse_command(command):
    token = shlex.split(command)
    #si la commande est vide on retourne None
    if len(token) == 0:
        return None, None
    

    #le premier token est la commande, les autres sont les arguments
    cmd = token[0]
    args = token[1:]
    return cmd, args