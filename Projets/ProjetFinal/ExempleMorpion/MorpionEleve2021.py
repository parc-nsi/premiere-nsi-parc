# -*- coding: utf-8 -*-

"""
Squelette de code pour le mini-projet modèle Morpion / Tic-Tac-Toe

Architecture du code selon le principe de séparation des parties Modèle Vue Controleur
https://fr.wikipedia.org/wiki/Mod%C3%A8le-vue-contr%C3%B4leur
"""

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#---------------------------------------Import des modules---------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter.messagebox import showinfo
import  random
import time


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#--------------------- Partie Modèle (variables et fonctions logiques du jeu)--------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

# Constantes du programme

#Joueurs :
JOUEUR_1 = 1
JOUEUR_2 = 2

#Couleurs
COULEUR_CASE = ["white","#3E61EA", "green"]
COULEUR_BORD_CASE ="#000000"
COULEUR_BOUTON = "#3E61EA"
COULEUR_JOUEUR = {JOUEUR_1 : 'Bleu', JOUEUR_2 : 'Vert'}

#Coté d'une case en pixels
COTE_CASE = 100

#Délai de réponse maximal en secondes
TEMPS_MAX = 5

# Fonctions de gestion de la logique du jeu

def initialiser_grille():
    """Retourne une grille 3 x 3 sous forme de liste de listes remplie de 0"""
    return [[0] * 3 for k in range(3)]


def adversaire(joueur):
    """Retourne le code de l'adversaire du joueur"""
    return 3 - joueur

def copie(grille):
    """Retourne une copie de la grille"""
    #A MODIFIER
    "à compléter"

def liste_alignement(grille):
    """Retourne une liste de listes représentant les 8 alignements
    possibles dans la grille"""
     #A MODIFIER
    "à compléter"

def nb_occurrence(liste, joueur):
    """Retourne le nombre d'occurences du code du joueur (1 ou 2) dans une liste"""
    #A MODIFIER
    "à compléter"

def verifier(grille, joueur):
    """Vérifie si  joueur a gagné avec la grille donnée
    Retourne un booléen
    """
    #A MODIFIER
    "à compléter"

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#--------------------- Partie Vue (mise en place de l'interface graphique)-----------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

#Fonction d'initialisation de l'interface graphique
#A MODIFIER
def initialiser_plateau(plateau, case_vers_identifiant):
    """Initialise le plateau"""
    for li in range(3):
        for co in range(3):
            "compléter"

#Fonction pour quitter l'interface graphique
def quitter():
    """Quitter proprement la fenetre"""
    fenetre.quit()
    fenetre.destroy()

# Fonctions de gestion d'une partie

def nouvelle_partie():
    """Initialise et lance une nouvelle partie"""
    global vainqueur, joueur, tour, grille, choix_joueur1, choix_joueur2
    grille = initialiser_grille()
    tour = 1
    joueur = random.randint(1, 2)
    textJoueur.set("Joueur : {}".format(COULEUR_JOUEUR[joueur]))
    initialiser_plateau(plateau, case_vers_identifiant)
    vainqueur = 0
    choix_joueur1 = False
    choix_joueur2 = False
    nouveau_tour()

def chronometre():
    """Fonction récursive qui met à jour l'horloge lors d'un tour"""
    duree = time.time()- debut_tour
    minute, seconde  = divmod(int(duree),  60)
    textHorloge.set("Chrono: {:02d}:{:02d}".format(minute, seconde))
    if duree < TEMPS_MAX:
        fenetre.after(1000, chronometre)

