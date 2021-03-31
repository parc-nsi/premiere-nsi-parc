# -*- coding: utf-8 -*-

from tkinter import *

#----fenetre principale----
fenetre = Tk()
fenetre.title("Tic-Tac-Toe")
#construire la fenetre à 100 pixels du cote gauche de l'ecran et 150 pixels du cote haut
fenetre.geometry("+100+150")
#interdire la modification de la taille de la fenetre
fenetre.resizable(width=False, height=False)


#----boucle de réception des événements----
#à placer à la fin du programme 
fenetre.mainloop()