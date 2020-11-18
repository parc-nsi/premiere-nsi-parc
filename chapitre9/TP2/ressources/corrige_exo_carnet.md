~~~shell
junier@fredportable:~/TP-SHELL/carnet$ wget https://gitlab.com/frederic-junier/nsi-public/-/raw/master/Premiere/Systeme/TP2/contacts-1000.csv
--2020-08-18 14:58:22--  https://gitlab.com/frederic-junier/nsi-public/-/raw/master/Premiere/Systeme/TP2/contacts-1000.csv
Résolution de gitlab.com (gitlab.com)… 172.65.251.78, 2606:4700:90:0:f22e:fbec:5bed:a9b9
Connexion à gitlab.com (gitlab.com)|172.65.251.78|:443… connecté.
requête HTTP transmise, en attente de la réponse… 200 OK
Taille : non indiqué [text/plain]
Enregistre : «contacts-1000.csv»

contacts-1000.csv       [ <=>                ]  40,07K  --.-KB/s    ds 0,1s    

2020-08-18 14:58:23 (352 KB/s) - «contacts-1000.csv» enregistré [41032]

junier@fredportable:~/TP-SHELL/carnet$ ls
contacts-1000.csv
junier@fredportable:~/TP-SHELL/carnet$ head -n10 contacts-1000.csv 
Virginie de Da Silva,wleroux@jourdan.org
Michelle Moreau-Ruiz,albertcolette@noos.fr
Virginie de Da Silva,christophe38@yahoo.fr
Capucine Girard du Mathieu,perrotmarianne@dijoux.org
Pénélope Paris,penelope92@sfr.fr
Virginie de Da Silva,charlottebenoit@marques.org
Capucine Girard du Mathieu,oceane34@lemonnier.fr
Paul Millet,gcosta@bouygtel.fr
Pénélope Paris,cbonneau@da.com
Pénélope Paris,hchretien@mendes.com
junier@fredportable:~/TP-SHELL/carnet$ head -n3 contacts-1000.csv 
Virginie de Da Silva,wleroux@jourdan.org
Michelle Moreau-Ruiz,albertcolette@noos.fr
Virginie de Da Silva,christophe38@yahoo.fr
junier@fredportable:~/TP-SHELL/carnet$ tail -n3 contacts-1000.csv 
Virginie de Da Silva,alopes@perrot.fr
Virginie de Da Silva,bessonlouis@ifrance.com
Pénélope Paris,averdier@morvan.com
junier@fredportable:~/TP-SHELL/carnet$ echo "3 premieres lignes" ; head -n3 contacts-1000.csv 
3 premieres lignes
Virginie de Da Silva,wleroux@jourdan.org
Michelle Moreau-Ruiz,albertcolette@noos.fr
Virginie de Da Silva,christophe38@yahoo.fr
junier@fredportable:~/TP-SHELL/carnet$ echo "3 dernières  lignes" ; tail -n3 contacts-1000.csv 
3 dernières  lignes
Virginie de Da Silva,alopes@perrot.fr
Virginie de Da Silva,bessonlouis@ifrance.com
Pénélope Paris,averdier@morvan.com
junier@fredportable:~/TP-SHELL/carnet$ cat contacts-1000.csv | sort | head -n10
Anaïs de la Gerard,adriennechauveau@wanadoo.fr
Anaïs de la Gerard,aimeduhamel@godard.fr
Anaïs de la Gerard,alexandre77@prevost.fr
Anaïs de la Gerard,anouk25@gay.net
Anaïs de la Gerard,benoitmercier@club-internet.fr
Anaïs de la Gerard,margotvidal@caron.fr
Anaïs de la Gerard,potierhortense@maillet.com
Anaïs de la Gerard,theodore81@free.fr
Anaïs de la Gerard,ucollin@noos.fr
Capucine Girard du Mathieu,acourtois@lemonnier.com
junier@fredportable:~/TP-SHELL/carnet$ cat contacts-1000.csv | sort > contacts-1000-alpha.csv 
junier@fredportable:~/TP-SHELL/carnet$ cat contacts-1000.csv | cut -d , -f 1 | sort  
Anaïs de la Gerard
Anaïs de la Gerard
.............
junier@fredportable:~/TP-SHELL/carnet$ cat contacts-1000.csv | cut -d , -f 1 | sort  | uniq -c
      9 Anaïs de la Gerard
     67 Capucine Girard du Mathieu
      4 Danielle du Costa
      1 Danielle Le Roux
     12 Éric Roche
      7 Hortense Blondel
     12 Juliette Lombard
      2 Lucie Fischer
      1 Maurice Gillet
     34 Michelle Moreau-Ruiz
      3 Michel Mary
     31 Paul Millet
    396 Pénélope Paris
    148 Sabine de Gillet
      1 Véronique Chauvin-Perret
    272 Virginie de Da Silva
junier@fredportable:~/TP-SHELL/carnet$ cat contacts-1000.csv | cut -d , -f 1 | sort  | uniq -c | sort -n -r > top-mails.txt
junier@fredportable:~/TP-SHELL/carnet$ cat top-mails.txt 
    396 Pénélope Paris
    272 Virginie de Da Silva
    148 Sabine de Gillet
     67 Capucine Girard du Mathieu
     34 Michelle Moreau-Ruiz
     31 Paul Millet
     12 Juliette Lombard
     12 Éric Roche
      9 Anaïs de la Gerard
      7 Hortense Blondel
      4 Danielle du Costa
      3 Michel Mary
      2 Lucie Fischer
      1 Véronique Chauvin-Perret
      1 Maurice Gillet
      1 Danielle Le Roux
~~~
