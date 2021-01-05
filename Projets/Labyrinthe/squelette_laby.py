from turtle import *
from random import randint

setworldcoordinates(-20, -20, 320, 320)
speed(0)
hideturtle()

# Partie A

# --- Question 1 ---

MursH = "à completer"
MursV = "à completer"

# --- Question 2 ---

def dim_laby(Laby):
    "à completer"

# --- Question 3 ---

def affiche_laby(Laby, Lmurs = 10):
    clear()   # remise à zéro de l'affichage turtle
    (n, p) = dim_laby(Laby)
    (MursH, MursV) = Laby
    
    for i in range(n + 1):
        M = (0, (n-i)*Lmurs)
        up()
        for j in range(p):
            goto(M)
            if MursH[i][j]:
                down()
            else:
                up()
            (x, y) = M
            M = (x + Lmurs, y)
            goto(M)
            
    # à compléter

# ===========  Partie B  ===========

# --- Question 1 ---

def position_valide(pos, dim):
    """ Fonction booléenne qui teste si pos est un couple de coordonnées
    d'une case dans les limites dim des dimensions d'un labyrinthe  """
    
    (n, p) = dim
    (i, j) = pos
    return  # à compléter ici

# --- Question 2 ---

def directions_possibles(Laby, Vues, pos):
    """ Renvoie une liste de chaines de caractères indiquant les différentes
    directions possibles pour désigner le mur à abattre à partir de la position
    pos lors de l'exécution de l'algorithme d'exploration exhaustive """
        
    dim = dim_laby(Laby)
    (MursH, MursV) = Laby
    (i, j) = pos
    directions = []
    
    # vers le nord
    nord = (i - 1, j)
    if position_valide(nord, dim) and not Vues[i-1][j]:
        directions.append('nord')
        
    # vers le sud
    # à compléter

    
    # vers l'ouest
    ouest = (i, j - 1)
    if position_valide(ouest, dim) and not Vues[i][j-1]:
        directions.append('ouest')
        
    # vers l'est
    # à compléter

    
    return directions

# --- Question 3 ---

def abattre_mur(Laby, pos, direction):
    """ Laby est un labyrinthe, pos désigne la position d'une
    case et direction est une chaine de caractère désignant le
    mur à abattre du point de vue de la case. Modifie Laby pour
    changer la valeur du booléen qui représente le statut (présent
    ou absent) du mur à abatre et renvoie la position de la case
    vers laquelle on se déplace.
       """

    (MursH, MursV) = Laby
    (i, j) = pos
    
    if direction == 'nord':
        MursH[i][j] = False
        return (i - 1, j)
    # à compléter        

# --- Question 4 ---

def genere_laby(n, p):
    """ Renvoie un couple (MursH, MursV) qui représente un labyrinthe
    aléatoire parfait de dimension (n, p) obtenu en appliquant
    l'algorithme d'exploration exhaustive """

    # tableau des cases visitées. Au départ, aucune n'a été visitée
    Vues = [[False for _ in range(p)] for _ in range(n)]
    # tableau des murs horizontaux, tous présents au départ
    MursH = [[True for _ in range(p)] for _ in range(n + 1)]
    # tableau des murs verticaux, tous présents au départ
    MursV = [[True for _ in range(p + 1)] for _ in range(n)]
    Laby = (MursH, MursV)

    # On choisit au hasard le point de départ
    
    (i, j) = (randint(0, n - 1), randint(0, p - 1))
    depart = (i, j)
    Chemin = [depart]
    Vues[i][j] = True

    while len(Chemin) > 0:
        pos = Chemin[-1]
        Directions = directions_possibles(Laby, Vues, pos)
        if len(Directions) == 0:  # Impasse
            Chemin.pop()
        else:
            "à compléter"
            
    return Laby

# deux petits labyrinthes pour vos tests

Laby1 = ([[True, True, True], [False, False, True], [True, True, True]],
         [[True, True, False, True], [True, False, False, True]])


Laby2 = ([[True, True, True, True, True], [False, True, True, False, True],
          [False, True, False, True, True], [True, True, True, True, True]],
         [[True, False, False, False, False, True],
            [True, True, False, True, False, True],
            [True, False, False, False, False, True]])
                                                                                                                                             

# getcanvas().postscript(file="laby_40x40.eps")

#pour fermer proprement la fenetre de la tortue en cliquant sur la croix
exitonclick()
