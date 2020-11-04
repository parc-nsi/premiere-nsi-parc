#!/usr/bin/env python
# coding: utf-8

# In[3]:


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# ## Outils fournis

# In[1]:


def dimensions(pix):
    """Retourne les dimensions (Largeur, Hauteur) d'une matrice
    de pixels"""
    return len(pix[0]), len(pix) 

def matrice_to_image(pix, mode = '1', fichier='image.png', res=1):
    """Convertit en image  une matrice de pixels pix 
    de dimensions (ligne, colonnes)=(nline, ncol)
    en représentant sur l'écran chaque case de pix
    par un carré de coté resolution pixels.
    Le mode de l'image peut être :
    '1'  : binaire 0 ou 1
    'L' : niveaux de gris entre 0 et 255
    'RGB' : triplet de valeurs (Rouge, Vert, Bleu) entre 0 et 255
    """
    #on force la conversion en type np.uint8 si pix est un tableau numpy
    if isinstance(pix, np.ndarray):
        pix = pix.astype(np.uint8)
    #précondition 1 : list doit être une matrice de pixels
    precondition1 = isinstance(pix, (list, np.ndarray))                    and len(pix) > 0                 and all(isinstance(pix[k], (list, np.ndarray))                         and  len(pix[k]) == len(pix[0])                          for k in range(len(pix)))
    assert precondition1, "Il faut passer en paramètre une matrice de pixels"
    #dimensions de la matrice de pixels
    largeur_pix, hauteur_pix = dimensions(pix)
    #préconditions sur la matrice de pixels pour respecter les contraintes du mode de l'image 
    precondition2 =  mode == '1' and                     all(isinstance(pix[y][x], (int, np.uint8)) and 0 <= pix[y][x] <= 1                         for y in range(hauteur_pix) for x in range(largeur_pix))
    precondition3 =  mode == 'L' and                     all(isinstance(pix[y][x], (int, np.uint8)) and 0 <= pix[y][x] <= 255                         for y in range(hauteur_pix) for x in range(largeur_pix))
    precondition4 = mode == 'RGB' and                     all(isinstance(pix[y][x], (list, np.ndarray))                         and len(pix[y][x]) == 3                         and  all(isinstance(pix[y][x][k], (int, np.uint8))                                  and 0 <= pix[y][x][k] <= 255                             for k in range(3))                         for y in range(hauteur_pix) for x in range(largeur_pix))
    assert precondition2 or precondition3 or precondition4, "matrice de pixels et mode incompatibles !"    
    #dimensions de la matrice de pixels
    hauteur_newpix, largeur_newpix = res * hauteur_pix, res * largeur_pix
    #copie de pix sous forme de tableau numpy agrandi d'un coefficient res 
    if mode != 'RGB':
        newpix =  np.zeros((hauteur_newpix, largeur_newpix), dtype='uint8')
    else:
        newpix =  np.zeros((hauteur_newpix, largeur_newpix, 3), dtype='uint8')
    #initialsation des blocs de taille res * res de newpix
    #avec des 0 si pix[i][j] == 0 et 1 sinon
    for y in range(hauteur_newpix):
        for x in range(largeur_newpix):
            ypix = y // res
            xpix = x // res
            newpix[y][x] = pix[ypix][xpix]   
    if mode != 'RGB':
        #création d'un objet image PIL en mode binaire (pixel de valeur 0 ou 1)
        im = Image.new(mode, (largeur_newpix, hauteur_newpix))  #Image.new(mode, (Largeur, Hauteur))  
        #on remplit l'image avec les valeurs de newpix
        im.putdata(newpix.flatten())
    else:
        im = Image.fromarray(newpix)
    #enregistrement de l'image sur le disque
    im.save(fichier)
    #affichage de l'image
    #plt.axis('off') #to disable xticks and yticks
    #cas des images binaires 
    if mode == '1':
        plt.imshow(newpix,cmap=plt.cm.gray, vmin= 0, vmax = 1)
    # cas des images en niveaux de gris
    elif mode == 'L':
        plt.imshow(newpix,cmap=plt.cm.gray, vmin= 0, vmax = 255)
    #cas des images RGB
    else:
        plt.imshow(newpix)
        
def image_to_matrice(fichier):
    #ouverture de l'image avec PIL
    im = Image.open(fichier)
    #conversion de l'image en matrice de pixels / tableau numpy
    pix = np.array(im, dtype = np.uint8)
    #conversion de la matrice de pixels en liste Python
    pix = pix.tolist()
    return pix

def matrice_vide(ncol, nlig, mode):
    """Retourne une matrice de pixels de n lignes et m colonnes
    représentant une image noire dans le mode  d'image choisi"""
    assert mode in ['1', 'L', 'RGB'], "mode doit appartenir à ['1', 'L', 'RGB']"
    if mode in ['1', 'L']:
        "à compléter : return ...."
    else:               
        "à compléter : return ...."


# ## Exercice 2

# In[15]:


def max_tab2d(tab):
    """Retourne le maximum d'un tableau à 2 dimensions"""
    maxi = float('-inf')
    for y in range(len(tab)): #boucle sur les lignes
        for x in range(len(tab[y])): # boucle sur les colonnes
            "à compléter"


