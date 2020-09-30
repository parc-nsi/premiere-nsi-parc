from rurple import *

def parcourir_ligne():
    "Parcourt une ligne"
    while not mur_devant():
        avance()
        
parcourir_ligne()

def mystere():
    while bille_au_sol():
        prends()
    
#mystere()
