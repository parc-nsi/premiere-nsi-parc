#!/usr/bin/env python
# -*- coding: utf-8 -*-

#%% Exercice 1 : données exif

#Laisser le code en commentaire
# Nécessite d'installer le programme exiftool
# Puis le module pyexiftool
# fjunier@fjunier:~/sandbox$ sudo apt install libimage-exiftool-perl
# fjunier@fjunier:~/sandbox$ pip3 install --user pyexiftool
# fjunier@fjunier:~/sandbox$ chmod +x exiftool_test.py 
# fjunier@fjunier:~/sandbox$ ls -l exiftool_test.py 
# -rwxrwxr-x 1 fjunier fjunier 355 févr. 24 21:50 exiftool_test.py
"""
import sys
import exiftool

def extraire_exif(fichier):
    et = exiftool.ExifTool()
    et.start()
    metadata = et.get_metadata(fichier)
    et.terminate()
    return metadata

#code client exécuté si script exécuté directement
if __name__ == "__main__": 
    #extrait les données exif du fichier passé en paramètre
    print(extraire_exif(sys.argv[1]))
"""

#Exécution sur l'image http://frederic-junier.org/SNT/images/20181230_162625.jpg
"""
fjunier@fjunier:~/sandbox$ ./exiftool_test.py image_mystere.jpg 
{, 'EXIF:Make': 'samsung', 'EXIF:Model': 'SM-G930F', 'EXIF:Orientation': 1, 'EXIF:XResolution': 72,
 'EXIF:YResolution': 72, 'EXIF:ResolutionUnit': 2, 'EXIF:Software': 'G930FXXU3ERL3', 'EXIF:ModifyDate': '2018:12:30 16:26:24', 'EXIF:YCbCrPositioning': 1, 'EXIF:ExposureTime': 0.0005733944954, 'EXIF:FNumber': 1.7, 'EXIF:ExposureProgram': 2, 'EXIF:ISO': 50,
 'EXIF:ExifVersion': '0220', 'EXIF:DateTimeOriginal': '2018:12:30 16:26:24', 'EXIF:CreateDate': '2018:12:30 16:26:24', 'EXIF:ComponentsConfiguration': '1 2 3 0', 'EXIF:ShutterSpeedValue': '0.000572673315054629', 'EXIF:ApertureValue': 1.6993699982773, 'EXIF:BrightnessValue': 8.36,
 'EXIF:ExposureCompensation': 0, 'EXIF:MaxApertureValue': 1.6993699982773, 'EXIF:MeteringMode': 2,
 'EXIF:Flash': 0, 'EXIF:FocalLength': 4.2, 'EXIF:UserComment': '', 'EXIF:SubSecTime': '0999',
 ., 'EXIF:FlashpixVersion': '0100', 'EXIF:ColorSpace': 1, 'EXIF:ExifImageWidth': 4032, 'EXIF:ExifImageHeight': 3024, , 'EXIF:GPSVersionID': '2 2 0 0', 'EXIF:GPSLatitudeRef': 'N',
 'EXIF:GPSLatitude': 42.4947222222222, 'EXIF:GPSLongitudeRef': 'E', 'EXIF:GPSLongitude': 3.13,
 'EXIF:GPSAltitudeRef': 0, 'EXIF:GPSAltitude': 123, 'EXIF:GPSTimeStamp': '15:26:35','EXIF:GPSDateStamp': '2018:12:30', .
 }
 """


#%% Création de dictionnaires

#%% Création par extension 

def dico_par_extension():
    processeur1 = {'annee' : 1974, 'fabricant' : 'Intel', 'Frequence' : '2 MHz','gravure' : '6000 nm', 'architecture' : '8080'}
    processeur2 = dict([('annee', 1978), ('fabricant', 'Intel'),('Frequence','5 MHz'),('gravure','3 micrometres'),('architecture','8086')])
    print("processeur 1 : ", processeur1)
    print("processeur 2 : ", processeur2)
    print("Accès à la clef 'gravure' du dictionnaire processeur1 avec processeur1['gravure'] : ",
    processeur1['gravure'])
    print("Accès à la clef 'gravure' du dictionnaire processeur2 avec processeur1['gravure'] : ",
    processeur2['gravure'])

#Décommenter pour exécuter
#dico_par_extension()
#%% Création par compréhension