# Assertions à vérifier

# In[ ]:


assert max_tab2d([[-1,-2],[-2,-3,-0.5]]) == -0.5
assert max_tab2d([[1,2],[float('inf'),10]]) == float('inf')
assert max_tab2d([[1,2],[8,0]]) == 8


# ## Exercice 5

# In[4]:


def generer_croix(couleur):
    blanc = [255,255,255]
    ## TO DO
    #croix = à compléter
    matrice_to_image(croix, mode = 'RGB', res = 100, fichier='croix.png')  


# ## Exercice 6

# In[5]:


def drapeau_3bandes_verticales(nlig, ncol, couleur1, couleur2, couleur3):
    #on crée une matrice vide de bonnes dimensions
    pix = matrice_vide(ncol, nlig, 'RGB')
    tiers_colonne = ncol // 3
    deux_tiers_colonne = 2 * tiers_colonne
    for x in range(ncol): #boucle sur les colonnes
        for y in range(nlig): #boucle sur les lignes
            if   x < tiers_colonne:
                pix[y][x] = couleur1
            #à compléter !
    return pix

def transpose(pix, mode):
    "Retourne la transposée tpix d'une matrice de pixels pix : tpix[y][x] = pix[x][y]"
    ncol, nlig  = dimensions(pix)
    tpix = matrice_vide(nlig, ncol, mode)
    #à compléter
    return tpix


# Les assertions suivantes doivent être vérifiées par la fonction `transpose`

# In[ ]:


assert transpose([[0]],'L') == [[0]]
assert transpose([[1,2],[4,5]], 'L') == [[1,4],[2,5]]
assert transpose([[1,2,3],[4,5,6]],'L') == [[1,4],[2,5],[3,6]]
assert transpose([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]],'RGB') == [[[1,2,3],[7,8,9]],[[4,5,6],[10,11,12]]]


# ## Exercice 7

# In[ ]:


def barres_horizontales(nlig, ncol):
    """Retourne la matrice de pixels d'une image
    de dimensions ncol x nlig avec alternance 
    de lignes noires (index pair)
    ou blanches (index impair)"""
    #on crée une matrice vide de bonnes dimensions
    pix = matrice_vide(ncol, nlig)
    for x in range(ncol): #boucle sur les colonnes
        for y in range(nlig): #boucle sur les lignes
            #les lignes d'index paires seront noires
            "à compléter"
    return pix 


# ## Exercice 8

# In[9]:


def applique_filtre(pix, filtre, mode):
    ncol, nlig = dimensions(pix)
    pix_but = matrice_vide(ncol, nlig, mode)
    for x in range(ncol): #boucle sur les colonnes
        for y in range(nlig): #boucle sur les lignes
            pix_but[y][x] = filtre(pix[y][x])
    return pix_but


# ### Filtre négatif

# In[ ]:


def filtre_negatif_gris(pixel):
    """Filtre négatif pour image en niveaux de gris"""
    return 255 - pixel

def filtre_negatif_rgb(pixel):
    """Filtre négatif pour image  en RGB"""
    "à compléter"


# ### Assertion qui doit être vérifiée

# In[ ]:


assert filtre_negatif_rgb([255,0,100]) == [0,255,155]


# ### Filtre de seuillage

# In[10]:


def filtre_seuillage_gris(seuil):
    """Retourne une fonction filtre de seuillage pour une image en niveaux de gris
    et pour le seuil choisi"""    
    def f(pixel):
        return fonction_seuil(pixel, seuil, 0, 255)    
    return f


# In[ ]:


def filtre_seuillage_rgb(seuil):
    """Retourne une fonction filtre de seuillage pour une image en RGB
    et pour le seuil choisi"""
    def g(pixel):
        "à compléter"
    return g


# ### Filtre de composante

# In[11]:


def filtre_rouge(pixel):
    """Filtre un pixel RGB en le projetant sur sa composante rouge"""
    #à compléter


# Assertions à vérifier

# In[ ]:


assert filtre_rouge([255,0,0]) == [255,0,0]
assert filtre_rouge([255,255,0]) == [255,0,0]
assert filtre_rouge([255,255,255]) == [255,0,0]
assert filtre_rouge([0,255,0]) == [0,0,0]


# In[12]:


def filtre_composante_rgb(index_comp):
    """Retourne une fonction de filtre qui projette un pixel
    sur la composante indexée en paramètre"""    
    "à compléter"


# In[ ]:


assert filtre_composante_rgb(0)([255,200,100]) == [255,0,0]
assert filtre_composante_rgb(1)([255,200,100]) == [0,200,0]
assert filtre_composante_rgb(2)([255,200,100]) == [0,0,100]


# ### Filtre monochrome

# In[13]:


def filtre_monochrome(pixel_rgb):
    """Retourne la moyenne pondérée des composantes
    d'un pixel RGB par les coefs [0.299,0.587,0.114]"""
    coef = [0.299,0.587,0.114]
    pixel_gris = 0
    somme_coef = 0
    "à compléter"


# Assertions qui doivent être vérifiées

# In[ ]:


assert filtre_monochrome([255,100,200]) == 157
assert filtre_monochrome([200,255,100]) == 220
assert filtre_monochrome([100,200,255]) == 176

