---
title : TP1 système d'exploitation et shell
subtitle: Thème architectures matérielles et systèmes d'exploitation
author : Première NSI,  [Lycée du Parc](https://frederic-junier.org/)
numbersections: true
fontsize: 11pt
geometry:
- top=20mm
- left=20mm
- right=20mm
- heightrounded    
--- 
  
<!-- Définition des hyperliens  -->

[Python]: https://docs.python.org/3/tutorial/datastructures.html
[Python-tutor]: http://pythontutor.com/visualize.html#mode=edit
[Laurent Bloch]: https://laurentbloch.net/MySpip3/IMG/pdf/histsys-screen-20200727.pdf
[BASH]: https://fr.wikipedia.org/wiki/Bourne-Again_shell
[Linux]: https://fr.wikipedia.org/wiki/Linux
[FreeBSD]: https://fr.wikipedia.org/wiki/FreeBSD
[MacOS]: https://fr.wikipedia.org/wiki/MacOS
[Windows]: https://fr.wikipedia.org/wiki/Microsoft_Windows
[UNIX]: https://fr.wikipedia.org/wiki/Unix

:::cours
Le [système d'exploitation](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27exploitation) est l'ensemble des programmes qui permet aux autres programmes d'interagir avec les ressources matérielles (processeur, mémoire, périphériques d'entrée / sortie) sur un ordinateur. Il sert donc *d'intermédiaire* entre le *matériel* et le *logiciel* et assure la coordination, la sécurité et la stabilité d'un environnement  partagés par plusieurs programmes et plusieurs utilisateurs.

Les systèmes d'exploitation les plus utilisés son [Windows][Windows], [MacOS][MacOS], [Linux][Linux] et [FreeBSD][FreeBSD], ces trois derniers étant dérivés du système [UNIX][UNIX].

Un *interpréteur de commandes* ou *shell* est un programme qui sert d'intermédiaire entre l'utilisateur et le système d'exploitation : son *interface* d'entrée / sortie peut être graphique ou textuelle.

Nous allons travailler sur  un *shell* avec interface textuelle nommé [BASH][BASH] qui est installé par défaut sur les systèmes [MacOS][MacOS] et [Linux][Linux].
:::

:::exercice
1. Ouvrir un terminal d'interpréteur de commandes avec le raccourci clavier `CTRL + ALT + T`.
2. Vérifier  son identité, le répertoire courant et la date avec les commandes suivantes :

        junier@fredportable:~$ whoami
        junier
        junier@fredportable:~$ pwd
        /home/junier
        junier@fredportable:~$ date
        lun. 17 août 2020 13:42:38 CEST



3. Télécharger l'archive du TP avec la commande `wget` en lui passant l'[URL][URL] en argument l'URL
 qui est <https://parc-nsi.github.io/premiere-nsi/chapitre9/TP1/materiel/sandbox.zip> (faire un copier-coller de cette URL dans l'interpréteur de commandes).

        junier@fredportable:~$ wget https://parc-nsi.github.io/premiere-nsi/chapitre9/TP1/materiel/sandbox.zip


4. Déballer l'archive avec la commande `unzip`.

        junier@fredportable:~$ unzip sandbox.zip
        junier@fredportable:~$ ls -ld sandbox
        drwxrwxr-x 28 junier junier 4096 août  15 22:29 sandbox

5. Changer de répertoire courant pour le répertoire `sandbox` avec la commande `cd` pour `change directory`.

        junier@fredportable:~$ cd sandbox
        junier@fredportable:~/sandbox$ ls
        a  c              consigne3.txt  e  g  i  k  m  o  q  s  u  w  y
        b  consigne1.txt  d              f  h  j  l  n  p  r  t  v  x  z


6. Afficher dans le terminal (ou console) le contenu du fichier `consigne1.txt`.

        junier@fredportable:~/sandbox$ cat consigne1.txt


7. Suivre les instructions données successivement dans les fichiers `consigne{1..8}.txt`.

L'objectif est de retrouver ou construire deux fichiers `systeme-cours.md` 
et `memento-shell.md` au format [Markdown](https://fr.wikipedia.org/wiki/Markdown) et de les convertir   en `pdf`  soit avec l'outil [pandoc]() s'il est installé, soit avec un convertisseur en ligne directement depuis le *shell* :

        junier@fredportable:~/sandbox$ pandoc systeme-cours.md -o systeme-cours.pdf

ou avec l'API du convertisseur en ligne `docverter`  et la commande `curl`: 

        junier@fredportable:~/sandbox$ curl \
        -F from=markdown \
        -F to=pdf \
        -F input_files[]=@systeme-cours.md  \
        -F table_of_contents=true  \
        http://c.docverter.com/convert > systeme-cours.pdf


8. À la fin du TP, copier avec la commande `cp`,  les fichiers `systeme-cours.pdf` et `memento-shell.pdf` qui ont été produits sur sa clef USB qui devrait être montée dans le dossier `media`. On peut afficher le point de montage avec `mount|grep media`.
:::