def nouveau_tour():
    """Fonction récursive qui lance un nouveau tour"""
    global vainqueur,joueur, tour, debut_tour, curseur, xcurseur, ycurseur, choix_joueur1, choix_joueur2
    #on positionne les joueurs
    joueur_precedent = joueur
    joueur = adversaire(joueur)
    #mise à jour de l'affichage du joueur
    textJoueur.set("Joueur : {}".format(COULEUR_JOUEUR[joueur]))
    #si le joueur précédent n'a pas cliqué le joueur courant est vainqueur
    #attention à bien mettre des parenthèses autour du or pour changer la priorité par défaut des opérateurs booléens
    if tour >= 2 and (joueur_precedent == JOUEUR_1 and not choix_joueur1 \
    or joueur_precedent == JOUEUR_2 and not choix_joueur2):
        vainqueur = joueur
    #sinon on vérifie si le joueur précédent  a gagné
    elif verifier(grille, joueur_precedent):
        vainqueur = joueur_precedent
    #On affiche le vainqueur sil y en un ou si on a atteint le 10ème tour
    if tour == 10 or vainqueur != 0:
        if joueur == JOUEUR_1:
            plateau.delete(curseur)
        message_fin(vainqueur)
    else: #sinon on commence un nouveau tour
        #pause de 1 seconde avant le changement de joueur
        time.sleep(2)
        #on démarre le chronomètre
        debut_tour = time.time()
        chronometre()
        #on positionne à False les booléens indiquant si le joueur courant a fait son choix
        choix_joueur1 = False
        choix_joueur2 = False
        #pour le joueur 2
        if joueur == JOUEUR_2:
            xcurseur, ycurseur = 0, 0
            curseur = plateau.create_rectangle(xcurseur, ycurseur , xcurseur + COTE_CASE, ycurseur + COTE_CASE,
        outline = 'red',  fill='', width=2)
        elif tour >= 2: #pour le joueur1 à partir du tour 2
            plateau.delete(curseur)
        #on incrémente le compteur de tour pour le tour suivant
        tour = tour + 1
        #on attend TEMPS_MAX secondes (argument en millisecondes) avant de commencer un nouveau tour
        #pendant la durée d'un tour les gestionnaires d'événements gèrent les actions
        fenetre.after(TEMPS_MAX * 1000, nouveau_tour)

def message_fin(vainqueur):
    """Affichage de fin de partie"""
    #A MODIFIER
    if vainqueur == 0:
        showinfo("Fin", "Fin de partie, match nul")


def interface_jeu():
    """
    Mise en place de l'interface graphique, fenetre principale et widgets
    Renvoie :
        les tous les widgets :  fenetre, textHorloge, bouton_quitter, plateau
        les tableaux de correspondance entre les items du canevas plateau
        et leurs identifiants : case_vers_identifiant, identifiant_vers_case
        
    """    
    #----fenetre principale----
    fenetre = Tk()
    fenetre.title("Tic-Tac-Toe")
    #construire la fenetre à 100 pixels du cote gauche de l'ecran et 150 pixels du cote haut
    fenetre.geometry("+100+150")
    #interdire la modification de la taille de la fenetre
    fenetre.resizable(width=False, height=False)

    #----Canevas----
    #il faut diriger les entrées claviers vers le canevas qui n'a pas le focus par défaut
    #voir http://tkinter.fdex.eu/doc/focus.html#focus
    plateau = Canvas(fenetre, width = COTE_CASE * 3, height = COTE_CASE * 3, bg = 'white', takefocus = 1)
    plateau.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)
    case_vers_identifiant = [ [0 for j in range(3)] for i in range(3) ]
    identifiant_vers_case = [ (0,0) for k in range(9) ]

    #---Création des items du canevas et de leurs identifiants----
    #A MODIFIER
    for lig in range(3):
        for col in range(3):
            "compléter / modifier la ligne ci-dessous"
            (x, y) = (0,0)  # A MODIFIER valeurs arbitraires
            iden = plateau.create_rectangle(x, y , x + COTE_CASE, y + COTE_CASE, 
                                            outline = COULEUR_BORD_CASE, 
                                            fill= COULEUR_CASE[0], width=2)
            identifiant_vers_case[iden - 1] = "à compléter"
            case_vers_identifiant[lig][col] = "à compléter"
            
            
    #----Horloge----
    textHorloge = StringVar()
    textHorloge.set("Chrono: {:02d}:{:02d}".format(0, 0))
    horloge = Label(fenetre, textvariable = textHorloge, bg = COULEUR_BOUTON, relief = 'raised')
    horloge.grid(row = 0, column = 1, padx = 5, pady = 5)


    
    #----Texte du joueur courant----
    textJoueur = StringVar()
    textJoueur.set("Joueur : ??")
    #----Etiquette du joueur courant----
    etiquetteJoueur = Label(fenetre, textvariable = textJoueur, bg = COULEUR_BOUTON, relief = 'raised')
    # A MODIFIER :  positionner l'étiquette avec grid
    "compléter ici"
   

    #----Bouton pour quitter----
    bouton_quitter = Button(fenetre, text="Quitter", bg = COULEUR_BOUTON, relief = 'raised',  command = quitter)
    bouton_quitter.grid(row = 2, column = 2, padx = 5, pady = 5)


    #----Bouton pour jouer----
    bouton_jouer = Button(fenetre, text="Nouvelle partie", bg = COULEUR_BOUTON, relief = 'raised',
                        command =  nouvelle_partie)
    # A MODIFIER :  positionner le bouton avec grid
    "compléter ici"

    # renvoie des widgets et des tableaux de correspondance items graphiques <-> identifiants 
    return fenetre,  textJoueur, etiquetteJoueur, bouton_quitter, bouton_jouer, textHorloge, horloge,  plateau, case_vers_identifiant, identifiant_vers_case

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#-------Partie Controleur (Gestionnaires d'événements et liaisons avec les événements)-----------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

