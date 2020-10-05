def sum_subarray(tab, i, j):
    """Retourne la somme des éléments du sous-tableau tab[i:j + 1]"""
    assert 0 <= i <= j < len(tab)   # précondition
    s = 0
    for k in range(i, j + 1):
        s = s + tab[k]
    return s

def maximum_sum_subarray1(tab):
    """Retourne le maximum des sommes d'éléments
    de sous-tableaux de tab.
    Complexité cubique"""
    max_sum_global = float('-inf')
    for i in range(0, len(tab)):
        for j in range(i, len(tab)):
            s = sum_subarray(tab, i, j)
            if s > max_sum_global:
                max_sum_global = s
    return max_sum_global


def maximum_sum_subarray2(tab):  
    """"Retourne le maximum des sommes d'éléments
    de sous-tableaux de tab.
    Complexité linéaire"""  
    max_sum_partial = tab[0]
    max_sum_global = max_sum_partial
    for k in range(1, len(tab)):
        if max_sum_partial > 0:
            max_sum_partial = max_sum_partial + tab[k]
        else:
            max_sum_partial = tab[k]
        if max_sum_partial > max_sum_global:
            max_sum_global = max_sum_partial
    return max_sum_global           