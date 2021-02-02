
Les deux scripts ont été créés par Luciano Ramalho pour son livre Fluent Python :

URL de son depot : https://github.com/fluentpython/example-code-2e/tree/master/03-dict-set/support

J'ai annoté les scripts et légèrement modifié les affichages.

1. Exécuter le script container_perftest_datagen_parc.py, exemple :

~~~
junier@fredportable:~/Git/Gitlab/frederic-junier/Premiere-NSI/TypesConstruits/Dictionnaires/Cours/ressources/test_performance_in$ python3 container_perftest_datagen_parc.py 
initial sample: 10500000 elements
complete sample: 10500000 elements
not selected: 500000 samples
  writing not_selected.arr
selected: 10000000 samples
  writing selected.arr
~~~

Sont alors créés les deux fichiers binaires d'échantillons de nombres flottants
au format double précision :
* selected.arr avec 10 000 000 de flottants  distincts pour choisir la meule de foin (haystack)
* not_selected.arr avec 500 000 flottants distincts (et pas dans selected.arr) pour choisir les aiguilles (needles)
Attention, ces fichiers sont volumineux (80 Mo et 4 Mo), mais le sont beaucoup moins
que s'il s'agissait de fichiers textes
(avec au moins 1 octet par chiffre soit au moins 16 octets par flottants + 1 octet par saut de lignes)

2. Exécuter le script container_perftest_parc.py avec en option le type de conteneur 
pour tester la performance du test d'appartenance avec l'oprateur in pour ce conteneur :
* pour le type dict des dictionnaires, exemple :
~~~
junier@fredportable:~/Git/Gitlab/frederic-junier/Premiere-NSI/TypesConstruits/Dictionnaires/Cours/ressources/test_performance_in$ python3 container_perftest_parc.py dict
Type de conteneur dict
--------------------
Taille de la meule de foin :     1000
Temps minimum de recherche de 1000 aiguilles  (sur 5 recherches): 0.000105 s
--------------------
Taille de la meule de foin :    10000
Temps minimum de recherche de 1000 aiguilles  (sur 5 recherches): 0.000118 s
--------------------
Taille de la meule de foin :   100000
Temps minimum de recherche de 1000 aiguilles  (sur 5 recherches): 0.000229 s
--------------------
Taille de la meule de foin :  1000000
Temps minimum de recherche de 1000 aiguilles  (sur 5 recherches): 0.000393 s
--------------------
Taille de la meule de foin : 10000000
Temps minimum de recherche de 1000 aiguilles  (sur 5 recherches): 0.000474 s
~~~

* pour le type list des listes python, exemple :
~~~
junier@fredportable:~/Git/Gitlab/frederic-junier/Premiere-NSI/TypesConstruits/Dictionnaires/Cours/ressources/test_performance_in$ python3 container_perftest_parc.py list
Type de conteneur list
--------------------
Taille de la meule de foin :     1000
Temps minimum de recherche de 1000 aiguilles  (sur 5 recherches): 0.008002 s
--------------------
Taille de la meule de foin :    10000
Temps minimum de recherche de 1000 aiguilles  (sur 5 recherches): 0.078902 s
--------------------
Taille de la meule de foin :   100000
Temps minimum de recherche de 1000 aiguilles  (sur 5 recherches): 0.812977 s
--------------------
Taille de la meule de foin :  1000000
Temps minimum de recherche de 1000 aiguilles  (sur 5 recherches): 8.554425 s
--------------------
Taille de la meule de foin : 10000000
Temps minimum de recherche de 1000 aiguilles  (sur 5 recherches): 84.754335 s
--------------------
~~~