def clic_gauche(event):
    """Gestionnaire de clic à gauche, pour le joueur 1"""
    global choix_joueur1
    #clic gauche bloqué si une nouvelle partie n'est pas lancée
    #ou s'il y  déjà un vainqueur
    if joueur == JOUEUR_1 and not choix_joueur1 and tour != 0 and vainqueur == 0:
        (iden,) = plateau.find_closest(event.x, event.y)
        (lig, col) = identifiant_vers_case[iden - 1]
        if grille[lig][col] != 0:
            showinfo("Erreur", "Case non libre")
        else:
            grille[lig][col] = joueur
            plateau.itemconfig(iden, fill = COULEUR_CASE[joueur])
            choix_joueur1 = True


def appui_touche(event):
    """Gestionnaire d'appui sur une touche, pour le joueur 2"""
    global choix_joueur2, xcurseur, ycurseur    
    if joueur == JOUEUR_2 and not choix_joueur2 and tour != 0 and vainqueur == 0:
        if event.keysym == 'Left' and xcurseur >= COTE_CASE:
            plateau.coords(curseur, xcurseur - COTE_CASE, ycurseur, xcurseur, ycurseur + COTE_CASE)
            xcurseur, ycurseur = xcurseur - COTE_CASE, ycurseur
        elif event.keysym == 'Up' and ycurseur >= COTE_CASE:
            plateau.coords(curseur, xcurseur, ycurseur - COTE_CASE, xcurseur + COTE_CASE, ycurseur)
            xcurseur, ycurseur = xcurseur, ycurseur - COTE_CASE
        #A MODIFIER : déplacement vers le bas ou la droite
        elif event.keysym == 'space':
            (lig, col) = (ycurseur//COTE_CASE, xcurseur//COTE_CASE)
            if grille[lig][col] == 0:
                iden = case_vers_identifiant[lig][col]
                grille[lig][col] = joueur
                plateau.itemconfig(iden, fill = COULEUR_CASE[joueur])
                choix_joueur2 = True
            else:
                showinfo("Erreur", "Case non libre")

#Liaisons événements/gestionnaires d'événements


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#-----------------Dernière partie : lancement de la boucle réceptionnaire d'événement------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------


# Programme principal
if __name__ == "__main__":
    fenetre,  textJoueur, etiquetteJoueur, bouton_quitter, bouton_jouer, textHorloge, horloge,  plateau, case_vers_identifiant, identifiant_vers_case = interface_jeu()
    #Liaisons événements/gestionnaires d'événements
    plateau.bind('<ButtonPress-1>', clic_gauche)
    plateau.bind_all('<KeyPress>', appui_touche)
    #boucle réceptionnaire d'événement 
    fenetre.mainloop()