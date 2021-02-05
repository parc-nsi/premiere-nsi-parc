from partieB import *

## Test de toutes_combinaisons2

def test_toutes_combinaisons2():
    assert toutes_combinaisons2() == toutes_combinaisons()
    print("Test réussi pour toutes_combinaisons2")

##Décommentez pour le test :
#test_toutes_combinaisons2()

## Test de compatible

def test_compatible():
    tab_proposition = [[0, 0, 0, 0],  [1, 1, 1, 1],  [2, 2, 2, 2],  [2, 3, 3, 3],  [4, 2, 3, 4],  
     [5, 2, 5, 3],  [6, 2, 6, 3],  [6, 2, 7, 3]]
    tab_reponse = [[0, 0], [0, 0], [1, 0], [1, 1], [1, 1], [2, 0], [3, 0], [4, 0]]
    for k in range(1, len(tab_proposition)):
        assert compatible(tab_proposition[k],tab_proposition[:k], tab_reponse[:k])
    print('Tests réussis pour compatible')

##Décommentez pour le test :
#test_compatible()

## Test de joueur_ordinateur

def test_joueur_ordinateur():
    #résultats de parties simulées (essi, secret, tab_proposition, tab_reponse)
    parties = [(10,
  [3, 0, 8, 7],
  [[0, 0, 0, 0],
   [0, 1, 1, 1],
   [2, 0, 2, 2],
   [3, 0, 3, 3],
   [3, 0, 4, 4],
   [3, 0, 5, 5],
   [3, 0, 6, 6],
   [3, 0, 7, 7],
   [3, 0, 7, 8],
   [3, 0, 8, 7]],
  [[1, 0],
   [0, 1],
   [1, 0],
   [2, 0],
   [2, 0],
   [2, 0],
   [2, 0],
   [3, 0],
   [2, 2],
   [4, 0]]),
 (10,
  [6, 7, 7, 9],
  [[0, 0, 0, 0],
   [1, 1, 1, 1],
   [2, 2, 2, 2],
   [3, 3, 3, 3],
   [4, 4, 4, 4],
   [5, 5, 5, 5],
   [6, 6, 6, 6],
   [6, 7, 7, 7],
   [6, 7, 7, 8],
   [6, 7, 7, 9]],
  [[0, 0],
   [0, 0],
   [0, 0],
   [0, 0],
   [0, 0],
   [0, 0],
   [1, 0],
   [3, 0],
   [3, 0],
   [4, 0]]),
 (7,
  [6, 1, 6, 6],
  [[0, 0, 0, 0],
   [1, 1, 1, 1],
   [1, 2, 2, 2],
   [3, 1, 3, 3],
   [4, 1, 4, 4],
   [5, 1, 5, 5],
   [6, 1, 6, 6]],
  [[0, 0], [1, 0], [0, 1], [1, 0], [1, 0], [1, 0], [4, 0]]),
 (12,
  [9, 5, 9, 8],
  [[0, 0, 0, 0],
   [1, 1, 1, 1],
   [2, 2, 2, 2],
   [3, 3, 3, 3],
   [4, 4, 4, 4],
   [5, 5, 5, 5],
   [5, 6, 6, 6],
   [7, 5, 7, 7],
   [8, 5, 8, 8],
   [8, 5, 9, 9],
   [9, 5, 8, 9],
   [9, 5, 9, 8]],
  [[0, 0],
   [0, 0],
   [0, 0],
   [0, 0],
   [0, 0],
   [1, 0],
   [0, 1],
   [1, 0],
   [2, 0],
   [2, 2],
   [2, 2],
   [4, 0]]),
 (11,
  [9, 8, 7, 0],
  [[0, 0, 0, 0],
   [0, 1, 1, 1],
   [2, 0, 2, 2],
   [3, 3, 0, 3],
   [4, 4, 4, 0],
   [5, 5, 5, 0],
   [6, 6, 6, 0],
   [7, 7, 7, 0],
   [7, 8, 8, 0],
   [9, 7, 8, 0],
   [9, 8, 7, 0]],
  [[1, 0],
   [0, 1],
   [0, 1],
   [0, 1],
   [1, 0],
   [1, 0],
   [1, 0],
   [2, 0],
   [2, 1],
   [2, 2],
   [4, 0]]),
 (9,
  [7, 8, 5, 1],
  [[0, 0, 0, 0],
   [1, 1, 1, 1],
   [1, 2, 2, 2],
   [3, 1, 3, 3],
   [4, 4, 1, 4],
   [5, 5, 5, 1],
   [5, 6, 6, 1],
   [7, 5, 7, 1],
   [7, 8, 5, 1]],
  [[0, 0], [1, 0], [0, 1], [0, 1], [0, 1], [2, 0], [1, 1], [2, 1], [4, 0]]),
 (10,
  [7, 3, 0, 9],
  [[0, 0, 0, 0],
   [0, 1, 1, 1],
   [2, 0, 2, 2],
   [3, 3, 0, 3],
   [3, 4, 0, 4],
   [5, 3, 0, 5],
   [6, 3, 0, 6],
   [7, 3, 0, 7],
   [7, 3, 0, 8],
   [7, 3, 0, 9]],
  [[1, 0],
   [0, 1],
   [0, 1],
   [2, 0],
   [1, 1],
   [2, 0],
   [2, 0],
   [3, 0],
   [3, 0],
   [4, 0]]),
 (9,
  [5, 0, 4, 8],
  [[0, 0, 0, 0],
   [0, 1, 1, 1],
   [2, 0, 2, 2],
   [3, 0, 3, 3],
   [4, 0, 4, 4],
   [4, 0, 5, 5],
   [5, 0, 4, 6],
   [5, 0, 4, 7],
   [5, 0, 4, 8]],
  [[1, 0], [0, 1], [1, 0], [1, 0], [2, 0], [1, 2], [3, 0], [3, 0], [4, 0]]),
 (10,
  [9, 1, 7, 1],
  [[0, 0, 0, 0],
   [1, 1, 1, 1],
   [1, 1, 2, 2],
   [1, 3, 1, 3],
   [4, 1, 4, 1],
   [5, 1, 5, 1],
   [6, 1, 6, 1],
   [7, 1, 7, 1],
   [7, 1, 8, 1],
   [9, 1, 7, 1]],
  [[0, 0],
   [2, 0],
   [1, 1],
   [0, 2],
   [2, 0],
   [2, 0],
   [2, 0],
   [3, 0],
   [2, 1],
   [4, 0]]),
 (7,
  [3, 0, 6, 0],
  [[0, 0, 0, 0],
   [0, 0, 1, 1],
   [0, 2, 0, 2],
   [3, 0, 3, 0],
   [3, 0, 4, 0],
   [3, 0, 5, 0],
   [3, 0, 6, 0]],
  [[2, 0], [1, 1], [0, 2], [3, 0], [3, 0], [3, 0], [4, 0]])]
    tab_combi = toutes_combinaisons()
    for essai, secret, tab_proposition, tab_reponse in parties:
        index_courant = 0
        tab_proposition2 = []
        tab_reponse2 = []
        for i in range(essai):
            index_courant, proposition_ordi = joueur_ordinateur(index_courant, tab_combi, tab_proposition2,tab_reponse2)
            tab_proposition2.append(proposition_ordi)
            bulls, cows = nombre_bulls_cows(proposition_ordi, secret) 
            tab_reponse2.append([bulls, cows])  
            assert tab_proposition2[i] == tab_proposition[i] and tab_reponse[i] == tab_reponse2[i]
    print('Tests réussis pour joueur_ordinateur')

##Décommentez pour le test :
#test_joueur_ordinateur()


## Test de moyenne


from random import randint

def test_moyenne():
    for _ in range(10):
        tab_alea = [randint(-100, 100) for _ in range(20)]
        assert moyenne(tab_alea) == sum(tab_alea) / len(tab_alea)
    print('Tests réussis pour moyenne')

##Décommentez pour le test :
#test_moyenne()


