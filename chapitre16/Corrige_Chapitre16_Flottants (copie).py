#!/usr/bin/env python
# coding: utf-8

# # Exercice 4

# In[35]:


def position_virgule(c):
    """
    Paramètre : c une chaine représentant un décimal avec une virgule
    Valeur renvoyée : position de la virgule
    """
    for k in range(len(c)):
        if c[k] == ',':
            return k
        

def ChaineBinDec(c):
    """
    Paramètre : c une une chaîne de caractères
    c représentant un nombre à virgule écrit en binaire
    Valeur renvoyée : nombre flottant correspondant
    """
    pos_virgule = position_virgule(c)
    puissance = 2 ** (pos_virgule - 1)
    val = 0
    for bit in c:
        if bit != ',':
            val = val + int(bit) * puissance
            puissance = puissance / 2
    return val
    
    
def ChaineBinDec2(c):
    """
    Paramètre : c une une chaîne de caractères
    c représentant un nombre à virgule écrit en binaire
    Valeur renvoyée : nombre flottant correspondant
    """
    partie_entiere = 0
    i = 0
    while c[i] != ',':
        partie_entiere = partie_entiere * 2 + int(c[i])
        i = i + 1
    #print(partie_entiere)
    j = len(c) - 1
    partie_frac = 0
    while c[j] != ',':
        partie_frac = (partie_frac  + int(c[j])) / 2
        j = j - 1
    return partie_entiere + partie_frac


# In[38]:


# Tests
assert ChaineBinDec('1,101') == 1.625
assert ChaineBinDec2('1,101') == 1.625
assert ChaineBinDec('101,001') == 5.125
assert ChaineBinDec2('101,001') == 5.125


# # Exercice 6

# Convertisseur en ligne : <https://www.h-schmidt.net/FloatConverter/IEEE754.html>

# Déterminer les bits de la représentation en double précision du nombre $x=0,01203125$.
# 
# * On détermine d'abord le bit de signe : $x$ est positif donc $s=0$
# * Ensuite on multiplie successivement par $2$ pour décaler les bits vers la gauche :
#   

# In[110]:


def decimal_vers_IEE754(x, taille_exposant, taille_mantisse):
    #print("détermination du signe")
    if x > 0:
        print("Bit de signe  : 0")
    elif x <0:
        print("Bit de signe : 1")
    else:
        print("O valeur particulière")
    if x != 0:
        #print("détermination de l'exposant")
        exposant = 0
        while int(x) >= 1:
            x = x / 2
            exposant = exposant + 1
        while int(x) == 0:
            x = x * 2
            exposant = exposant - 1           
        decalage = 2 ** (taille_exposant - 1) - 1
        print("Exposant en décimal : ", exposant)
        print(f"Exposant décalé  de  + {decalage} : ", exposant + decalage)
        print(f"Exposant décalé de + {decalage}  : codage binaire sur 11 bits : ", bin(exposant + decalage).lstrip('0b').zfill(taille_exposant))
        #print("détermination des bits de mantisse")
        x = x - 1
        nbits = 0
        mantisse = []
        while nbits < taille_mantisse:
            x = x * 2
            partie_entiere = int(x)
            mantisse.append(str(partie_entiere))
            if partie_entiere == 1:
                x = x - partie_entiere
            nbits = nbits + 1
        print("Mantisse : ", ''.join(mantisse))


# Le développement binaire de $0.01203125$ est illimité !

# In[111]:


# en binary32  : 8 bits d'exposant et 23 bits de mantisse
decimal_vers_IEE754(0.01203125, 8, 23)


# Vérification avec le convertisseur en ligne <https://www.h-schmidt.net/FloatConverter/IEEE754.html>
# 
# 
# ![convertisseur](convertisseur.png)

# In[106]:


# en binary64  : 11 bits d'exposant et 32 bits de mantisse
decimal_vers_IEE754(0.01203125, 11, 32)


# In[103]:


# vérification avec le module Decimal
import decimal
decimal.Decimal.from_float(0.01203125)


# Un flottant représenté de façon exacte

# In[100]:


decimal_vers_IEE754(1/2 + 1/2**2 + 1/2**22, 8,23)


# $0,1$ n'est pas représenté de façon exacte !

# In[82]:


decimal_vers_IEE754(0.1, 11, 52)


# In[112]:


decimal_vers_IEE754(14.5, 8, 23)


# In[98]:


# aujourd'hui 21/01/2021
2021 + 21 / 365


# In[99]:


decimal_vers_IEE754(2021 + 21 / 365, 8, 23)


# In[107]:


decimal_vers_IEE754(9 + 1/2 + 1/2 ** 2 + 1/2 ** 5, 11, 52)


# In[108]:


9 + 1/2 + 1/2 ** 2 + 1/2 ** 5


# In[113]:


decimal_vers_IEE754(9 + 1/2 + 1/2 ** 2 + 1/2 ** 5, 11, 52)

