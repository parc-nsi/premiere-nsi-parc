---
title:  Automatismes
layout: parc
---



>L'image `gif` ci-dessous présente  différentes étapes du déroulement d'un algorithme de rotation d'images inspiré d'un travail présenté par Laurent Abbal du lycée français de Tokyo. Le  programme assez court peut être réalisé par un élève  de terminale (récursivité, approche _diviser pour régner_).
>L'image source représente l'oeuvre _Matsuri Yatai Dragon_ du peintre japonais [Hokusai](https://en.wikipedia.org/wiki/en:Hokusai). Elle est dans le domaine public et disponible sur [https://commons.wikimedia.org](https://commons.wikimedia.org/wiki/File:Hokusai_Dragon.jpg).

[![Dragon](rotation-dragon-2.gif "dragon-hokusai")](https://commons.wikimedia.org/wiki/File:Hokusai_Dragon.jpg)



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
