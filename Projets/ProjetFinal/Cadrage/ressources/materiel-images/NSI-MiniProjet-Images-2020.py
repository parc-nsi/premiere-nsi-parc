#!/usr/bin/env python
# coding: utf-8




from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


## Outils fournis


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
        return [[0 for x in range(ncol)] for y in range(nlig)]
    else:               
        return [[[0,0,0] for x in range(ncol)] for y in range(nlig)]
