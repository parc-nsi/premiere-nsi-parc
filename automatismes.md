---
title:  Automatismes
layout: parc
---



>L'image `gif` ci-dessous présente  différentes étapes du déroulement d'un algorithme de rotation d'images inspiré d'un travail présenté par Laurent Abbal du lycée français de Tokyo. Le  programme assez court peut être réalisé par un élève  de terminale (récursivité, approche _diviser pour régner_).
>L'image source représente l'oeuvre _Matsuri Yatai Dragon_ du peintre japonais [Hokusai](https://en.wikipedia.org/wiki/en:Hokusai). Elle est dans le domaine public et disponible sur [https://commons.wikimedia.org](https://commons.wikimedia.org/wiki/File:Hokusai_Dragon.jpg).

[![Dragon](rotation-dragon-2.gif "dragon-hokusai")](https://commons.wikimedia.org/wiki/File:Hokusai_Dragon.jpg)


__[Corrigé des automatismes](automatismes/automatismes.py)__

## Automatisme 1

Programmer la fonction dont on donne la spécification :

~~~python
def index_min(t):
    """
    Paramètre : t un tableau de nombres (int ou float)
    Précondition : t non vide
    Valeur renvoyée : un tableau contenant les positions (index) où le minimum de t est atteint
    """
~~~

## Automatisme 2 

Programmer la fonction dont on donne la spécification :

~~~python
def au_moins_un_zero(t):
    """
    Paramètre : t un tableau de nombres (int ou float)
    Précondition : t non vide
    Valeur renvoyée : un booléen indiquant si t contient au moins un zéro
    """
~~~

## Automatisme 3

Représenter en binaire le nombre d’écriture décimale 49.

## Automatisme 4

Représenter en base dix, le nombre dont l'écriture en base deux est `1010110` puis le nombre dont l'écriture en base 16 est `A4`.

## Automatisme 5 

Déterminer le successeur  des entiers dont l'écriture en base deux est :

* 111
* 10011
* 10111
 
## Automatisme 6  

Pour déterminer la liste des chiffres en base dix d'un entier naturel, un élève a écrit la fonction ci-dessous :

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

## Automatisme 7 

On travaille sur des tableaux à deux dimensions qui représentent des images binaires : un pixel a pour valeur un entier : 0 pour un pixel noir et 1 pour un pixel blanc.

Compléter les fonctions ci-dessous en respectant leurs spécifications, les postconditions doivent être vérifiées.

[Lien vers Basthon pour tester en ligne](https://python.infobrisson.fr/?script=def%2520image_noire%2528largeur%252C%2520hauteur%2529%253A%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520Param%25C3%25A8tre%2520%253A%2520%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520largeur%2520et%2520hauteur%2520deux%2520entiers%2520non%2520nuls%250D%250A%2520%2520%2520%2520Valeur%2520renvoy%25C3%25A9e%2520%253A%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520un%2520tableau%2520%25C3%25A0%25202%2520dimensions%2520repr%25C3%25A9sentant%2520une%2520image%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520binaire%2520de%2520dimensions%2520%2528largeur%252C%2520hauteur%2529%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520rempli%2520de%25200%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520%2523%2520%25C3%25A0%2520compl%25C3%25A9ter%2520avec%2520un%2520tableau%2520en%2520compr%25C3%25A9hension%250D%250A%2520%2520%2520%2520%250D%250Adef%2520dimensions%2528tab%2529%253A%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520Param%25C3%25A8tre%2520%253A%2520%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520tab%2520un%2520tableau%2520%25C3%25A0%2520deux%2520dimensions%2520d%27entiers%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520repr%25C3%25A9sentant%2520une%2520image%2520binaire%2520rectangulaire%250D%250A%2520%2520%2520%2520Valeur%2520renvoy%25C3%25A9e%2520%253A%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520un%2520tableau%2520de%2520deux%2520entiers%2520%255Blargeur%252C%2520hauteur%255D%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520repr%25C3%25A9sentant%2520les%2520dimensions%2520de%2520l%27image%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520%2523%2520%25C3%25A0%2520compl%25C3%25A9ter%250D%250A%2520%2520%2520%2520%250D%250Adef%2520nombre_blancs%2528tab%2529%253A%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520Param%25C3%25A8tre%2520%253A%2520%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520tab%2520un%2520tableau%2520%25C3%25A0%2520deux%2520dimensions%2520d%27entiers%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520repr%25C3%25A9sentant%2520une%2520image%2520binaire%2520rectangulaire%250D%250A%2520%2520%2520%2520Valeur%2520renvoy%25C3%25A9e%2520%253A%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520un%2520entier%2520repr%25C3%25A9sentant%2520le%2520nombre%2520de%2520pixels%2520%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520blancs%2520%2528valeur%25201%2529%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520%2523%2520%25C3%25A0%2520compl%25C3%25A9ter%250D%250A%250D%250A%2523postconditions%2520pour%2520la%2520fonction%2520image_noire%2520%250D%250Aassert%2520image_noire%25282%252C1%2529%2520%253D%253D%2520%255B%255B0%252C0%255D%255D%250D%250Aassert%2520image_noire%25281%252C2%2529%2520%253D%253D%2520%255B%255B0%255D%252C%2520%255B0%255D%255D%250D%250Aassert%2520image_noire%25283%252C2%2529%2520%253D%253D%2520%255B%255B0%252C0%252C0%255D%252C%2520%255B0%252C0%252C0%255D%255D%250D%250A%250D%250A%250D%250A%2523postconditions%2520pour%2520la%2520fonction%2520dimensions%2520%250D%250Aassert%2520dimensions%2528%255B%255B%255D%252C%2520%255B%255D%255D%2529%2520%253D%253D%2520%255B0%252C2%255D%250D%250Aassert%2520dimensions%2528%255B%255B0%252C1%252C2%255D%252C%2520%255B3%252C4%252C5%255D%255D%2529%2520%253D%253D%2520%255B3%252C2%255D%250D%250A%250D%250A%2523postconditions%2520pour%2520la%2520fonction%2520nombre_blancs%250D%250Aassert%2520nombre_blancs%2528%255B%255B0%252C0%255D%252C%2520%255B0%252C0%255D%255D%2529%2520%253D%253D%25200%250D%250Aassert%2520nombre_blancs%2528%255B%255B0%252C1%252C1%255D%252C%2520%255B0%252C1%252C0%255D%255D%2529%2520%253D%253D%25203%250D%250Aassert%2520nombre_blancs%2528%255B%255B%255D%252C%2520%255B%255D%255D%2529%2520%253D%253D%25200).

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

## Automatisme 8

Modifier les expressions "à modifier"  dans la fonction Python ci-dessous pour que la spécification soit vérifiée.

Tester le code dans [Basthon](https://python.infobrisson.fr/?script=%2523%2520Fonction%2520de%2520tri%2520dans%2520l%27ordre%2520croissant%2520par%2520s%25C3%25A9lection%2520du%2520maximum%250D%250A%250D%250Adef%2520indice_maximum%2528tab%252C%2520debut%252C%2520fin%2529%253A%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520Param%25C3%25A8tres%2520%253A%2520%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520tab%2520un%2520tableau%2520d%27entiers%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520debut%2520un%2520entier%2520indice%2520du%2520d%25C3%25A9but%2520de%2520la%2520plage%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520fin%2520un%2520entier%2520indice%2520de%2520la%2520fin%2520de%2520la%2520plage%2520%2528inclus%2529%250D%250A%2520%2520%2520%2520Valeur%2520renvoy%25C3%25A9e%2520%253A%2520l%27indice%2520de%2520la%2520premi%25C3%25A8re%2520occurence%2520du%2520maximum%2520de%2520tab%2520%250D%250A%2520%2520%2520%2520dans%2520la%2520plage%2520%2520de%2520valeurs%2520entre%2520les%2520indice%2520et%2520debut%2520et%2520fin%2520%2528inclus%2529%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520imax%2520%253D%2520%2522%25C3%25A0%2520modifier%2522%250D%250A%2520%2520%2520%2520for%2520i%2520in%2520range%2528debut%2520%252B%25201%252C%2520fin%2520%252B%25201%2529%253A%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520if%2520%2522%25C3%25A0%2520modifier%2522%253A%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520imax%2520%253D%2520%2522%25C3%25A0%2520modifier%2522%250D%250A%2520%2520%2520%2520return%2520imax%250D%250A%2520%2520%2520%2520%250D%250A%2520%2520%2520%2520%250D%250Adef%2520tri_selection%2528tab%2529%253A%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520Param%25C3%25A8tre%2520%253A%2520tab%2520un%2520tableau%2520de%2520nombres%250D%250A%2520%2520%2520%2520Valeur%2520renvoy%25C3%25A9e%2520%253A%2520tab%250D%250A%2520%2520%2520%2520Postcondition%2520%253A%2520valeur%2520renvoy%25C3%25A9e%2520de%2520tab%2520tri%25C3%25A9e%2520dans%2520l%27ordre%2520croissant%250D%250A%2520%2520%2520%2520%2522%2522%2522%250D%250A%2520%2520%2520%2520i%2520%253D%2520len%2528tab%2529%2520-%25201%250D%250A%2520%2520%2520%2520while%2520i%2520%253E%253D%25201%253A%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520imax%2520%253D%2520indice_maximum%2528tab%252C%2520%2522%25C3%25A0%2520modifier%2522%252C%2520%2522%25C3%25A0%2520modifier%2522%2529%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520tab%255Bi%255D%252C%2520tab%255Bimax%255D%2520%253D%2520%2520%2522%25C3%25A0%2520modifier%2522%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2523%2520assertion%2520qui%2520doit%2520%25C3%25AAtre%2520v%25C3%25A9rifi%25C3%25A9e%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520assert%2520max%2528tab%255B%253Ai%252B1%255D%2529%2520%253D%253D%2520tab%255Bi%255D%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520i%2520%253D%2520%2522%25C3%25A0%2520modifier%2522%250D%250A%2520%2520%2520%2520return%2520tab%2520%250D%250A%2520%2520%2520%2520%250D%250A%2523%2520Tests%2520unitaires%250D%250A%250D%250Aimport%2520random%250D%250A%250D%250A%250D%250Adef%2520test_indice_maximum%2528fonction_indice_maximum%2529%253A%250D%250A%2520%2520%2520%2520%2523tableaux%2520al%25C3%25A9atoires%250D%250A%2520%2520%2520%2520for%2520size%2520in%2520range%25281%252C%252010%2529%253A%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520tab%2520%253D%2520%255Brandom.randint%25280%252C%2520100%2529%2520for%2520_%2520in%2520range%2528size%2529%255D%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520assert%2520fonction_indice_maximum%2528tab%252C%25200%252C%2520len%2528tab%2529%2520-%25201%2529%2520%253D%253D%2520tab.index%2528max%2528tab%2529%2529%250D%250A%2520%2520%2520%2520print%2528f%2522Tests%2520unitaires%2520r%25C3%25A9ussis%2520pour%2520%257Bfonction_indice_maximum.__name__%257D%2522%2529%250D%250A%2520%2520%2520%2520%250D%250Adef%2520test_tri%2528fonction_tri%2529%253A%250D%250A%2520%2520%2520%2520%2522%2522%2522Test%2520unitaire%2520d%27une%2520fonction%2520de%2520tri%2522%2522%2522%250D%250A%2520%2520%2520%2520%2523tableaux%2520d%25C3%25A9j%25C3%25A0%2520tri%25C3%25A9s%250D%250A%2520%2520%2520%2520for%2520size%2520in%2520range%25280%252C%252010%2529%253A%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520tab%2520%253D%2520list%2528range%25280%252C%2520size%2529%2529%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520assert%2520fonction_tri%2528tab%2529%2520%253D%253D%2520sorted%2528tab%2529%252C%2520f%2522echec%2520sur%2520%257Btab%257D%2522%250D%250A%2520%2520%2520%2520%2523tableaus%2520tri%25C3%25A9s%2520dans%2520l%27ordre%2520inverse%250D%250A%2520%2520%2520%2520for%2520size%2520in%2520range%25280%252C%252011%2529%253A%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520tab%2520%253D%2520list%2528range%25289%2520-%2520size%252C%2520-1%252C%2520-1%2529%2529%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520assert%2520fonction_tri%2528tab%2529%2520%253D%253D%2520sorted%2528tab%2529%252C%2520f%2522echec%2520sur%2520%257Btab%257D%2522%250D%250A%2520%2520%2520%2520%2523tableaux%2520al%25C3%25A9atoires%250D%250A%2520%2520%2520%2520for%2520size%2520in%2520range%25280%252C%252010%2529%253A%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520tab%2520%253D%2520%255Brandom.randint%25280%252C%2520100%2529%2520for%2520_%2520in%2520range%2528size%2529%255D%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520assert%2520fonction_tri%2528tab%2529%2520%253D%253D%2520sorted%2528tab%2529%252C%2520f%2522echec%2520sur%2520%257Btab%257D%2522%250D%250A%2520%2520%2520%2520print%2528f%2522Tests%2520unitaires%2520r%25C3%25A9ussis%2520pour%2520%257Bfonction_tri.__name__%257D%2522%2529%250D%250A%250D%250A%2523d%25C3%25A9sactiver%2520pour%2520effectuer%2520les%2520tests%2520unitaire%2520%2520%2520%2520%2520%2520%250D%250A%2523test_indice_maximum%2528indice_maximum%2529%250D%250A%2523test_tri%2528tri_selection%2529)

Décommenter  `#test_indice_maximum(indice_maximum)`  en ligne 63 pour soumettre votre fonction au test unitaire. 


~~~python
def indice_maximum(tab, debut, fin):
    """
    Paramètres : 
        tab un tableau d'entiers
        debut un entier indice du début de la plage
        fin un entier indice de la fin de la plage (inclus)
    Valeur renvoyée : l'indice de la première occurence du maximum de tab 
    dans la plage  de valeurs entre les indice et debut et fin (inclus)
    """
    imax = "à modifier"
    for i in range(imax + 1, fin + 1):
        if "à modifier":
            imax = "à modifier"
    return imax
~~~


## Automatisme 9

Modifier les expressions "à modifier" dans la fonction `tri_selection` ci-dessous pour que la spécification et l'assertion placée à la fin de la boucle externe soient vérifiés.

~~~python
def tri_selection(tab):
    """
    Paramètre : tab un tableau de nombres
    Valeur renvoyée : tab
    Postcondition : valeur renvoyée de tab triée dans l'ordre croissant
    """
    i = len(tab) - 1
    while i >= 1:
        imax = indice_maximum(tab, "à modifier", "à modifier")
        tab[i], tab[imax] =  "à modifier"
        # assertion qui doit être vérifiée
        assert max(tab[:i+1]) == tab[i]
        i = "à modifier"
    return tab 
~~~

Décommenter  `#test_tri(tri_selection)`  en ligne 64 pour soumettre votre fonction au test unitaire. 


## Automatisme 10

Un algorithme de tri d’une liste d’entiers est implémenté  de la façon suivante : 

~~~python
def trier(L) : 
    for i in range(len(L)): 
        indice_min = i 
        for j in range(i+1, len(L)): 
            if L[j] < L[indice_min] : 
                indice_min = j 
        L[i], L[indice_min] = L[indice_min], L[i] 
        # assertion vraie à cet endroit 
    return L 
~~~

Parmi les assertions suivantes laquelle reste vraie à chaque itération de la boucle, à l'endroit indiqué ci-dessus ?

* __Réponse A :__ la sous-liste `L[0:i+1]` contient les `i` plus grandes valeurs de `L` triées par ordre décroissant
* __Réponse B :__  la sous-liste `L[0:i+1]` contient les `i` plus grandes valeurs de `L` triées par ordre croissant
* __Réponse C :__  la sous-liste `L[0:i+1]` contient les i plus petites valeurs de `L` triées par ordre décroissant
* __Réponse D :__ la sous-liste `L[0:i+1]` contient les i plus petites valeurs de L triées par ordre croissant


## Automatisme 11

* Compléter la fonction Python ci-dessous pour que  la spécification et les postconditions soient satisfaites.
* Combient de comparaisons sont faites lors de l'appel `un_doublon(list(range(100)))` ?


~~~python
def un_doublon(t):
    """
    Paramètre : t un tableau de nombres
    Valeur renvoyée : un booléen 
        True si t comporte au moins un doublon
        False sinon
    """
    #à compléter

assert un_doublon([1, 2, 3]) == False
assert un_doublon([1, 2, 2]) == True
assert un_doublon([1, 2, 4, 2]) == True
assert un_doublon([]) == False
~~~

## Automatisme 12

* Compléter la fonction Python ci-dessous pour que  la spécification et les postconditions soient satisfaites.

~~~python
def index_premiere_occurence_dicho(x, t):
    """
    Paramètre : 
        t un tableau de nombres trié dans l'ordre croissant
        x un nombre 
    Valeur renvoyée : 
        l'index de la première de x dans t si x est dans t
        -1 sinon
    """
    a = 0
    b = len(t) - 1
    while a <= b:
        m = (a + b) // 2
        if t[m] < x:
            "à compléter"
        elif t[m] > x:
            "à compléter"
        else:
            "à compléter"
            return "à compléter"
    return -1

assert index_premiere_occurence_dicho(10, [10, 10, 11, 12, 13]) == 1
assert index_premiere_occurence_dicho(10, [9, 10, 11, 12, 13]) == 1
assert index_premiere_occurence_dicho(10, [9, 9, 11, 12, 13]) == -1
assert index_premiere_occurence_dicho(10, [7, 8, 9, 10]) == 3 
assert index_premiere_occurence_dicho(10, [7, 10, 10,  10, 10]) == 1 
assert index_premiere_occurence_dicho(10, []) == -1
~~~


## Automatisme 13

* Compléter la fonction Python ci-dessous pour que  la spécification et les postconditions soient satisfaites.

~~~python
def est_decroissant(t):
    """
    Paramètre : 
        t un tableau de nombres 
    Valeur renvoyée : 
        booléen indiquant si t dans l'ordre décroissant
    """
    "à compléter"


def recherche_dicho_decroissant(x, t):
    """
    Paramètre : 
        t un tableau de nombres trié dans l'ordre décroissant
        x un nombre 
    Valeur renvoyée : 
        index de x dans t si x dans t
        None si x pas dans t
    """
    a = 0
    b = len(t) - 1
    while a <= b:
        m = (a + b) // 2
        "à compléter"
    return None

assert est_decroissant([k ** 2 for k in range(10)]) == False
assert est_decroissant([]) == True
t1 = list(range(10, -1, -1))
assert est_decroissant(t1) == True
assert recherche_dicho_decroissant(8, t1) == 2
assert recherche_dicho_decroissant(10, t1) == 0
assert recherche_dicho_decroissant(0, t1) == 10
assert recherche_dicho_decroissant(4.5, t1) == None
print("Test unitaires réussis pour l'automatisme 13 : recherche_dicho_decroissant et est_decroissant")
~~~


## Automatisme 14

* Convertir en flottant au format simple précision (mantisse sur 8 bits et exposant sur 23 bits), le nombre  d'écriture décimale 9,78125.
* Convertir en flottant au format simple précision (mantisse sur 8 bits et exposant sur 23 bits), le nombre  d'écriture décimale 0,1.
* Vérifier avec le convertisseur en ligne <https://www.h-schmidt.net/FloatConverter/IEEE754.html> ou la fonction donnée ci-dessous :

~~~python
def decimal_vers_IEE754(x, taille_exposant, taille_mantisse):
    #print("détermination du signe")
    if x > 0:
        print("Bit de signe  : 0")
    elif x <0:
        print("Bit de signe : 1")
    else:
        print("O valeur particulière")
    if x != 0:
        #print("détermination de l'exposant")
        exposant = 0
        while int(x) >= 1:
            x = x / 2
            exposant = exposant + 1
        while int(x) == 0:
            x = x * 2
            exposant = exposant - 1           
        decalage = 2 ** (taille_exposant - 1) - 1
        print("Exposant en décimal : ", exposant)
        print(f"Exposant décalé  de  + {decalage} : ", exposant + decalage)
        print(f"Exposant décalé de + {decalage}  : codage binaire sur 11 bits : ", bin(exposant + decalage).lstrip('0b').zfill(taille_exposant))
        #print("détermination des bits de mantisse")
        x = x - 1
        nbits = 0
        mantisse = []
        while nbits < taille_mantisse:
            x = x * 2
            partie_entiere = int(x)
            mantisse.append(str(partie_entiere))
            if partie_entiere == 1:
                x = x - partie_entiere
            nbits = nbits + 1
        print("Mantisse : ", ''.join(mantisse))
~~~

## Automatisme 15

On considère une formule booléenne form des variables booléennes `a` et `b` dont voici la table de vérité. 


| a     | b     | form  |
|-------|-------|-------|
| True  | True  | False |
| False | True  | True  |
| True  | False | True  |
| False | False | False |


Quelle est cette formule booléenne  ?

* **Réponse A :**  `a and b`
* **Réponse B :** `a or b`
* **Réponse C :** `((not(a)) and b) or (a and  (not(b)))`
* **Réponse D :** `(not(a)) or (not(b))`


## Automatisme 16

Pouvez-vous deviner  ce qui va se passer si on exécute le code ci-dessous  ? Vérifiez. Explication ?


<pre data-executable>
def boucle1():
    x = 1
    h = 1
    c = 0
    while x < 2:
        h = h / 2
        x = x + h
        c = c + 1
    return x == 2, c

boucle1()
</pre>

* **Réponse A :**  `(False, 53)`
* **Réponse B :** `(True, 53)`
* **Réponse C :** `(True, 52)`
* **Réponse D :** la boucle ne se termine pas car d'après une formule du cours de mathématiques sur la somme des termes consécutifs d'une suite géométrique, pour tout entier naturel n on a :

<a href="https://www.codecogs.com/eqnedit.php?latex=1&plus;1/2&plus;1/2^2&plus;...&plus;1/2^n&space;=&space;(1-1/2^{n&plus;1})/(1-1/2)=2(1-1/2^{n&plus;1})<2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?1&plus;1/2&plus;1/2^2&plus;...&plus;1/2^n&space;=&space;(1-1/2^{n&plus;1})/(1-1/2)=2(1-1/2^{n&plus;1})<2" title="1+1/2+1/2^2+...+1/2^n = (1-1/2^{n+1})/(1-1/2)=2(1-1/2^{n+1})<2" /></a>



## Automatisme 17 ([banque d'épreuve pratique 2021](http://nsi.enseigne.ac-lyon.fr/spip/spip.php?article81))

Écrire une fonction `recherche` qui prend en paramètres `elt` un nombre entier et `tab`
un tableau de nombres entiers, et qui renvoie l’indice de la première occurrence de `elt`
dans tab si elt est dans tab et -1 sinon.

Exemples :

~~~python
>>> recherche(1, [2, 3, 4])
-1
>>> recherche(1, [10, 12, 1, 56])
2
>>> recherche(50, [1, 50, 1])
1
>>> recherche(15, [8, 9, 10, 15])
3
~~~

## Automatisme 18 ([banque d'épreuve pratique 2021](http://nsi.enseigne.ac-lyon.fr/spip/spip.php?article81))

Écrire une fonction maxi qui prend en paramètre une liste tab de nombres entiers et
renvoie un couple donnant le plus grand élément de cette liste, ainsi que l’indice de la
première apparition de ce maximum dans la liste.

Exemple :

~~~python
>>> maxi([1,5,6,9,1,2,3,7,9,8])
(9,3)
~~~

## Automatisme 19 ([banque d'épreuve pratique 2021](http://nsi.enseigne.ac-lyon.fr/spip/spip.php?article81))


On considère la fonction `insere` ci-dessous qui prend en argument un entier `a` et un
tableau `tab` d'entiers triés par ordre croissant. Cette fonction insère la valeur `a` dans le tableau et renvoie le nouveau tableau. Les tableaux seront représentés sous la forme de
listes python.

Compléter la fonction `insere` ci-dessous.

<pre data-executable>
def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = "à compléter"
    while i >= 0 and a < "à compléter" : 
      l[i+1] = "à compléter"
      l[i] = a
      i = "à compléter"
    return l

assert insere(3,[1,2,4,5]) == [1, 2, 3, 4, 5]
assert insere(10,[1,2,7,12,14,25]) == [1, 2, 7, 10, 12, 14, 25]
assert insere(1,[2,3,4]) == [1,2,3,4]
print('Tests réussis')
</pre>

## Automatisme 20 ([banque d'épreuve pratique 2021](http://nsi.enseigne.ac-lyon.fr/spip/spip.php?article81))


Compléter sous Python la fonction suivante en respectant la spécification. 


<pre data-executable>
def dichotomie(tab, x):
    """
        tab : tableau d’entiers trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """

    debut = 0 
    fin = len(tab) - 1
    while debut <= fin:
        m = "à compléter"
        if x == tab[m]:
            return "à compléter"
        if x > tab[m]:
            debut = m + 1
        else:
             fin = "à compléter"			
    return "à compléter"

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27) == False
print('Tests réussis')
</pre>




## Automatisme 21 ([banque d'épreuve pratique 2021](http://nsi.enseigne.ac-lyon.fr/spip/spip.php?article81))


Écrire une fonction `tri_selection` qui prend en paramètre un tableau tab de nombres entiers et qui renvoie le tableau trié par ordre croissant.

On utilisera l’algorithme suivant :

* on recherche le plus petit élément du tableau, et on l'échange avec l'élément d'indice
0 ;
* on recherche le second plus petit élément du tableau, et on l'échange avec l'élément
d'indice 1 ;
* on continue de cette façon jusqu'à ce que le tableau soit entièrement trié dans l'ordre croissant.


Exemples de postconditions :

~~~python
>>> assert tri_selection([1,52,6,-9,12]) == [-9, 1, 6, 12, 52]
>>> assert tri_selection([]) == []
>>> assert tri_selection([1, 4, 8]) == [1, 4, 8]
>>> assert tri_selection([8, 4, 1]) == [1, 4, 8]
~~~


## Automatisme 22 ([banque d'épreuve pratique 2021](http://nsi.enseigne.ac-lyon.fr/spip/spip.php?article81))

Un mot palindrome peut se lire de la même façon de gauche à droite ou de droite à
gauche : bob, radar, et non sont des mots palindromes.

De même certains nombres sont eux aussi des palindromes : 33, 121, 345543.

L’objectif de cet exercice est d’obtenir un programme Python permettant de tester si un
nombre est un nombre palindrome.

Pour remplir cette tâche, on vous demande de compléter le code des trois fonctions ci-
dessous sachant que la fonction est_nbre_palindrome s’appuiera sur la fonction
`est_palindrome` qui elle-même s’appuiera sur la fonction `inverse_chaine`.


La fonction `inverse_chaine` inverse l'ordre des caractères d'une chaîne de caractères
chaine et renvoie la chaîne inversée.
La fonction `est_palindrome` teste si une chaine de caractères chaine est un
palindrome. Elle renvoie `True` si c’est le cas et `False` sinon. Cette fonction s’appuie sur
la fonction précédente.
La fonction `est_nbre_palindrome` teste si un nombre nbre est un palindrome. Elle
renvoie True si c’est le cas et False sinon. Cette fonction s'appuie sur la fonction
précédente.



Compléter le code des trois fonctions ci-dessous.


<pre data-executable>
def inverse_chaine(chaine):
    result = "à compléter"
    for caractere in chaine:
       result = "à compléter"
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return "à compléter"
    
def est_nbre_palindrome(nbre):
    chaine = "à compléter"
    return est_palindrome(chaine)

assert inverse_chaine('bac') == 'cab'
assert est_palindrome('NSI') == False
assert est_palindrome('ISN-NSI') == True
assert est_nbre_palindrome(214312) == False
assert est_nbre_palindrome(213312) == True
print("Tests réussis")
</pre>

## Automatisme 23 ([banque d'épreuve pratique 2021](http://nsi.enseigne.ac-lyon.fr/spip/spip.php?article81))

Compléter la fonction `separe` ci-dessous qui prend en argument un tableau tab dont
les éléments sont des 0 et des 1 et qui sépare les 0 des 1 en plaçant les 0 en début de
tableau et les 1 à la suite.

<pre data-executable>
def separe(tab):
    i = 0
    j = "à compléter"
    while i < j :
        if tab[i] == 0 :
            i = "à compléter"
        else :
            tab[i], tab[j] = "à compléter"
            j = "à compléter"
    return tab

assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print("Tests réussis")
</pre>



## Automatisme 24 ([banque d'épreuve pratique 2021](http://nsi.enseigne.ac-lyon.fr/spip/spip.php?article81))

Écrire une fonction `indice_du_min` qui prend en paramètre un tableau de nombres non
trié `tab`, et qui renvoie l'indice de la première occurrence du minimum de ce tableau. Les
tableaux seront représentés sous forme de liste Python.

Exemples :
~~~python
>>> indice_du_min([5])
0
>>> indice_du_min([2, 4, 1])
2
>>> indice_du_min([5, 3, 2, 2, 4])
2
~~~

## Automatisme 25 : traitement de données en tables

Télécharger [l'archive](automatismes/ressources/archive_automatisme25.zip) avec le code source à compléter et le fichier `eleves.csv`.  Un corrigé est [ici](automatismes/ressources/automatisme_tables_traiter.py).

~~~python
#!/usr/bin/env python

"""Consigne : compléter au niveau des  à "compléter"
les fonctions :
    
    1)  moyenne_table
    2) enreg_avec_recompense
    3)  generer_table_recompenses
    4) decompte_recompenses
    5) clef_tri_moyenne_decroissant
    6) clef_tri_alphabetique_croissant_moyenne_decroissant
    
    Chaque fonction est accompagné d'un test unitaire => pour tester, 
    désactiver les commentaires dans le programme principal à partir de la ligne 151
    Pour les tris il faut aussi compléter le programme principal en lignes 167 et 171
"""

import csv

#Import / Export d'un tel fichier CSV ver la représentation d'une tble en Python (tableau de dictionnaires)
def lecture_csv(fichier, delimiteur):
    """
    Paramètre : un chemin vers un fichier CSV
    Valeur renvoyée : un tableau de dictionnaires, extraction de la table contenue dans le fichier
    """
    f = open(fichier, mode = 'r', encoding = 'utf8', newline='')
    reader = csv.DictReader(f, delimiter = delimiteur)  #création de l'objet reader
    table = [dict(enregistrement) for enregistrement in reader]
    f.close()
    return table

def ecriture_csv(table, fichier, delimiteur):
    """
    Paramètre : 
        un chemin vers un fichier CSV
        une table comme tableau de dictionnaires partageant les mêmes clefs, de valeurs str
    Valeur renvoyée :
        None, écrit table dans fichier avec Dictriter du  module CSV 
    """
    g = open(fichier, mode = 'w', encoding = 'utf8', newline='')
    attributs = list(table[0].keys())
    writer = csv.DictWriter(g, delimiter = delimiteur, fieldnames = attributs) #création de l'objet writer
    writer.writeheader()   #écriture des attibuts
    for enregistrement in table:
        writer.writerow(enregistrement)  #écriture des enregistrements
    g.close()
    
def moyenne_table(table_eleves) :
    """Paramètre : table_eleves est une représentation de la table extraite de eleves.csv
        sous forme de tableau de dictionnaires. Attention les attributs 'moyenne' sont de 
        type 'str'
    Valeur renvoyée : un flottant représentant la moyenne de tous les élèves
    de la table arrondie à 2 chiffres après la virgule
    """
    somme = 0
    compteur = 0
    for enreg in table_eleves:
        "à compléter"
        "à compléter"
    return round(somme / compteur, 2)

def test_moyenne_table():
    assert moyenne_table(table_eleves) == 11.46
    print("Test unitaire de moyenne_table réussi")
    
def enreg_avec_recompense(enreg):
    """
    Paramètre : enreg un dictionnaire de clefs 'prénom', 'nom', 'moyenne' 
                Attention toutes les clefs ont des valeurs de type str
    Valeur renvoyée : extension du dictionnaire avec une nouvelle clef
    'récompense' de valeurs s :
            'insuffisant' si moyenne < 8
            'médiocre' si 8 <= moyenne < 10
            'passable' si 10 <= moyenne < 12
            'encouragements' si  12 <= moyenne < 14
            'compliments' si   14 <= moyenne < 16
            'félicitations' si moyenne > 16
    """
    copie = { clef : valeur for clef, valeur in enreg.items() }
    m = "à compléter"
    if m < 8:
        copie['récompense'] = 'insuffisant'
    elif "à compléter":
        copie['récompense'] = 'médiocre'
    elif "à compléter":
        copie['récompense'] = 'passable'
    elif "à compléter":
        copie['récompense'] = 'encouragements'
    elif "à compléter":
        copie['récompense'] = 'compliments'
    else:
        copie['récompense'] = 'félicitations'
    return copie


def generer_table_recompenses(table_eleves):
    """Paramètre : table_eleves est une représentation de la table extraite de eleves.csv
        sous forme de tableau de dictionnaires
    Valeur renvoyée : une extension de table_eleves avec un nouvel attribut 'récompense'
    chaque nouvel enregistrement est généré par enreg_avec_recompense
    """
    table_recompenses = "à compléter"  
    return table_recompenses

def test_generer_table_recompenses():
    """Test unitaires de generer_table_recompenses"""
    table_recompenses = generer_table_recompenses(table_eleves)
    assert table_recompenses[0] == {'prénom': 'Zoé', 'nom': 'Collin',
                                    'moyenne': '19', 'récompense': 'félicitations'}
    assert table_recompenses[8] == {'prénom': 'Roland', 'nom': 'Joly', 
                                    'moyenne': '8', 'récompense': 'médiocre'}
    print("Test unitaires de generer_table_recompenses réussis")
    
def decompte_recompenses(table_recompenses):
    """Paramètre : table_recompenses  est une représentation de la table renvoyée 
                    par generer_table_recompenses. 
    Valeur renvoyée : un dictionnaire avec le décompte de chaque récompense
    """
    decompte = dict()
    for enreg in table_recompenses:
        "à compléter"
        "à compléter"
        "à compléter"
        "à compléter"
    return decompte

def test_decompte_recompenses():
    """Test unitaires de decompte_recompenses"""
    decompte = decompte_recompenses(table_recompenses)
    assert decompte == {'félicitations': 89,
                         'médiocre': 77,
                         'compliments': 95,
                         'insuffisant': 86,
                         'passable': 81,
                         'encouragements': 72}
    print("Test unitaires de decompte_recompenses réussis")
    
    
     
def clef_tri_moyenne_decroissant(enreg):
    """Clef de tri par moyenne décroissante
    Attention la valeur de l'attribut 'moyenne' de enreg est de type str"""
    return "à compléter"

def clef_tri_alphabetique_croissant_moyenne_decroissant(enreg):
    """Clef de tri par moyenne décroissante
    Attention la valeur de l'attribut 'moyenne' de enreg est de type str"""
    return "à compléter"
    

#Programme principal
table_eleves = lecture_csv('eleves.csv', ',')
#Décommenter lorsque moyenne_table est complétée
#test_moyenne_table()

#Décommenter lorsque generer_table_recompenses est complétée
#table_recompenses = generer_table_recompenses(table_eleves)
#test_generer_table_recompenses()

#Décommenter lorsque decompte_recompenses est complétée
#test_decompte_recompenses()

#Décommenter e lorsque clef_tri_moyenne_decroissant terminée
#table_recompenses = generer_table_recompenses(table_eleves)

#Ecrire une instruction qui permet de trier  table_recompenses dans l'ordre décroissant des moyennes
#table_tri1 = "à compléter"

#Ecrire une instruction qui permet de trier  table_recompenses :
#d'abord dans l'ordre alphabétique croissant puis dans l'ordre décroissant des moyennes
#table_tri2 = "à compléter"
~~~