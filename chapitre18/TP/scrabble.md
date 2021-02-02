---
title:  TP scrabble
layout: parc
---


## Présentation de la structure de données dictionnaires

* [Présentation par Pierre Marquestaut](https://peertube.lyceeconnecte.fr/videos/watch/86be0059-a3c1-41ec-952a-79dea6310c87)

* En Python la structure de données __dictionnaire__ est implémentée par le type `dict`. Voici un  exemple d'implémentation avec les opérations de base : définition, accès en lecture / écriture,test d'appartenance, parcours.


<pre data-executable>
annuaire = { 'Victor' : '06 44 44 44 44'}
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





  <script src="https://github.com/parc-nsi/premiere-nsi/assets/js/juniper.min.js"></script>
  <script>new Juniper({ repo: 'parc-nsi/premiere-nsi', isolateCells: false , theme: 'monokai'})</script>