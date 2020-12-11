import random

## Fonctions outils

def permute(tab, i, j):
    """
    Paramètres : 
        t un tableau de nombres  et element un nombre
    Postcondition : 
        permutation des éléments de t d'indices i et j
    """
    tab[i], tab[j] = tab[j], tab[i]
    
def inserer(element, tab):
    """
    Paramètres : 
        t un tableau de nombres trié dans l'ordre croissant
        element un nombre
    Postcondition : 
        insère element dans tab à sa place
    """
    tab.append(element)
    j = len(tab) - 1
    while j > 0 and tab[j - 1] > tab[j]:
        permute(tab, j - 1, j)
        j = j - 1

## k plus petits éléments 

def plus_petit(k, t):
    """"
    Paramètres : 
        k un entier
        t un tableau de nombres
    Précondition : 
        len(t) >= k  
    Valeur renvoyée : 
        un tableau de nombres contenant les k plus petits
        éléments de t
    """
    assert len(t) >= k
    kpetit = []
    if k == 0:
        return kpetit
    for i in range(len(t)):
        if  i < k or kpetit[k-1] > t[i]:
            inserer(t[i], kpetit)
            if len(kpetit) > k:
                kpetit.pop()
    return kpetit

def test_unitaire_plus_petit(fonction):
    for taille in range(0, 10):
        t = [random.randint(0, 100) for _ in range(taille)]
        for k in range(0, taille):
            assert plus_petit(k, t) == sorted(t)[:k]
    print(f"Tests unitaires réussis pour la fonction {fonction.__name__}")

# Décommenter pour effectuer les tests unitaires pour la fonction plus_petit

test_unitaire_plus_petit(plus_petit)

## Tri par dénombrement
    
def tri_denombrement(t, n):
    """
    Paramètre : t un tableau denombres et binf et bsup deux entiers
    Precondition : toutes les valeurs de t entre 0 et n
    Valeur renvoyée : un tableau où les éléments de t sont triés
    dans l'ordre croissant
    """
    histo = [0 for _ in range(n + 1)]
    for e in t:
        histo[e] = histo[e] + 1
    t_ordre = []
    for k in range(n + 1):
        t_ordre = t_ordre + [k for _ in range(histo[k])]
    return t_ordre
    
def tri_denombrement2(t, n):
    """
    Paramètre : t un tableau denombres et binf et bsup deux entiers
    Precondition : toutes les valeurs de t entre 0 et n
    Valeur renvoyée : un tableau où les éléments de t sont triés
    dans l'ordre croissant
    """
    if len(t) == 0:
        return []
    histo = [0 for _ in range(n + 1)]
    for e in t:
        histo[e] = histo[e] + 1
    t_ordre = [0 for _ in range(len(t))]
    k = 0
    i = 0
    while k <= n:
        if histo[k] > 0:
            histo[k] = histo[k] - 1
            t_ordre[i] = k
            i = i + 1
        else:
            k = k + 1
    return t_ordre
    
def test_unitaire_denombrement(fonction):
    for n in range(0, 10):
        for taille in range(0, 10):
            t = [random.randint(0, n) for _ in range(taille)]
            assert fonction(t, n) == sorted(t)
    print(f"Tests unitaires réussis pour la fonction {fonction.__name__}")
    
# Décommenter pour effectuer les tests unitaires pour la fonction tri_denombrement
test_unitaire_denombrement(tri_denombrement)
test_unitaire_denombrement(tri_denombrement2)



    