---
title:  TP scrabble
layout: parc
---


## Présentation de la structure de données _dictionnaires_

* [Présentation video par Pierre Marquestaut](https://peertube.lyceeconnecte.fr/videos/watch/86be0059-a3c1-41ec-952a-79dea6310c87)

* En Python la structure de données __dictionnaire__ est implémentée par le type `dict`. Voici un  exemple de construction de dictionnaire en Python et de manipulation avec les opérations de base : définition, accès en lecture / écriture,test d'appartenance, parcours.


<pre data-executable>
annuaire = {}  #initialisation d'un dictionnaire vide
annuaire = { 'Victor' : '06 44 44 44 44'} #on peut aussi initialiser un dictionnaire par extension
print("Lecture du numéro de téléphone de Victor dans le dictionnaire annuaire ", annuaire['Victor'])
print("Modification du numéro de Victor dans le dictionnaire annuaire ")
annuaire['Victor'] = '06 33 33 33 33'
print("Ajout  du numéro de Valérie dans le dictionnaire annuaire ")
annuaire['Valérie'] = '06 22 22 22 22'
print("Affichage du dictionnaire annuaire")
print("Test d'appartenance de la clef 'Antoine' au dictionnaire annuaire", 'Antoine' in annuaire)
print("Test d'appartenance de la clef 'Valérie' au dictionnaire annuaire", 'Valérie' in annuaire)
print("Parcours du dictionnaire annuaire par clefs (ici les personnes) :")
for clef in annuaire:
    print("Clef : ", clef, " Valeur : ", annuaire[clef])
print("Parcours du dictionnaire annuaire par tuple (clef, valeur) (ici (personne, numéro)) :")
for clef, valeur in annuaire.items():
    print("Clef : ", clef, " Valeur : ", valeur)
</pre>

Si Binder ne se lance pas, le _snippet_ sur [glot.io](https://glot.io/snippets/fvk5o67xl0) :


<iframe src='https://glot.io/snippets/fvk5o67xl0/embed' frameborder='0' scrolling='no' sandbox='allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts' width='800' height='600'></iframe>

Le même _snippet_ mais sur [basthon](https://console.basthon.fr/?script=eJyVUk1rwkAQvQv-hyEeNgEpRaUHoQfptYUeSi_Fw5KMdUrcDfshheIP8nf4xzqbmE0ULTUsIdl9-96bNyOV8pIMwiP87ABGpMiRLMlKR1pBITy_KA8_qsZtqcDhQPaugXhngDYC5iDuH2A2i0vsYMQsFXoH0ltLEPnRwDl1JQ3gt0NleWs4qAwplybPmDvPp4UH5TeHvdFQILjDvjzsq7VWGH4bB1BIZaHEU9roNRnH74_W8zKLQi-6oBXlx8JP1P5Hn3W5dPycUAhlOo1LRMXFl-ZgzrUkF2YIb1M7Xop6k0lcPb0V17eWn3WYF2mTLo43tI77LytuC_dEqrxOupSQl7gCsVBOk0LBjb3CNe6BSMX9_0vEqv7U6FAXRV6lybU39mrN9dwFQQsp5cSRW55YYxmHNoN5yGSlG0hfYj4cAD9HmadwOg8zFnBjSEIj0ZtmL3YqHC5vNed8xXOQNsTbmjZrvKat0XE7QtmZ4_ZC3_kdOdzYNLulgqPsL_DAbG8)

## Une première utilisation des dictionnaires : résolution d'un problème sur CodinGame

1. Lire l'énoncé du problème sur la page <https://www.codingame.com/ide/puzzle/scrabble>.
2. Pour résoudre ce problème on propose de compléter le code ci-dessous :
   * dans`spyder`, compléter chaque fonction   en respectant sa spécifications des fonctions et en vérifiant  les tests unitaires qui l'accompagnent. 
   * compléter le code du programme principal
   * soumettre son code aux validateurs sur la page <https://www.codingame.com/ide/puzzle/scrabble>.


~~~python
#dictionnaire des valeurs des lettres minuscules au scrabble
valeur = {
    'a' : 1,
    'e' : 1,
    'i' : 1,
    'o' : 1,
    'n' : 1,
    'r' : 1,
    't' : 1,
    'l' : 1,
    's' : 1,
    'u' : 1,
    'd' : 2,
    'g' : 2,
    'b' : 3, 'c' : 3, 'm' : 3, 'p' : 3,
    'f' : 4, 'h' : 4, 'v' : 4, 'w' : 4, 'y' : 4,
    'k' : 5, 
    'j' : 8, 'x' : 8,
    'q' : 10, 'z' : 10}

def signature(mot):
    """Paramètre : mot de type str
    Valeur renvoyée : un dictionnaire représentant le nombre d'occurences
    de chaque lettre minuscule de l'alphabet dans mot""" 
    sig  = {}  #dictionnaire vide
    for c in mot:
        "à compléter"
    return sig

#Tests unitaires de la fonction signature
assert signature("") == {}
assert signature("ananas") == {'a': 3, 'n': 2, 's': 1}
assert signature("abcd") == {'a': 1, 'b': 1, 'c': 1, 'd': 1}


def score_mot(mot, valeur):
    """Paramètre : mot de type str, 
    valeur de type dict associe à chaque lettre minuscule sa valeur au scrabble
    Valeur renvoyée : score du mot au scrabble""" 
    s = 0
    "à compléter"
    return s

#Tests unitaires de la fonction signature
assert score_mot("") == 0
assert score_mot("zazou") == 23
assert score_mot("ananas") == 6


def mot_possible(mot, sig_lettres):
    """Paramètre : mot de type str
    sig_lettres de type dict représente la signature des lettres disponibles
    Valeur renvoyée : un booléen indiquant si sig_mot compatible avec  sig_lettres
    et donc si le mot peut être composé avec les lettres fournies"""
    sig_mot = signature(mot)
    "à compléter"


#Tests unitaires de la fonction mot_possible
assert mot_possible("zazou", {"a" : 1, "b" : 1, "o" : 2, "u" : 1, "z" : 2}) == True
assert mot_possible("zazou", {"b" : 1, "o" : 1, "u" : 1, "z" : 2}) == False
assert mot_possible("zazou", {"a" : 1, "o" : 2, "u" : 3, "z" : 1}) == False

#Programme principal
# saisie du nombre de mots du dictionnaire
n = int(input())
# saisie des mots du dictionnaire dans une liste
dico = [input().rstrip() for _ in range(n)]
letters = input().rstrip()
sig_lettres = signature(letters)
smax = -1
mot_max = ""
# boucle sur les mots du dictionnaire
for mot in dico:
    "à compléter"


print(mot_max)
~~~

Attention, spoiler !  [solution](solution_scrabble.py)

