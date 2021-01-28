#!/usr/bin/env python
# coding: utf-8

#%% Exercice 1

# ouverture du fichier
f = open('communes69.csv', encoding = 'utf8')
# lecture du fichier ligne par ligne
for ligne in f:
    print(ligne)
#fermeture du fichier
f.close()

#%% 

def fichier_vers_tab_tuple(fichier, separateur):
    """Prend en paramètres :
    - fichier de type str représentant un chemin d'accès à un fichier texte
    - separateur de type str désignant le séparateur de champs sur une ligne du fichier
    Retourne un tableau de tuples, chaque tuple contenant les différents champs
    d'une ligne du fichier"""
    #on ouvre le fichier en lecture
    f = open(fichier, encoding = 'utf8')
    tab = []
    for ligne in f:
        #on nettoie la fin de ligne
        ligne = "à compléter"
        #on découpe les champs selon le separateur
        tuple_ligne = tuple(ligne.split(separateur))
        tab.append("à compléter")
    #on ferme le fichier
    f.close()
    return tab



tab_tuple_communes = fichier_vers_tab_tuple('communes69.csv', ',')
assert (len(tab_tuple_communes), tab_tuple_communes[:2]) == (296, [('Affoux', '340', '3', '343'), ('Aigueperse', '246', '1', '247')])

#%% 
tab_tuple_airports = fichier_vers_tab_tuple('airports-reduit.csv', ';')
assert (len(tab_tuple_airports), tab_tuple_airports[:2]) == (57302,
       [('Total Rf Heliport', '40.07080078125', '-74.93360137939453', '11', 'US'),
  ('Aero B Ranch Airport', '38.704022', '-101.473911', '3435', 'US')])

#%% Exercice 2

#%% Exercice 3


def population_minimale(tab):
    """Prend en paramètres :
    - tab un tableau de tuples rassemblant les enregistrements dans 'communes69.csv'
    Retourne un tuple constitué de la population minimale
    et du tableau des villes atteignant ce minimum
    """     
    ville1, pop_int1, pop_ext1, pop_tot1 = tab[0]
    pop_min = int(pop_tot1)
    tab_villes_min = [ville1]    
    "à compléter"
    return (pop_min, tab_villes_min)      




assert(population_minimale(tab_tuple_communes)) == (63, ['Saint-Mamert'])


def population_cumul(tab):
    """Prend en paramètres :
    - tab un tableau de tuples rassemblant les enregistrements dans 'communes69.csv'
    Retourne un tuple constitué des cumuls des populations municipale, externe
    et totale des communes 
    """
    cumul_int,cumul_ext, cumul_tot  = 0, 0, 0 
    "à compléter"



assert population_moyenne(tab_tuple_communes) == (5955.628378378378, 110.80067567567568, 6066.429054054054)



def population_moyenne(tab):
    """Prend en paramètres :
    - tab un tableau de tuples rassemblant les enregistrements dans 'communes69.csv'
    Retourne un tuple constitué des moyennes des populations municipale, externe
    et totale des communes
    """



assert population_moyenne(tab_tuple_communes) == (5955.628378378378, 110.80067567567568, 6066.429054054054)



def population_lyon(tab):
    """Prend en paramètres :
    - tab un tableau de tuples rassemblant les enregistrements dans 'communes69.csv'
    Retourne la population totale de la ville de Lyon, cumul des populations des 9
    arrondissements
    """


assert(population_lyon(tab_tuple_communes)) == 505094



def population_maximale(tab):
    """Prend en paramètres :
    - tab un tableau de tuples rassemblant les enregistrements dans 'communes69.csv'
    Retourne un tuple constitué de la population maximale
    et du tableau des villes atteignant ce maximum
    """  
    pop_max = -1
    tab_villes_max = []    
    "à compléter"
    return (pop_max, tab_villes_max) 



assert(population_maximale(tab_tuple_communes)) == (147940, ['Villeurbanne'])


## Exercice 4



def nombre_aeroports_pays(tab, pays):
    """Prend en paramètres:
    - tab un tableau de tuples rassemblant tous les enregistrements contenus dans airports-reduit.csv
    - pays de type str correspondant au code ISO d'un pays
    Retourne un tuple constitué du pays et du  nombre d'aéroports pour ce pays"""
    nb_airport = 0
    for tuple_ligne in tab:
        code_pays = tuple_ligne[4]
        if code_pays != '' and code_pays == pays:
            nb_airport = "à compléter"
    return nb_airport




def filtre_altmin_aeroports(tab, altmin):
    """Prend en paramètres:
    - tab un tableau de tuples rassemblant tous les enregistrements contenus dans airports-reduit.csv
    - altmin une altitude minimale en mètres
    Retourne  un tuple constitué de altmin et du nombre d'aéroports d'altitude >= altmin"""




assert filtre_altmin_aeroports(tab_tuple_airports, 1000) == (3280.839895013123, 4996)





def filtre_altmax_aeroport(tab, latmin):
    """Prend en paramètres:
    - tab un tableau de tuples rassemblant tous les enregistrements contenus dans airports-reduit.csv
    - latmin une latitude minimale
    Retourne un tuple constitué de latmin, altmax, tab_nom
    où altmax est l'altitude maximale en mètres d'un aeroport de latitude > latmin
    et tab_nom le tableau des noms des aéroports atteignant ce maximum"""


assert filtre_altmax_aeroport(tab_tuple_airports, -90) == (89.999845, 9136.9896, ['Modi'])

