#!/usr/bin/env python
# coding: utf-8

# # Prétraitement du fichier airports.csv

#%%


import csv
#j'ai remplacé tous les caractères ';' par des ',' dans le fichier source 
#le séparateur de champ est  ',' et il y a des ';' et ',' dans certaines valeurs de champs
csv_airports = open('airports.csv', encoding='utf8')
airports_reader = csv.DictReader(csv_airports, delimiter=',')
f = open('airports-reduit.csv','w')
#c = 0
for ligne in airports_reader:    
    f.write(';'.join([ligne['name'],ligne['latitude_deg'], 
                      ligne['longitude_deg'],ligne['elevation_ft'],
                      ligne['iso_country']]) + '\n')
f.close()
csv_airports.close()


# ## Exercice 1


#%%

# ouverture du fichier
f = open('communes69.csv', encoding='utf8')
# lecture du fichier ligne par ligne
for ligne in f:
    print(ligne)
#fermeture du fichier
f.close()


#%%


def fichier_vers_tab_tuple(fichier, separateur):
    """Prend en paramètres :
    - fichier de type str représentant un chemin d'accès à un fichier texte encodé en utf8
    - separateur de type str désignant le séparateur de champs sur une ligne du fichier
    Retourne un tableau de tuples, chaque tuple contenant les différents champs
    d'une ligne du fichier"""
    #on ouvre le fichier en lecture
    f = open(fichier, encoding='utf8')
    tab = []
    for ligne in f:
        #on nettoie la fin de ligne
        ligne = ligne.rstrip()
        #on découpe les champs selon le separateur
        tuple_ligne = tuple(ligne.split(separateur))
        tab.append(tuple_ligne)
    #on ferme le fichier
    f.close()
    return tab


# In[3]:


tab_tuple_communes = fichier_vers_tab_tuple('communes69.csv', ',')
assert (len(tab_tuple_communes), tab_tuple_communes[:2]) == (296, [('Affoux', '340', '3', '343'), ('Aigueperse', '246', '1', '247')])


#%%


tab_tuple_airports = fichier_vers_tab_tuple('airports-reduit.csv', ';')
assert (len(tab_tuple_airports), tab_tuple_airports[:2]) == (57302,
       [('Total Rf Heliport', '40.07080078125', '-74.93360137939453', '11', 'US'),
  ('Aero B Ranch Airport', '38.704022', '-101.473911', '3435', 'US')])


#%%Exercice 2

tab_tuple_photos = fichier_vers_tab_tuple('photos.txt', ' ')
tab_tuple_photos[0:2]



import re

def fichier_vers_tab_tuple1(fichier, separateur, regex = False):
    """Prend en paramètres :
    - fichier de type str représentant un chemin d'accès à un fichier texte
    - separateur de type str désignant le séparateur de champs sur une ligne du fichier
    Retourne un tableau de tuples, chaque tuple contenant les différents champs
    d'une ligne du fichier"""
    #on ouvre le fichier en lecture
    f = open(fichier)
    tab = []
    for ligne in f:
        #on nettoie la fin de ligne
        ligne = ligne.rstrip()
        #on découpe les champs selon le separateur
        if regex:
            tuple_ligne = tuple(re.split(separateur, ligne))
        else:
            tuple_ligne = tuple(ligne.split(separateur))
        tab.append(tuple_ligne)
    #on ferme le fichier
    f.close()
    return tab


tab_tuple_communes = fichier_vers_tab_tuple1('communes69.csv', ',')
tab_tuple_photos = fichier_vers_tab_tuple1('photos.txt', '\s+',regex=True)
tab_tuple_airports = fichier_vers_tab_tuple1('airports-reduit.csv', ';')


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
    for k in range(1, len(tab)):
        ville, pop_int, pop_ext, pop_tot = tab[k]
        pop_tot = int(pop_tot)
        if pop_tot < pop_min:
            tab_villes_min = [ville]
            pop_min = pop_tot
        elif pop_tot == pop_min:
            tab_villes_min.append(ville)
    return (pop_min, tab_villes_min)        




assert(population_minimale(tab_tuple_communes)) == (63, ['Saint-Mamert'])

#%%



def population_cumul(tab):
    """Prend en paramètres :
    - tab un tableau de tuples rassemblant les enregistrements dans 'communes69.csv'
    Retourne un tuple constitué des cumuls des populations municipale, externe
    et totale des communes 
    """
    cumul_int,cumul_ext, cumul_tot  = 0, 0, 0 
    for tuple_ligne in tab:
        ville, pop_int, pop_ext, pop_tot = tuple_ligne
        pop_int = int(pop_int)
        pop_ext = int(pop_ext)
        pop_tot = int(pop_tot)
        cumul_int,cumul_ext, cumul_tot  = cumul_int + pop_int, cumul_ext + pop_ext, cumul_tot + pop_tot
    return cumul_int, cumul_ext, cumul_tot       
    


# In[13]:


assert population_cumul(tab_tuple_communes) == (1762866, 32797, 1795663)


#%%


