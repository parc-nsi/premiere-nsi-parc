---
title : TP sur les tableaux
subtitle: Thème types construits
author : Première NSI,  [Lycée du Parc](https://frederic-junier.org/)
numbersections: true
fontsize: 11pt
geometry:
- top=20mm
- left=20mm
- right=20mm
- heightrounded    
--- 
 
<!-- Définition des hyperliens  -->

[Python]: https://docs.python.org/3/tutorial/datastructures.html
[Python-tutor]: http://pythontutor.com/visualize.html#mode=edit

_On désigne par tableaux, les objets de type `list` du langage [Python][Python]. Dans les exercices, comme dans les QCM d'E3C, on rencontrera parfois l'appellation Python liste pour désigner la structure de données tableau_.

:::exercice
Créer un fichier _TP-Tableaux.py_  pour rassembler les scripts rédigés pendant le TP.

Enregistrer ce fichier dans un dossier pertinent de son espace personnel sur le réseau pédagogique.
:::

:::exercice

QCM type E3C

1. On exécute le code suivant :

    ~~~python
    t = [1,2,3,4,5,6,7,8,9]

    v = [c for c in t if c%3 == 0]
    ~~~

Quelle est la valeur de la variable `v` à la fin de cette exécution ?

* __Réponse A :__ 18    __Réponse B :__ `[1,4,7]`
* __Réponse C :__  `[3,6,9]`  __Réponse D :__  `[1,2,3,4,5,6,7,8,9]`


2. On définit : `resultat = [ i*2 for i in range(10) ]`. 

Quelle est la valeur de `resultat` ?

* __Réponse A :__  `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` 
* __Réponse B :__ `[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]` 
* __Réponse C :__ `[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]` 
* __Réponse D :__ `[2, 4, 6, 8, 10, 12, 14, 16, 18]`


3. On considère la fonction suivante :

~~~python
def somme(tab):
    s = 0
    for i in range(len(tab)):
        .....
    return s
~~~

Par quelle instruction faut-il remplacer les points de suspension pour
que l'appel `somme([10,11,12,13,14])` renvoie 60 ?

* __Réponse A :__  `s = tab[i]`  __Réponse B :__   `s = s + tab[i]`
* __Réponse C :__ `tab[i] = tab[i] + s`   __Réponse D :__ `s = s + i`

:::

:::exercice

1. La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il remplacer les points de suspension pour que la fonction soit correcte ? _Auteur Sylvie Genre_

    ~~~python
    def moyenne(tableau):
        total = ...
        for valeur in tableau:
            total = total + valeur
        return total / ...
    ~~~
2. Donner la valeur des expressions Python suivantes :

    ~~~python
    >>> [1, 2, 3] + [4, 5, 6]
    >>> 2 * [1, 2, 3]
    ~~~

:::

:::exercice

1. Écrire une fonction Python   `smul` à deux paramètres, un nombre et une liste de nombres, qui multiplie chaque élément de la liste par le nombre et renvoie une nouvelle liste :
~~~python
>>> smul(2, [1, 2, 3])
[2, 4, 6]
~~~
2. Écrire une fonction Python `vsom`  qui prend en paramètre deux listes de nombres de même longueur et qui renvoie une nouvelle liste constituée de la somme terme à terme de ces deux listes :
~~~python
>>> vsom([1, 2, 3], [4, 5, 6])
[5, 7, 9]
~~~
3. Écrire une fonction  [Python][Python] `vdif` qui prend en paramètre deux listes de nombres de même longueur et qui renvoie une nouvelle liste constituée de la différence terme à terme de ces deux listes (la deuxième  moins la première).
~~~python
>>> vdif([1, 2, 3], [4, 5, 6])
[3, 3, 3]
~~~
4. Écrire une fonction Python `vprod` qui prend en paramètre deux listes de nombres de même longueur et qui retourne une nouvelle liste constituée des produits terme à terme de ces deux listes.
~~~python
>>> vprod([1, 2, 3], [4, 5, 6]) 
[4, 10, 18]
~~~
:::


:::exercice
1. Écrire une  fonction `produit(tab)` qui retourne le produit  des éléments d'un tableau de nombres `tab`.
2. Écrire une fonction   `all_positive(tab)`  qui retourne un booléen indiquant si tous les éléments du tableau de nombres `tab`  sont strictement positifs.
3. Écrire une fonction   `any_positive(tab)`  qui retourne un booléen indiquant si  au moins un élément du tableau de nombres `tab`  est strictement positif.
:::

:::exercice

1. Écrire une fonction `tableau_aleatoire(n, a, b)` qui retourne un tableau de `n` entiers tirés aléatoirement entre les entiers `a` et `b` inclus. On utilisera la fonction `randint`  du module `random`.

~~~python
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.
~~~


2. Écrire une fonction `echantillon(nbexp)` qui retourne un tableau de taille 6 comptant le nombre d'occurences de chaque face numérotée de 1 à 6 sur un échantillon de `nbexp` lancers d'un dé cubique équilibré.

3. On donne ci-dessous une fonction qui prend en paramètre un tableau et retourne un élément extrait au hasard  du tableau. Elle permet par exemple de simuler un tirage sans remise d'une boule dans une urne.

    ~~~python
    from random import randint
    def tirage_sans_remise(urne):
        return tab.pop(randint(0, .......)
    ~~~

   * Compléter les pointillés pour respecter la spécification de la fonction.
   * Écrire une fonction `echantillon_tirage_sans_remise` respectant la spécification ci-dessous. Les [annotations de type](https://docs.python.org/fr/3/tutorial/controlflow.html#function-annotations) sont des métadonnées optionnelles décrivant les types utilisés par une fonction.

    ~~~python
    def echantillon_tirage_sans_remise(urne : list, nbtirage : int) -> list:
        """Retourne un tableau, échantillon de nbtirage sans remises
        dans une urne qui est un tableau"""
    ~~~
:::



:::exercice

* La fonction `ord` prend en paramètre un caractère de type `string` et retourne son point de code dans le jeu de caractères [Unicode](https://fr.wikipedia.org/wiki/Unicode).
* La fonction `chr` prend en paramètre un point de code Unicode et retourne le caractère correspondant.

~~~python
>>> ord('a')
97
>>> chr(97)
'a'
~~~


1. Construire un tableau  `alphabet` qui contient toutes les lettres minuscules de l'alphabet romain.
2. Construire un tableau `consonne` qui contient toutes les consonnes dans `alphabet`.
3. Écrire une fonction `occurences(chaine)` qui prend en paramètre une chaîne de caractère et retourne un tableau de taille 26 avec le nombre d'occurences dans `chaine` des 26 lettres de l'alphabet romain.
:::

:::exercice

_Exercice du manuel de NSI de Thibault Balabonski  chez Ellipses_

En mathématiques, la [suite de Fibonacci](http://images.math.cnrs.fr/Mysteres-arithmetiques-de-la-suite-de-Fibonacci.html) est une séquence d'entiers définie ainsi : on part des entiers 0 et 1 puis on construit à chaque fois l'entier suivant comme la somme des deux précédents :
$$0, 1, 1, 2, 3, 5 ....$$

Compléter la fonction `fibonacci(n)` ci-dessous pour qu'elle retourne un tableau contenant les `n`  premiers termes de la suite de Fibonacci avec `n` entier supposé supérieur ou égal à 2. Les deux assertions proposées doivent être vérifiées.

~~~python
def fibonacci(n):
    #à compléter

f6 = fibonacci(6)
assert f6 == [0,1, 1, 2,3,5]
f30 = fibonacci(30)
assert f30[29] == 514229
~~~
:::


:::methode
Pour stocker  de façon persistante (sur le disque et pas seulement en mémoire vive) des informations  lisibles par un humain, on utilise un __fichier texte__ qui est une simple séquence de caractères. Le contenu du fichier doit respecter un  __format__ qui fixe  des contraintes pour que les informations soient interprétables lors de la  lecture.  Par exemple le code source d'un programme [Python][Python] ou d'une page Web en HTML, un fichier de mesures au format [CSV][https://fr.wikipedia.org/wiki/Comma-separated_values),  sont  des fichiers textes. 

Tester les séquences  d'instructions suivantes dans une console [Python][Python] pour découvrir des manipulations de base de fichiers textes.

* Création d'un fichier `test.txt` dans le répertoire de travail

~~~python
>>> f = open('test.txt', 'w')   # ouverture du fichier en écriture
>>> f.write('10\n')   #  ligne 1 : '\n'  est un caractère de saut de ligne
3
>>> f.write('11 12\n')  #ligne 2  avec 6 caractères 
6
>>> f.write('13 14 15\n')  #ligne 3 avec 9 caractères
9
>>> f.close()   #fermeture du fichier
~~~

* Lecture et traitement ligne par ligne du fichier  `test.txt` :

~~~python
>>> g = open('test.txt', 'r')  #ouverture du fichier
>>> ligne1 = g.readline()  #lecture de ligne 1
>>> ligne1
'10\n'
>>> ligne1.rstrip() #nettoyage du caractère de fin de ligne
'10'
>>> int(ligne1.rstrip()) #conversion de chaine vers entier
10
>>> ligne2 = g.readline()  #lecture de ligne 2
>>> ligne2
'11 12\n'
>>> ligne2.rstrip()  #nettoyage du caractère de fin de ligne
'11 12'
>>> ligne2.rstrip().split(' ')  #découpage de ligne 2 selon le caractère par défaut de séparation ' ', on peut écrire juste split() 
['11', '12']
>>> [int(c) for c in ligne2.rstrip().split()]  #conversion en entier
[11, 12]
>>> g.close()   #fermeture du fichier
~~~


:::

:::exercice

* __Énoncé :__

Comme le disait le grand-père de Joseph Marchand, « Le plus beau voyage est celui qu'on n'a pas encore fait ». New York était dans la tête de Joseph depuis plusieurs années maintenant, et il a décidé aujourd'hui d'acheter son billet d'avion. 
Quelques secondes avant de cliquer sur le bouton « Acheter ! », son amie Haruhi lui envoie une liste de prix qu'elle a trouvés sur Internet. Joseph est curieux de voir si ces derniers sont moins chers que le billet qu'il s'apprêtait à acheter.

* __Entrée :__

Sur la première ligne le prix initial du billet de Joseph.
Sur la deuxième ligne un entier N , correspondant au nombre de billets envoyés par Haruhi. La ligne suivante contient les N prix trouvés par Haruhi.

* __Sortie :__ 

Si Haruhi a trouvé au moins 3 prix strictement moins chers que celui de Joseph, affichez « ARNAQUE ! » pour l'avertir. Sinon « Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos ! ».

* Exemple 1 :

    * Entrée :    
  
        ~~~
        570
        4
        495 1200 540 450
        ~~~
        
    * Sortie :  
  
        ~~~
        ARNAQUE !
        ~~~

* Exemple 2:
  * Entrée :
  
    ~~~
    820
    5
    580 2000 970 1050 820
    ~~~

  *  Sortie :
  
    ~~~
    Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos !
    ~~~


1. Récupérer les fichiers textes `arnaque-exemple1.txt`  et `arnaque-exemple2.txt` avec les entrées des deux exemples.
2. En s'inspirant de la méthode de lecture de fichier texte présentée précédemment, compléter la fonction ci-dessous pour qu'elle résolve le problème. Les deux assertions doivent être vérifiées.
3. Se créer un compte sur le site [Prologin](https://prologin.org/user/register?next=%2F) et soumettre sa solution au juge en ligne sur <https://prologin.org/train/2019/qualification/arnaque_aerienne>. 
   
    Avant de soumettre, remplacer dans la fonction l'instruction `f = open(inputfile)` par `f = inputfile` et le code du programme principal par :

    ~~~python
    import sys
    arnaque(sys.stdin)
    ~~~
    
    `sys.stdin` est [l'entrée standard](https://docs.python.org/fr/3/library/sys.html#sys.stdin) de l'interpréteur Python.

4. Sur la même plateforme, résoudre  cet autre problème du même type : <https://prologin.org/train/2018/qualification/faites_place>

~~~python
def arnaque(inputfile):
    """Résolution du problème 
    https://prologin.org/train/2019/qualification/arnaque_aerienne"""
    f = open(inputfile)  #ouverture du  fichier d'entrée
    # TO DO à compléter
    f.close() 
    c = 0
    # TO DO à compléter
    if c >= 3:
        print("ARNAQUE !")
        return 1
    else:
        print("Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos !")
        return 0
         
assert arnaque('arnaque-exemple1.txt') == 1
assert arnaque('arnaque-exemple2.txt') == 0
print("Tests unitaires réussis !")
~~~
:::


:::exercice
Écrire une fonction `maximum_intervalle(t, n)` qui prend en paramètres un tableau d'entiers `t`  et un entier `n` supposé inférieur ou égal à la longueur de `t` et qui retourne la somme maximale sur tous les sous-tableaux de longueur `n`  inclus dans `t` .

~~~python
>>> maximum_intervalle([10,2,8,4,7,5], 3)
16
~~~
:::

