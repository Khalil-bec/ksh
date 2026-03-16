import shlex

# diviser la commende en tokens
def parse_command(command):
      #si la commande est vide on retourne None
    if not command.strip():
        return None
    commandes=[]
    courante=[]
    token = shlex.split(command)

    for t in token:
        if t == '|':
            commandes.append(courante)
            courante = []
        else:
            courante.append(t)
    commandes.append(courante)

  
    
    return commandes