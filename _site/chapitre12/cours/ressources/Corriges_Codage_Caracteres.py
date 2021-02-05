#!/usr/bin/env python
# coding: utf-8

# # Corrigés des exercices du chapitre codage des caractères

# ## Exercice 1

# In[6]:


def miroir(chaine):
    """
    Paramètre : chaine de type str
    Valeur renvoyée : chaine de caractères miroir de chaine
    """
    res = ''
    for c in chaine:
        res = c + res
    return res


# In[5]:


miroir('Suis-je toujours la plus belle?')


# In[11]:


def palindrome(chaine):
    """
    Paramètre : chaine de type str
    Valeur renvoyée : un booléen indiquant si chaine est un palindrome
    Précondition : suppression des espaces d'abord
    Complexité : parcourt toute la chaine
    """
    chaine = chaine.replace(' ', '')
    return miroir(chaine) == chaine


# In[12]:


palindrome('caser vite ce palindrome ne mord ni lape cet ivre sac')


# In[13]:


def palindrome_moitie(chaine):
    """
    Paramètre : chaine de type str
    Valeur renvoyée : un booléen indiquant si chaine est un palindrome
    Précondition : suppression des espaces d'abord
    Complexité : parcourt la moitié de la chaine
    """
    chaine = chaine.replace(' ', '')
    n = len(chaine) - 1
    for k in range(len(chaine) // 2):
        if chaine[k] != chaine[n - k]:
            return False
    return True


# In[14]:


palindrome_moitie('anna')


# In[15]:


palindrome_moitie('anana')


# ## Exercice 2

# ### Table ASCII

# Les 32 premiers caractères ne sont pas imprimables.

# In[24]:


for a in range(8):
    for b in range(16):
        print(chr(a * 16 + b), end = " ")
    print()


# `caractere_plus_petit(c1, c2)`

# In[ ]:


def caractere_plus_petit(c1, c2):
    return ord(c1) <= ord(c2)


# `chaine_plus_petite(chaine1, chaine2)`

# In[29]:


def chaine_plus_petite(chaine1, chaine2):
    for k in range(min(len(chaine1), len(chaine2))):
        if chaine1[k] > chaine2[k]:
            return False
        elif chaine1[k] < chaine2[k]:
            return True
    return len(chaine1) <= len(chaine2)


# In[32]:


assert chaine_plus_petite('a', 'b') == True
assert chaine_plus_petite('a', 'a') == True
assert chaine_plus_petite('a', 'aa') == True
assert chaine_plus_petite('a', 'ab') == True
assert chaine_plus_petite('aa', 'ab') == True
assert chaine_plus_petite('ab', 'aa') == False


# In[33]:


def croissant(tab, comparaison):
    for k in range(len(tab) - 1):
        if not comparaison(tab[k],tab[k+1]):
            return False
    return True


# In[34]:


croissant(['Chat', 'Chien', 'Cheval', 'Cochon'], 
          chaine_plus_petite)


# In[36]:


croissant(['Chien', 'Cheval', 'Cochon', 'Chat'], 
          chaine_plus_petite)


# In[37]:


croissant(['Cochon', 'Chien', 'Cheval', 'Chat'], 
          chaine_plus_petite)


# ## Exercice 3 Codage ROT13

# In[30]:


def rot13(chaine):
    res = ''
    chaine = chaine.upper()
    origine = ord('A')
    for c in chaine:
        res = res + chr(origine + (ord(c) - origine + 13) % 26)
    return res


# In[31]:


rot13('ave cesar')


# ## Module `this` le Zen de Python

# Commençons par importer le module `this` de `Python` pour obtenir un court texte résumant la philosophie du langage

# In[25]:


import this


# In[ ]:


get_ipython().run_line_magic('psource', 'this')


# Ci-dessous le code source du module, expliquez le code :
# 
# ~~~python
# s = """Gur Mra bs Clguba, ol Gvz Crgref
# 
# Ornhgvshy vf orggre guna htyl.
# Rkcyvpvg vf orggre guna vzcyvpvg.
# Fvzcyr vf orggre guna pbzcyrk.
# Pbzcyrk vf orggre guna pbzcyvpngrq.
# Syng vf orggre guna arfgrq.
# Fcnefr vf orggre guna qrafr.
# Ernqnovyvgl pbhagf.
# Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
# Nygubhtu cenpgvpnyvgl orngf chevgl.
# Reebef fubhyq arire cnff fvyragyl.
# Hayrff rkcyvpvgyl fvyraprq.
# Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
# Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
# Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
# Abj vf orggre guna arire.
# Nygubhtu arire vf bsgra orggre guna *evtug* abj.
# Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
# Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
# Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""
# 
# d = {}
# for c in (65, 97):
#     for i in range(26):
#         d[chr(i+c)] = chr((i+13) % 26 + c)
# 
# print("".join([d.get(c, c) for c in s]))
# ~~~

# ## Exercice 4

# In[63]:


def valeur(mot):
    v = 1
    for c in mot:
        v = v * (ord(c) - ord('a') + 1)
    return v

def indice_maximum(tab):
    """Renvoie l'index du maximum du tableau de nombres tab"""
    imax = 0
    for k in range(1, len(tab)):
        if tab[k] > tab[imax]:
            imax = k
    return imax    
    
f = open('dico.txt')
histo = [0 for _ in range(1000)]
for mot in f:
    v = valeur(mot.rstrip())    
    if 2000 <= v < 3000:
        #print(mot, v)
        histo[v - 2000] = histo[v - 2000] + 1
f.close()
annee_max = 2000 + indice_maximum(histo)
print(annee_max)


# ## Exercice 7

# valeur en décimal (base 10) du point de code U+ABCD .

# In[65]:


int(0xABCD)


# caractère dont le point de code est U+263A

# In[68]:


'\U0000263A'


# In[69]:


pointcode = 0x263A
print(pointcode)
for k in range(10):
    print(chr(pointcode))
    pointcode = pointcode + 1


# Le code affiche précédent les caractères correspondants aux points de codes compris (en hexadécimal) entre 263A (9786 en décimal) et 263A + 10 (9796 en décimal)

# In[70]:


0x263A


# In[71]:


0x263A + 10


# In[72]:


print("\U0001f600")


# In[90]:


hex(0x1F600 + 79)


# In[92]:


for pointcode in range(0x1F600, 0x1F650):
    print(chr(pointcode), end = ' ')
    if pointcode % 16 == 15:
        print()


# ## Exercice 8

# ### Fonction unicode

# In[93]:


def unicode(s):
    """Affiche les caractères d'une chaine, leur point de code et leurs octets codants en hexadécimal
    et en binaire"""
    for caractere in s:
        octets = caractere.encode("utf-8")
        octets_hexa = [hex(oct) for oct in octets]
        octets_bin = [bin(oct) for oct in octets]
        print("Caractère : {} | Point de code  : {} | Octets (hexa) : {} | Octets (binaire) : {}".format(caractere,ord(caractere),octets_hexa, octets_bin))

def unicode2(s):
    print("Caractères : ")
    for c in s:
        print(c, end=",")
    print("\n\nPoints de code : ")
    for c in s:
        print(ord(c),end=",")
    octets = s.encode("utf-8")
    print("\n\nOctets codants en hexadécimal : ")
    for c in octets:
        print(hex(c), end=',')
    print("\n\nOctets codants en binaire : ")
    for c in octets:
        print(bin(c), end=',')
        
def unicode3(s):
    """Affiche les caractères d'une chaine, leur point de code et leurs octets codants en hexadécimal
    et en binaire"""
    for caractere in s:
        octets = caractere.encode("utf-8")
        octets_hexa = [format(b,'x') for b in octets]
        octets_bin = [format(b,'08b') for b in octets]
        print("Caractère : {} | Point de code  : {} | Octets (hexa) : {} | Octets (binaire) : {}".format(caractere,ord(caractere),octets_hexa, octets_bin))

    
        


# In[94]:


unicode("lycée")


# In[13]:


unicode2("lycée")


# In[14]:


unicode3("lycée")


# ### Encodage UTF-8 d'un caractère en hexadécimal, décimal et binaire

# In[15]:


etoile = chr(8902)


# In[16]:


etoile_octet = etoile.encode('utf8')


# In[17]:


etoile_octet


# In[18]:


etoile_liste_octet = [bin(octet) for octet in etoile_octet]
print(etoile_liste_octet)


# In[19]:


etoile_liste_decimal = [octet for octet in etoile_octet]
print(etoile_liste_decimal)


# ### Nombre de caractères codés par une chaine d'octets en UTF-8

# In[20]:


def longueur(b):
    """Retourne le nombre de caractères encodé par une 
    chaine d'octets en utf8"""
    k = 0
    long = 0
    while k < len(b):
        #attention les représentations binaires des octets ne sont pas remplies par des 0 à gauche
        binaire = bin(b[k]).lstrip('0b').zfill(8)
        #decimal = b[k]
        long += 1
        if binaire[0] == '0':
            k += 1
        elif binaire[:3] == '110':
            k += 2
        elif binaire[:4] == '1110':
            k += 3
        else:
            k += 4
    return long     


# In[21]:


longueur(etoile.encode('utf8'))


# In[22]:


chaine = 'élémentaire mon cher Watson'.encode('utf8')


# In[23]:


longueur('élémentaire mon cher Watson'.encode('utf8'))


# In[24]:


len('élémentaire mon cher Watson')


# In[25]:


chaine = 'élémentaire mon cher Watson'.encode('utf8')


# In[26]:


type(chaine)


# In[27]:


len(chaine)


# In[28]:


chaine


# In[29]:


'1110'.zfill(8)

