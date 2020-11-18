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