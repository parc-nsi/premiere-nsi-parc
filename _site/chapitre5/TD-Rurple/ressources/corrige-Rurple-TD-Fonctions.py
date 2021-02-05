from rurple import *

def parcourir_ligne():
    "Parcourt une ligne"
    while not mur_devant():
        avance()
        
#parcourir_ligne()
        
def tour_grille(n):
    "Effectue n tours d'une grille rectangulaire"
    for i in range(n):
        for j in range(4):
            parcourir_ligne()
            gauche()

def tour_grille2(n):
    "Effectue n tours d'une grille rectangulaire"
    for i in range(4 * n):
        parcourir_ligne()
        gauche()


#tour_grille(6)


def mystere():
    "Ramasse toutes les billes sur une case"
    while bille_au_sol():
        prends()
    
#mystere()


def aspirateur_ligne():
    "Ramasse toutes les billes sur une ligne"
    mystere()
    while not mur_devant():
        avance()
        mystere()
        
    
#aspirateur_ligne()


def droite():
    "Fait tourner le robot à droite"
    for k in range(3):
        gauche()
        
def quart_tour(ligne):
    if ligne % 2 == 1:
        gauche()
    else:
        droite()

def aspirateur_grille():
    "Ramasse toutes les billes sur une grille"
    ligne = 1
    aspirateur_ligne()
    quart_tour(ligne)
    while not mur_devant():
        avance()
        quart_tour(ligne)
        aspirateur_ligne()
        ligne = ligne + 1
        quart_tour(ligne)
        

#aspirateur_grille()

def demi_tour():
    gauche()
    gauche()
    
def bille_devant():
    "Détermine si la case devant contient une bille"
    avance()
    reponse = bille_au_sol()
    demi_tour()
    avance()
    demi_tour()
    return reponse
    

def petit_poucet():
    """Le robot parcourt toutes les cases d'une grille carré nxn avec n impair
    et dépose 1 billes sur chaque case """
    while bille_en_poche():
        depose()
        if mur_devant() or bille_devant():
            gauche()
        if not bille_devant():
            avance()            

petit_poucet()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
