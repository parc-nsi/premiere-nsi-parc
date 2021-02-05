#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import faker
import sys
import random

NB_EMAIL =  int(sys.argv[1])
FICHIER_SORTIE = sys.argv[2]
fake = faker.Faker('fr_FR')

def generer_mail():
    return [fake.email() for _ in range(NB_EMAIL)]


def generer_nom():
    return [fake.name() for _ in range(NB_EMAIL)]


def decoupage_aleatoire(n, decoupage):
    if n <= 0:
        return [0] + decoupage
    if n == 1:
        return [0, 1] + decoupage
    print(n, decoupage)
    coupe = random.randint(n//2, n)
    decoupage =  [coupe] + decoupage
    #print(decoupage)
    return  decoupage_aleatoire(coupe - 1, decoupage)

les_mails = generer_mail()
urne_noms = generer_nom()
decoupage = decoupage_aleatoire(NB_EMAIL - 1, [NB_EMAIL])
les_noms = []
for k in range(1, len(decoupage)):
    nom = urne_noms.pop()
    les_noms += [nom] * (decoupage[k] - decoupage[k-1])
les_contacts = [(mail, nom) for (mail, nom) in zip(les_mails, les_noms)]
# print(len(les_contacts))
random.shuffle(les_contacts)
with open(FICHIER_SORTIE, 'w') as f:
    for (mail, contact) in les_contacts:
        f.write(','.join([contact, mail]) + '\n')
    

