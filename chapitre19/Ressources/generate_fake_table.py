#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from faker import Faker
import csv
import datetime
import random
import re

def remove_accents(string):   
    string = re.sub("[àáâãäå]", 'a', string)
    string = re.sub("[èéêë]", 'e', string)
    string = re.sub("[ìíîï]", 'i', string)
    string = re.sub("[òóôõö]", 'o', string)
    string = re.sub("[ùúûü]", 'u', string)
    string = re.sub("[ýÿ]", 'y', string)

    return string


fake = Faker('fr_FR')
Faker.seed(0)   #pour générer toujours les mêmes données
DESCRIPTEURS = ['nom','prénom','email','département',
             'naissance','visites','dépenses']
DICO_MAILS  = dict()
NB_CLIENT = 50000
NB_TRANSACTIONS = 1000


def generer_client():
    visites = random.randint(2, 151)
    panier_moyen = random.randint(2, 151) + random.random()
    depenses = round(visites * panier_moyen, 2)
    _, domaine = fake.ascii_free_email().split('@')
    prenom = fake.first_name()
    nom = fake.last_name_nonbinary()
    email = remove_accents(prenom[0].lower()) + remove_accents(nom.lower()) + '@' + domaine
    if email in DICO_MAILS:
        index_mail = DICO_MAILS[email] + 1
        DICO_MAILS[email] = index_mail
        email = remove_accents(prenom[0].lower()) + remove_accents(nom.lower()) + str(index_mail) + '@' + domaine        
    else:
        DICO_MAILS[email] = 0
    return {'nom' : nom,
            'prénom': prenom,
            'email' :  email,
            'département'  : fake.department_number(),
            'naissance' : fake.date_between(datetime.date(1940,1,1),datetime.date(2005,12,31)).strftime('%Y-%m-%d'),
            'visites' : str(visites),
            'dépenses' : str(depenses)
            }

def generer_client_avec_erreurs():
    visites = random.randint(2, 151)
    if random.random() < 0.05:
        visites = -visites
    panier_moyen = random.randint(2, 151) + random.random()
    depenses = round(visites * panier_moyen, 2)
    if random.random() < 0.05:
        depenses = -depenses
    _, domaine = fake.ascii_free_email().split('@')
    prenom = fake.first_name()
    nom = fake.last_name_nonbinary()
    if random.random() < 0.05:        
        if random.random() < 0.8:
            email = remove_accents(prenom[0].lower()) + remove_accents(nom.lower()) + '.' + domaine
        else:
            email = ''
    else:
        email = remove_accents(prenom[0].lower()) + remove_accents(nom.lower()) + '@' + domaine
    if email in DICO_MAILS:
        index_mail = DICO_MAILS[email] + 1
        DICO_MAILS[email] = index_mail
        email = remove_accents(prenom[0].lower()) + remove_accents(nom.lower()) + str(index_mail) + '@' + domaine        
    else:
        DICO_MAILS[email] = 0
    if random.random() < 0.1:
        naissance = str(random.randint(2004, 2020)) + '-' + str(random.randint(10, 16)) + '-' + str(random.randint(28, 35))
    else:
        naissance = fake.date_between(datetime.date(1940,1,1),datetime.date(2005,12,31)).strftime('%Y-%m-%d')
    if random.random() < 0.1:
        departement = ['96', '977', '978', '2C'][random.randint(0, 3)]
    else:
        departement = fake.department_number()
    return {'nom' : nom,
            'prénom': prenom,
            'email' :  email,
            'département'  : departement,
            'naissance' : naissance,
            'visites' : str(visites),
            'dépenses' : str(depenses)
            }


csvfile = open('clients.csv', mode ='w', encoding='utf8',newline='')
writer = csv.DictWriter(csvfile, fieldnames = DESCRIPTEURS, delimiter=',')
writer.writeheader()
for _ in range(NB_CLIENT):
    writer.writerow(generer_client())
csvfile.close()
csvfile = open('transactions.csv', mode ='w', encoding='utf8',newline='')
writer = csv.DictWriter(csvfile, fieldnames = ['email','dépenses'], delimiter=',')
writer.writeheader()
LISTE_MAILS = list(DICO_MAILS.keys())
for _ in range(NB_TRANSACTIONS):
    writer.writerow({'email' : LISTE_MAILS[random.randint(0, len(LISTE_MAILS ) - 1)],  'dépenses' : round(random.randint(2, 151) + random.random(), 2)})
csvfile.close()
csvfile = open('clients_avec_erreurs.csv', mode ='w', encoding='utf8',newline='')
writer = csv.DictWriter(csvfile, fieldnames = DESCRIPTEURS, delimiter=',')
writer.writeheader()
for _ in range(1000):
    writer.writerow(generer_client_avec_erreurs())
csvfile.close()