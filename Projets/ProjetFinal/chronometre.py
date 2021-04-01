import tkinter as tk
import time

#Code de Pierre Duclosson

##----- Définition des Fonctions -----##

def action_depart():
    """ fonction qui receptione le clic sur le bouton Départ """
    global temps_depart, en_route
    if not en_route: 
        temps_depart = time.time() # note le temps machine dans temps_depart
    en_route = True
    evolution() # lance l'évolution de l'affichage du chrono

def evolution():
    """ fonction qui se rappelle automatiquement toute les 100ms.
        Modifie la valeur de la variable de controle texte_chrono
        en fonction du temps écoulé depuis le départ du chronomètre """
    
    # on arrive ici toutes les 100 ms
    if not en_route:
        return
    secondes = int(time.time() - temps_depart)  # nb de secondes depuis le départ
    affiche_sec = "{:02d}".format(secondes%60)  
    minutes = secondes//60
    affiche_min = "{:02d}".format(minutes%60)
    heures = minutes//60
    affiche_heure = "{:02d}".format(heures)
    affiche_temps = affiche_heure + ":" + affiche_min + ":" + affiche_sec
    texte_chrono.set(affiche_temps)
    fenetre.after(100, evolution) # provoque le rappel de la fonction après 100ms
    
def action_arret():
    """ fonction qui receptione le clic sur le bouton Arrêt """
    global en_route
    en_route = False  

# Création de la fenêtre principale

fenetre = tk.Tk()
fenetre.title("Chronomètre NSI")
fenetre.geometry("400x200")

## -------  Variables globales et variables de contrôle  -------

en_route = False  # booléen qui indique si le chronomètre est en route
texte_chrono = tk.StringVar()  # Variable de contrôle pour le texte affiché
texte_chrono.set('00:00:00')   # Initialise la valeur de texte_chrono


##------- Affichage -------##

etiquette1 = tk.Label(fenetre, textvariable = texte_chrono, font=("times", 60))
etiquette1.pack()

##----- Boutons -----##

cadre_boutons = tk.Frame(fenetre)  # cadre pour les boutons Départ et Arrêt 
cadre_boutons.pack()
bouton_depart = tk.Button(cadre_boutons, text = "  Départ  ",
                    command = action_depart, 
                    font=("sans-serif", 30))
bouton_arret= tk.Button(cadre_boutons, text = "  Arrêt  ",
                    command = action_arret, 
                    font=("sans-serif", 30))
bouton_depart.pack(side = 'left'  )
bouton_arret.pack()

##----- Programme principal -----##

fenetre.mainloop()