def dico_par_comprehension():
    tab_tuple = [('annee', 1989), ('fabricant', 'Intel'),('Frequence','25 MHz'),('gravure','600 nm'),('architecture','80486')]
    processeur3 = { clef : valeur for clef, valeur in tab_tuple }
    print("Processeur3 : ", processeur3)

#Décommenter pour exécuter
#dico_par_comprehension()

#%% Exercice 2

#compléter ici

#décommenter pour exécuter les tests
#assert ordinal == {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106}
#assert caractere == {97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j'}

#%% Ajout et suppression
def dico_ajout_suppression():
    nobel2019 = {}
    nobel2019['Littérature'] = 'Peter Handke'
    assert nobel2019 == {'Littérature': 'Peter Handke'}
    print("nobel2019=",nobel2019)
    nobel2019['Paix'] = 'Kim Joon Hyun'
    assert nobel2019 == {'Littérature': 'Peter Handke', 'Paix': 'Kim Joon Hyun'}
    print("nobel2019=",nobel2019)
    nobel2019['Paix'] = 'Abiy Ahmed'
    assert nobel2019 ==  {'Littérature': 'Peter Handke', 'Paix': 'Abiy Ahmed'}
    print("nobel2019=",nobel2019)
    nobel2019['Maths'] = 'Cédric Villani'
    assert nobel2019 ==  {'Littérature': 'Peter Handke', 'Paix': 'Abiy Ahmed', 'Maths': 'Cédric Villani'}
    print("nobel2019=",nobel2019)
    del nobel2019['Maths']
    assert nobel2019 ==  {'Littérature': 'Peter Handke', 'Paix': 'Abiy Ahmed'}
    print("nobel2019=",nobel2019)


#Décommenter pour exécuter
#dico_ajout_suppression()

#%% Immutabilité des dictionnaires

def dico_immutable():
    jouet =dict()
    jouet[2] = 'clef de type int'
    jouet[True] = 'clef de type bool'
    jouet[(1,2)] = 'clef de type tuple'
    print("jouet = ", jouet)
    assert jouet == {2: 'clef de type int', True: 'clef de type bool', (1, 2): 'clef de type tuple'}
    jouet[[1,2]] = 'clef de type list -> impossible'

#Décommenter pour exécuter
#dico_immutable()

#%% Dictionnaire structure imbriquée

def dico_imbrique():
    vols = {'Lisbonne': {'heure': '21:10','num': 'EJU7674','compagnie': 'EASYJET'},
    'Vienne': {'heure': '21:25','num': 'OS430','compagnie': 'AUSTRIAN AIRLINES'},
    'Londres': {'heure': '21:55','num': 'BA357','compagnie': 'BRITISH AIRWAYS'}}
    print("vols['Londres']", vols['Londres'])
    {'heure': '21:55', 'num': 'BA357', 'compagnie': 'BRITISH AIRWAYS'}
    tab_dico_airports = [{'nom': 'Total Rf Heliport','latitude': '40.07080078125', 'longitude': '-74.93360137939453',
    'altitude': '11',  'code_pays': 'US'},
    {'nom': 'Aero B Ranch Airport',  'latitude': '38.704022',  'longitude': '-101.473911',
    'altitude': '3435',  'code_pays': 'US'}]
    print("tab_dico_airports[1]", tab_dico_airports)

#Décommenter pour exécuter
#dico_imbrique()

#%%Méthode get

def dico_get():
    prix_turing2006 = {'nom' : 'Frances Allen', 'sujet' : 'Optimisation des compilateurs'}
    try:
        print(prix_turing2006['pays'])
    except KeyError:
        print("Erreur d'accès car clef manquante, nouvel essai avec get qui renvoie :")
        print(prix_turing2006.get('pays'))

#Décommenter pour exécuter
#dico_get()

#%% 


#Décommenter pour exécuter
#dico_get()

#%% Parcours de dictionnaire

def dico_parcours():
    dico = { 'Paul' : '0640507080', 'Marie' : '0742516483', 'Hicham' : '0987416543'}
    print("Parcours par clef 1")
    for clef in dico:
        print("Clef -> ", clef)
    print("Parcours par clef 2")
    for clef in dico.keys():
        print("Clef -> ", clef)
    print("Parcours par valeurs")
    for val in dico.values():
        print("Valeur -> ", val)
    print("Parcours par couples (clef,valeur)")
    for (clef, val) in dico.items():
        print("Clef ->", clef, " Valeur ->", val)

#Décommenter pour exécuter
#dico_parcours()
