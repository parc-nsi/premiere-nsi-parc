#import de la bibliothèque graphique
import matplotlib.pyplot as plt
#graduations de l'axe des abscisses
plt.xticks(list(range(1, 4)), ['T1', 'T2', 'T3'], rotation = 60)
#légende de l'axe des abscisses
plt.xlabel('Trimestres')
#limites des abscisses
plt.xlim(0, 4)
#graduations de l'axe des ordonnées
plt.yticks([5,10,15,20], ['D', 'C', 'B', 'A'])
#légende de l'axe des ordonnées
plt.ylabel('Moyennes')
#limite des ordonnées
plt.ylim(0,20)
#affichage de la grille
plt.grid()
#Titre du graphique
plt.title('Élève X année scolaire 2016/2017')
#liste d'abscisses
x = list(range(1, 4))
#liste d'ordonnées
y = [6,17,12]
#graphique avec des points bleus reliés en pointillés
plt.plot(x, y,'bo:')
#affichage du graphique
plt.show()
#enregistrement sur disque du graphique
plt.savefig('eleve-X-2016-2017.png')