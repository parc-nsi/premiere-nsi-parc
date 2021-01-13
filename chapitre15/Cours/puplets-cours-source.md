---
title : Cours sur les p-uplets
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

# Crédits {-} 
 
_Ce cours est inspiré du chapitre 14 du manuel NSI de la collection Tortue chez Ellipse,  auteurs : Ballabonski, Conchon, Filliatre, N'Guyen. J'ai également consulté le prepabac Première NSI de Guillaume Connan chez Hatier, le [document ressource  eduscol sur les types construits](https://cache.media.eduscol.education.fr/file/NSI/77/7/RA_Lycee_G_NSI_repd_types_construits_1170777.pdf) et le livre __Fluent Python__._


<!-- Définition des hyperliens  -->



# p-uplets en Python

:::definition
Un objet de type __tuple__, un __p-uplet__, est une suite ordonnée d’éléments qui peuvent être chacun de n’importe quel type. On parlera indifféremment de __p-uplet__ ou de __tuple__.

Un __p-uplet__ est utilisé comme __enregistrement__ de données hétérogènes qui sont liées entre elles,  par exemple pour une ville : (nom, code postal, latitude, longitude).

~~~python
>>> a = ('lyon', 69000, 45.75, 4.85)
~~~
:::


:::propriete
En [Python][Python], un  __p-uplet__ est un objet de type `tuple`. Pour le définir,  on entoure de parenthèses la séquence ordonnée d'éléments qu'il contient. 

Un objet de type `tuple` partage de nombreuses propriétés avec les objets de type `list` que nous avons utilisés pour implémenter les tableaux homogènes. En particulier, sa valeur est une __référence__  vers la zone mémoire où est stockée la séquence d'objets (propriété d'aliasing). 

![aliasing](images/aliasing.png){width=80%}\

