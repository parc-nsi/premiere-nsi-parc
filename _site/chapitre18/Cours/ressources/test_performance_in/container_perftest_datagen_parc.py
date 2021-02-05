"""
Generate data for container performance test

Auteur : Luciano Ramalho "Fluent Python"
Source : https://github.com/fluentpython/example-code-2e/tree/master/03-dict-set/support
"""

import random
import array

#varaibles globales
MAX_EXPONENT = 7
HAYSTACK_LEN = 10 ** MAX_EXPONENT
NEEDLES_LEN = 10 ** (MAX_EXPONENT - 1)
SAMPLE_LEN = HAYSTACK_LEN + NEEDLES_LEN // 2


#ensemble de SAMPLE_LEN  flottants double précision
sample = {1/random.random() for i in range(SAMPLE_LEN)}
print('initial sample: %d elements' % len(sample))

#un ensemble n'a pas de doublons
#on complète l'ensemble jusqu'à obtenir une taille de SAMPLE_LEN 
#tant qu'il y a des doublons
# SAMPLE_LEN correspond
while len(sample) < SAMPLE_LEN:
    sample.add(1/random.random())

print('complete sample: %d elements' % len(sample))

#création d'un tableau de flottants double précision 
#à partir de l'échantillon sans doublons sample
#au passage sample passe du type set au type array (typage dynamique en Python)
sample = array.array('d', sample)
#mélange de sample
random.shuffle(sample)

#on sélectionne NEEDLES_LEN // 2 (égal à 500 000) flottants dans sample
not_selected = sample[:NEEDLES_LEN // 2]
print('not selected: %d samples' % len(not_selected))
print('  writing not_selected.arr')
#on les enregistre dans le  fichier binaire not_selected.arr
#de taille 500 000 * 8 = 4 000 0000 octets
#avantage du type array : les flottants double précision sont codés sur 8 octets comme en C
with open('not_selected.arr', 'wb') as fp:
    not_selected.tofile(fp)

#on sélectionne  les autres flottants de sample (soit 10 000 000)
selected = sample[NEEDLES_LEN // 2:]
print('selected: %d samples' % len(selected))
print('  writing selected.arr')
#on les enregistre dans le  fichier binaire selected.arr
with open('selected.arr', 'wb') as fp:
    selected.tofile(fp)