def population_moyenne(tab):
    """Prend en paramètres :
    - tab un tableau de tuples rassemblant les enregistrements dans 'communes69.csv'
    Retourne un tuple constitué des moyennes des populations municipale, externe
    et totale des communes
    """
    n = len(tab)
    cumul_int, cumul_ext, cumul_tot = population_cumul(tab)
    return cumul_int/n, cumul_ext/n, cumul_tot/n


# In[15]:


assert population_moyenne(tab_tuple_communes) == (5955.628378378378, 110.80067567567568, 6066.429054054054)


#%%


def population_maximale(tab):
    """Prend en paramètres :
    - tab un tableau de tuples rassemblant les enregistrements dans 'communes69.csv'
    Retourne un tuple constitué de la population maximale
    et du tableau des villes atteignant ce maximum
    """
    pop_max = -1
    tab_villes_max = []    
    for tuple_ligne in tab:
        ville, pop_int, pop_ext, pop_tot = tuple_ligne 
        pop_tot = tuple_ligne[-1]
        pop_tot = int(pop_tot)
        if pop_tot > pop_max:
            tab_villes_max = [ville]
            pop_max = pop_tot
        elif pop_tot == pop_max:
            tab_villes_max.append(ville)
    return (pop_max, tab_villes_max)        


# In[19]:


assert(population_maximale(tab_tuple_communes)) == (147940, ['Villeurbanne'])


#%%

def population_lyon(tab):
    """Prend en paramètres :
    - tab un tableau de tuples rassemblant les enregistrements dans 'communes69.csv'
    Retourne la population totale de la ville de Lyon, cumul des populations des 9
    arrondissements
    """
    pop_lyon = 0
    for tuple_ligne in tab:
        ville, pop_int, pop_ext, pop_tot = tuple_ligne 
        ville_mots = ville.split(' ')
        if "Lyon" in ville_mots and "Arrondissement" in ville_mots:
            pop_lyon = pop_lyon + int(pop_tot)
    return pop_lyon


# In[23]:


assert(population_lyon(tab_tuple_communes)) == 505094


#%% Exercice 4

# In[24]:


tab_tuple_airports = fichier_vers_tab_tuple('airports-reduit.csv', ';')


# In[25]:


def nombre_aeroports_pays(tab, pays):
    """Prend en paramètres:
    - tab un tableau de tuples rassemblant tous les enregistrements contenus dans airports-reduit.csv
    - pays de type str correspondant au code ISO d'un pays
    Retourne un tuple constitué du pays et du  nombre d'aéroports pour ce pays"""
    nb_airport = 0
    for tuple_ligne in tab:
        code_pays = tuple_ligne[4]
        if code_pays != '' and code_pays == pays:
            nb_airport = nb_airport + 1
    return nb_airport


# In[26]:


assert nombre_aeroports_pays(tab_tuple_airports, 'US') == 23260
assert nombre_aeroports_pays(tab_tuple_airports, 'FR') == 893


# In[30]:


def metre_to_pied(metre):
    """Prend en paramètre :
    - metre de type float ou int
    Retourn la conversion en pieds de metre, de type float
    """
    return metre / 0.3048


# In[33]:


def filtre_altmin_aeroports(tab, altmin):
    """Prend en paramètres:
    - tab un tableau de tuples rassemblant tous les enregistrements contenus dans airports-reduit.csv
    - altmin une altitude minimale en mètres
    Retourne  un tuple constitué de altmin en pieds et du nombre d'aéroports d'altitude >= altmin"""
    nb_airport = 0
    altmin = metre_to_pied(altmin)
    for tuple_ligne in tab:
        alt = tuple_ligne[3]
        if alt != '' and float(alt) >= altmin:
            nb_airport = nb_airport + 1
    return altmin, nb_airport    


# In[36]:


filtre_altmin_aeroports(tab_tuple_airports, 1000)


# In[37]:


assert filtre_altmin_aeroports(tab_tuple_airports, 1000) == (3280.839895013123, 4996)


# In[38]:


def filtre_altmax_aeroport(tab, latmin):
    """Prend en paramètres:
    - tab un tableau de tuples rassemblant tous les enregistrements contenus dans airports-reduit.csv
    - latmin une latitude minimale
    Retourne un tuple constitué de latmax, altmax, tab_nom
    où altmax est l'altitude maximale en mètres d'un aeroport de latitude > latmin
    latmax est sa latitude
    et tab_nom le tableau des noms des aéroports atteignant ce maximum"""
    altmax = -1
    latmax = -100
    tab_nom = []
    for tuple_ligne in tab:
        nom, lat, alt = tuple_ligne[0], tuple_ligne[1], tuple_ligne[3]
        if nom != '' and lat != '' and alt != '' and float(lat) >= latmin:
            alt = float(alt)
            if altmax < alt:
                altmax = alt
                latmax = float(lat)
                tab_nom = [nom]
            elif altmax == alt:
                tab_nom.append(nom)
    return (latmax, altmax * 0.3048, tab_nom)


# On obtient un résultat bizarre pour l'aéroport d'altitude maximal : altitude supérieure à celle du Mont Everest et quasiment la latitude du pole nord

# In[41]:


assert filtre_altmax_aeroport(tab_tuple_airports, -90) == (89.999845, 9136.9896, ['Modi'])

