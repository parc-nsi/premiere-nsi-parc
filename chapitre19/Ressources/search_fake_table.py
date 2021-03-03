import csv
import sys



def extraire_table(file):
    csvfile = open('clients.csv', mode ='r', encoding='utf8',newline='')
    reader = csv.DictReader(csvfile,delimiter=',')
    table = []
    for row in reader:
        table.append(dict(row))
    csvfile.close()
    return table

if __name__ == "__main__":
    try:
        table = extraire_table(sys.argv[1])
    except:
        table = extraire_table('clients.csv')
    finally:
        #print(table[:5])
        #Clients dans le Rhone
        #clients_rhone = [client for client in table if client['département'] == '69']
        #print(len(clients_rhone))
        #Clients ayant dépensé plus de 1000 euros
        #depense_plus_mille = [client for client in table if float(client['dépenses']) >= 1000]
        #print(len(depense_plus_mille), depense_plus_mille[:5])
        #Tri des cllents par ordre croissant de dépenses
        def clef_depenses(client):
            return float(client['dépenses'])
        
        #extract1  = sorted(table, key = clef_depenses)
        #print(extract[:5])
        #Tri des cllents par ordre décroissant des dépenses            
        #extract2 = sorted(table, key = clef_depenses, reverse = True)
        #print(extract[:5])
        #Tris lexicographiques des clients par ordre croissant des départements et des visites
        #en permutant l'ordre des clefs
        def clef_departement_visites(client):
            return (client['département'], int(client['visites']))
        def clef_visites_departement(client):
            return (int(client['visites']), client['département'])
        extract3 = sorted(table, key = clef_visites_departement)
        extract4 = sorted(table, key = clef_departement_visites)
        print(extract3[:5])
        # print(extract4[:10])
        # print(extract3[:10] == extract4[:10])
        # print(extract3 == extract4)

        #Tri des clients par ordre croissant des départements puis décroissant des visites
        # Enchainement de tris, inversion par rapport à l'ordre lexicographique
        # Possibilité de choisir  des ordres différents selon les clefs de tri
        def clef_departement(client):
            return client['département']

        def clef_visites(client):
            return int(client['visites'])

        print('\n' * 3)
        extract5 = sorted(table, key = clef_visites)
        #print(extract5[:10])
        #print('\n' * 3)
        extract6 = sorted(extract5, key = clef_departement)
        print(extract6[:5])
        print(extract4 == extract6)

        print('\n' * 5)
        extract7 = sorted(table, key = clef_departement)
        print(extract7[:10])
        print('\n' * 5)
        extract8 = sorted(extract7, key = clef_visites)
        print(extract8[:10])
        print(extract3 == extract8)
        
