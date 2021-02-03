def infini_pos():
    x = 1.
    n = 0
    while x != 2*x:
        n = n + 1
        x = x*2
    return n, x

def infini_neg():
    x = -1.
    n = 0
    while x != 2*x:
        n = n + 1
        x = x*2
    return n, x

def vers_zero():
    x = 1.
    n = 0
    while x >0:
        n = n + 1
        x = x/2
    return n, x

def div_mult(n):
    x = 1.1
    for k in range(n):
        x = 1+(x-1) /3
    for k in range(n):
        x = 1+(x-1) *3
    return x

def subdivision(a, b, n):
    """ Renvois une liste de n flottants régulièrement
    répartis entre a (compris) et b (non compris) """
    
    L = [a]
    x = a
    pas = (b - a)/n
    
    while x != b:
        x = x + pas
        L.append(x)

    return L

def suite(n):
    (a, b) = (0.2, 0.1)
    for k in range(n):
        (a, b) = (b, 2.5*b -a)
    return a
    