Les objets de type `tuple` diffèrent de ceux de type `list` car ils ne peuvent être modifiés une fois qu'ils sont créés : on dit qu'ils sont __immutables__.  Cette propriété, partagée avec les chaînes de caractères de type `str` est importante  car elle facilite la gestion en  mémoire  des données qui ne doivent pas changer, la démonstration  de propiétés des programmes et elle permet leur  utilisation comme clef dans les tableaux associatifs ou [tables de hachage](https://fr.wikipedia.org/wiki/Table_de_hachage). Ces derniers sont  implémentés par un autre type construit très important en [Python][Python], celui des __dictionnaires__.

A part les propriétés de modification, les autres propriétés du type `list` sont disponibles pour le type `tuple`.


~~~python
>>> a = ('lyon', 69000, 45.75, 4.85)
>>> type(a)
<class 'tuple'>
>>> a[0]
'lyon'
>>> len(a)
4
>>> a[0] = 'St-Etienne'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
~~~

:::

:::methode

Présentons les principales opérations sur les __tuples__  en [Python][Python]. Le type __tuple__ implémente toutes les méthodes du type __list__ sauf celles d'ajout ou de modification d'élément. Pour obtenir la liste de ces méthodes, on peut évaluer `dir(tuple)`dans une console. 


* __Construction :__
  * _Par extension_, on définit un __tuple__ en séparant ses éléments par une virgule. En particulier, s'il ne contient
qu'un seul élément, il faut le faire suivre d'une virgule. Les parenthèses ne sont pas obligatoires mais sont nécessaires si on imbrique des __tuples__. On peut aussi convertir en __tuple__ un autre itérable (`list`, `str`, `range`) avec le constructeur `tuple` .
~~~python
>>> notes = ('paul',10, 12,18)
>>> telephone = 'paul', '0606060606'
>>> telephone
('paul', '0606060606')
>>> singleton = 'Solo',
>>> singleton
('Solo',)
>>> s = ('solo')
>>> s
'solo'
>>> los_angeles = ('Lax aiport', (33.9425, -118.408056))
>>> tuple([1,2])
(1, 2)
>>> tuple(range(3))
(0, 1, 2)
~~~
  * _Par compréhension_, la syntaxe est la même que pour les tableaux de type `list`, mais attention, il faut utiliser le constructeur `tuple`, sinon on construit un __générateur__ (distributeur d'objets comme `range`). En général on construit plutôt une structure imbriquée avec un tableau de __tuples__.
~~~python
>>> m = (k for k in range(10))
>>> m
<generator object <genexpr> at 0x7f26afa0ef90>
>>> tuple(m)
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> famille = ['trefle', 'pique', 'carreau', 'coeur']
>>> hauteur = ['V', 'R', 'D']
>>> valets = [(h,f) for f in famille for h in hauteur if h == 'V']
>>> valets
[('V', 'trefle'), ('V', 'pique'), ('V', 'carreau'), ('V', 'coeur')]
~~~
* __Accès en lecture :__  Seul l'accès en lecture est permis, on utilise les index (de 0 à `len(tuple)-1`)  comme pour les objets de type `list`. Une propriété très utilisée est le _tuple unpacking_ qui permet de déballer les éléments d'un __tuple__  à droite d'un symbole d'affectation `=` pour les assigner à un __tuple__ d'identifiants à gauche du `=`. On peut ainsi échanger des variables en une seule instruction. Cela fonctionne aussi sur les  autres objets itérables comme ceux  de type `list`.
~~~python
>>> paul = ('identifiant', '01011970')
>>> len(paul)
2
>>> paul[1] = '31122000'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> login, password = paul
>>> login
'identifiant'
>>> password
'01011970'
>>> login, password = password, login  #échange de variables par tuple unpacking
>>> login, password
('01011970', 'identifiant')
>>> paul
('identifiant', '01011970')
~~~
* __Parcours :__ Comme pour les objets de type `list` et les itérables en général, on peut parcourir un __tuple__ par index ou par éléments. Pour un tableau de __tuple__, on peut déballer directement dans la boucle `for` avec le _tuple unpacking_.
~~~python
>>> notes
('paul', 10, 12, 18)
>>> for k in range(len(notes)):
...     print('Index : ', k, 'Valeur : ', notes[k])
... 
Index :  0 Valeur :  paul
Index :  1 Valeur :  10
Index :  2 Valeur :  12
Index :  3 Valeur :  18
>>> for element in notes:
...     print(element)
... 
paul
10
12
18
>>> passeports = [('USA', '31195855'), ('BRA', 'CE342567'), ('FRA', 'XDA502856')]
>>> for pays, numero in passeports:
...     print(pays, numero)
... 
USA 31195855
BRA CE342567
FRA XDA502856
~~~
* __Concaténation :__ On peut concaténer deux __tuples__ et on créé alors un nouveau __tuple__. On peut l'observer en affichant l'identité du __tuple__ avec la fonction `id` : l'entier affiché représente l'identifiant mémoire de l'objet. On ne peut pas ajouter des éléments à un __tuple__ comme pour un tableau avec la méthode `append`.
  On peut  factoriser l'opération de concaténation avec l'opérateur `*`.
~~~python
>>> a = ('Limoges',)    #attention tuple avec u nseul élément
>>> id(a)               #identifiant de a 
139804156798144
>>> b = (45.85, 1.25)   # latitude et longitude
>>> a = a + b
>>> a
('Limoges', 45.85, 1.25)
>>> id(a)  #l'identifiant de a est changé, un nouveau tuple a été créé
139804132207488
>>> population = 132175
>>> a.append(population)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> d = ('paris',)
>>> 3 * d
('paris', 'paris', 'paris')
~~~
* __Test d'appartenance, comparaison :__   On peut tester l'appartenance d'un élément à un __tuple__ avec l'opérateur `in` et comparer deux __tuples__ avec `==`, `<`, `>`.  La comparaison de deux __tuples__  s'effectue de gauche à droite selon _l'ordre lexicographique_.
~~~python
>>> b = ('Lyon', 516092)
>>> a = ('Lyon', 516092)
>>> id(a), id(b)
(139804132208448, 139804132156672)
>>> a is b
False
>>> a == b
True
>>> 'Lyon' in a
True
>>> 'St-Etienne' not in a
True
>>> ('adama', 10, 6) < ('adam', 10)
False
>>> ('adama', 10, 6) > ('adama', 10)
True
~~~

* __Recherche, dénombrement :__ On peut rechercher l'index de la première occurence d'un élément dans un __tuple__ avec la méthode `index`, ou compter le nombre d'occurences d'une valeur avec `count`.
~~~python
>>> from random import randint
>>> e = tuple([randint(1,6) for _ in range(10)])
>>> e
(2, 6, 1, 3, 5, 1, 5, 2, 5, 5)
>>> e.index(5)
4
>>> e.index(1)
2
~~~
:::

:::exercice
Dans le plan muni d'un repère orthonormé, chaque point est représenté par un __tuple__ de coordonnées :

~~~python
>>> M = (1, 2)
>>> N = (4,6)
>>> P = (9,8)
~~~

1. Compléter la fonction Python ci-dessous pour que `milieu(A, B)` retourne le __tuple__ de coordonnées du milieu du segment reliant les points `A` et `B` passés en paramètres.

~~~python
def milieu(A, B):
  xA, yA = A
  xB, yB = B
  # à compléter
~~~

2. Écrire une fonction `longueurs(A, B, C)` qui prend en paramètres trois points `A, B, C` et retourne le triplet de longueurs des côtés du triangle `ABC`.  On rappelle la formule de la distance entre deux points $A(x_{A}, y_{A})$,  $B(x_{B}, y_{B})$ :   $AB=\sqrt{(x_{B}-x_{A})^{2}+(y_{B}-y_{A})^{2}}$. On importera la fonction racine carrée depuis le module `math` avec `from math import sqrt` et on pourra écrire aussi une fonction de signature `distance(A, B)` qui renvoie la distance entre les points A et B.
:::


# QCM de type E3C2

:::exercice

1. __Question 1 :__ On définit :
   
tab = \[ (\'Léa\', 14), (\'Guillaume\', 12), (\'Anthony\', 16),
(\'Anne\', 15) \]

Quelle est la valeur de l\'expression \[x\[0\] for x in tab if
x\[1\]\>=15\] ?

**Réponses**

A \[(\'Anthony\', 16), (\'Anne\', 15)\]

B \[\'Anthony\', \'Anne\'\]

C \[16, 15\]

D TypeError : \'tuple\' object is not callable

2. __Question 2 :__ Une table d'un fichier client contient le nom, le prénom et
l'identifiant des clients sous la forme :

clients = \[ (\"Dupont\", \"Paul\", 1),(\"Durand\", \"Jacques\", 2),\(\"Dutronc\", \"Jean\", 3),\...\]

En supposant que plusieurs clients se prénomment Jean, que vaut la liste
x après l'exécution du code suivant ?

~~~python
x = []
for i in range(len(clients)):
if clients[i][j] == "Jean":
  x = clients[i]
~~~


***Réponses***

A Une liste de tuples des noms, prénoms et numéros de tous les clients
prénommés Jean

B Une liste des numéros de tous les clients prénommés Jean

C Un tuple avec le nom, prénom et numéro du premier client prénommé Jean

D Un tuple avec le nom, prénom et numéro du dernier client prénommé Jean

3. __Question 3 :__ Quel est le type de l'expression `f(4)` si la fonction `f`est définie par
:

~~~python
def f(x):
  return (x, x**2)
~~~

**Réponses**

A un entier

B un flottant

C une liste

D un tuple
:::


# Synthèse

:::memo
* Un __p-uplet__ ou __tuple__ est une séquence ordonnée d'éléments qui peuvent être de type hétérogènes.
* La séquence d'informations rassemblée dans un __tuple__ est un __enregistrement__.
* En [Python][Python], les __tuples__ sont de type `tuple` et sont __immutables__. Ils partagent les mêmes opérations que les tableaux de type `list` sauf les opérations de modification et d'ajout.
:::