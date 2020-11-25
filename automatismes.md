---
title:  Automatismes
layout: parc
---



>L'image `gif` ci-dessous présente  différentes étapes du déroulement d'un algorithme de rotation d'images inspiré d'un travail présenté par Laurent Abbal du lycée français de Tokyo. Le  programme assez court peut être réalisé par un élève  de terminale (récursivité, approche _diviser pour régner_).
>L'image source représente l'oeuvre _Matsuri Yatai Dragon_ du peintre japonais [Hokusai](https://en.wikipedia.org/wiki/en:Hokusai). Elle est dans le domaine public et disponible sur [https://commons.wikimedia.org](https://commons.wikimedia.org/wiki/File:Hokusai_Dragon.jpg).

[![Dragon](rotation-dragon-2.gif "dragon-hokusai")](https://commons.wikimedia.org/wiki/File:Hokusai_Dragon.jpg)


## Automatismes :


1. **Automatisme n° 1 :**  programmer la fonction dont on donne la spécification :

~~~python
def index_min(t):
    """
    Paramètre : t un tableau de nombres (int ou float)
    Précondition : t non vide
    Valeur renvoyée : un tableau contenant les positions (index) où le minimum de t est atteint
    """
~~~

2.  **Automatisme n° 2 :**  programmer la fonction dont on donne la spécification :

~~~python
def au_moins_un_zero(t):
    """
    Paramètre : t un tableau de nombres (int ou float)
    Précondition : t non vide
    Valeur renvoyée : un booléen indiquant si t contient au moins un zéro
    """
~~~

3. **Automatisme 3 :** Représenter en binaire le nombre d’écriture décimale 49.

4. **Automatisme 4 :**  Représenter en base dix, le nombre dont l'écriture en base deux est `1010110` puis le nombre dont l'écriture en base 16 est `A4`.

5. **Automatisme 5 :**  Déterminer le successeur  des entiers dont l'écriture en base deux est :
   * 111
   * 10011
   * 10111
 
6. **Automatisme 6 :**  Pour déterminer la liste des chiffres en base dix d'un entier naturel, un élève a écrit la fonction ci-dessous :

~~~python
def liste_chiffres(n):
    L = [n % 10]
    while n > 0:
        n = n // 10
        L.insert(0, n % 10)
    return L
~~~

Malheureusement sa fonction ne retourne pas le résultat attendu pour l'entier 730 :

~~~
>>> liste_chiffres(730)
[0, 7, 3, 0]
~~~

Proposer une version corrigée de la fonction `liste_chiffres`.

7. **Automatisme 7 :**

On travaille sur des tableaux à deux dimensions qui représentent des images binaires : un pixel a pour valeur un entier : 0 pour un pixel noir et 1 pour un pixel blanc.

Compléter les fonctions ci-dessous en respectant leurs spécifications, les postconditions doivent être vérifiées.

[Lien vers Basthon pour tester en ligne](https://python.infobrisson.fr/?script=def%2520image_noire%2528largeur%252C%2520hauteur%2529%253A%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520Param%25C3%25A8tre%2520%253A%2520%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520largeur%2520et%2520hauteur%2520deux%2520entiers%2520non%2520nuls%250D%250A%2520%2520%2520%2520Valeur%2520renvoy%25C3%25A9e%2520%253A%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520un%2520tableau%2520%25C3%25A0%25202%2520dimensions%2520repr%25C3%25A9sentant%2520une%2520image%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520binaire%2520de%2520dimensions%2520%2528largeur%252C%2520hauteur%2529%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520rempli%2520de%25200%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520%2523%2520%25C3%25A0%2520compl%25C3%25A9ter%2520avec%2520un%2520tableau%2520en%2520compr%25C3%25A9hension%250D%250A%2520%2520%2520%2520%250D%250Adef%2520dimensions%2528tab%2529%253A%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520Param%25C3%25A8tre%2520%253A%2520%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520tab%2520un%2520tableau%2520%25C3%25A0%2520deux%2520dimensions%2520d%27entiers%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520repr%25C3%25A9sentant%2520une%2520image%2520binaire%2520rectangulaire%250D%250A%2520%2520%2520%2520Valeur%2520renvoy%25C3%25A9e%2520%253A%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520un%2520tableau%2520de%2520deux%2520entiers%2520%255Blargeur%252C%2520hauteur%255D%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520repr%25C3%25A9sentant%2520les%2520dimensions%2520de%2520l%27image%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520%2523%2520%25C3%25A0%2520compl%25C3%25A9ter%250D%250A%2520%2520%2520%2520%250D%250Adef%2520nombre_blancs%2528tab%2529%253A%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520Param%25C3%25A8tre%2520%253A%2520%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520tab%2520un%2520tableau%2520%25C3%25A0%2520deux%2520dimensions%2520d%27entiers%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520repr%25C3%25A9sentant%2520une%2520image%2520binaire%2520rectangulaire%250D%250A%2520%2520%2520%2520Valeur%2520renvoy%25C3%25A9e%2520%253A%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520un%2520entier%2520repr%25C3%25A9sentant%2520le%2520nombre%2520de%2520pixels%2520%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520blancs%2520%2528valeur%25201%2529%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520%2523%2520%25C3%25A0%2520compl%25C3%25A9ter%250D%250A%250D%250A%2523postconditions%2520pour%2520la%2520fonction%2520image_noire%2520%250D%250Aassert%2520image_noire%25282%252C1%2529%2520%253D%253D%2520%255B%255B0%252C0%255D%255D%250D%250Aassert%2520image_noire%25281%252C2%2529%2520%253D%253D%2520%255B%255B0%255D%252C%2520%255B0%255D%255D%250D%250Aassert%2520image_noire%25283%252C2%2529%2520%253D%253D%2520%255B%255B0%252C0%252C0%255D%252C%2520%255B0%252C0%252C0%255D%255D%250D%250A%250D%250A%250D%250A%2523postconditions%2520pour%2520la%2520fonction%2520dimensions%2520%250D%250Aassert%2520dimensions%2528%255B%255B%255D%252C%2520%255B%255D%255D%2529%2520%253D%253D%2520%255B2%252C0%255D%250D%250Aassert%2520dimensions%2528%255B%255B0%252C1%252C2%255D%252C%2520%255B3%252C4%252C5%255D%255D%2529%2520%253D%253D%2520%255B2%252C3%255D%250D%250A%250D%250A%2523postconditions%2520pour%2520la%2520fonction%2520nombre_blancs%250D%250Aassert%2520nombre_blancs%2528%255B%255B0%252C0%255D%252C%2520%255B0%252C0%255D%255D%2529%2520%253D%253D%25200%250D%250Aassert%2520dimensions%2528%255B%255B0%252C1%252C1%255D%252C%2520%255B0%252C1%252C0%255D%255D%2529%2520%253D%253D%25203%250D%250Aassert%2520dimensions%2528%255B%255B%255D%252C%2520%255B%255D%255D%2529%2520%253D%253D%25200).

~~~python
def image_noire(largeur, hauteur):
    """
    Paramètre : 
        largeur et hauteur deux entiers non nuls
    Valeur renvoyée :
        un tableau à 2 dimensions représentant une image
        binaire de dimensions (largeur, hauteur)
        rempli de 0
    """
    # à compléter avec un tableau en compréhension
    
def dimensions(tab):
    """
    Paramètre : 
        tab un tableau à deux dimensions d'entiers
        représentant une image binaire rectangulaire
    Valeur renvoyée :
        un tableau de deux entiers [largeur, hauteur]
        représentant les dimensions de l'image
    """
    # à compléter
    
def nombre_blancs(tab):
    """
    Paramètre : 
        tab un tableau à deux dimensions d'entiers
        représentant une image binaire rectangulaire
    Valeur renvoyée :
        un entier représentant le nombre de pixels 
        blancs (valeur 1)
    """
    # à compléter

#postconditions pour la fonction image_noire 
assert image_noire(2,1) == [[0,0]]
assert image_noire(1,2) == [[0], [0]]
assert image_noire(3,2) == [[0,0,0], [0,0,0]]


#postconditions pour la fonction dimensions 
assert dimensions([[], []]) == [2,0]
assert dimensions([[0,1,2], [3,4,5]]) == [2,3]

#postconditions pour la fonction nombre_blancs
assert nombre_blancs([[0,0], [0,0]]) == 0
assert dimensions([[0,1,1], [0,1,0]]) == 3
assert dimensions([[], []]) == 0
~~~