import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def signature(mot):
    sig  = dict()
    for c in mot:
        if c not in sig:
            sig[c] = 1
        else:
            sig[c] = sig[c] + 1
    return sig

def score_mot(mot):
    s = 0
    for c in mot:
        s = s + valeur[c]
    return s

def mot_possible(mot, sig_lettres):
    sig_mot = signature(mot)
    for c in sig_mot:
        if c not in sig_lettres or sig_mot[c] > sig_lettres[c]:
            return False
    return True

valeur = {
    'a' : 1,
    'e' : 1,
    'i' : 1,
    'o' : 1,
    'n' : 1,
    'r' : 1,
    't' : 1,
    'l' : 1,
    's' : 1,
    'u' : 1,
    'd' : 2,
    'g' : 2,
    'b' : 3, 'c' : 3, 'm' : 3, 'p' : 3,
    'f' : 4, 'h' : 4, 'v' : 4, 'w' : 4, 'y' : 4,
    'k' : 5, 
    'j' : 8, 'x' : 8,
    'q' : 10, 'z' : 10}


n = int(input())
dico = [input().rstrip() for _ in range(n)]
letters = input().rstrip()
sig_lettres = signature(letters)
smax = -1
for mot in dico:
    if mot_possible(mot, sig_lettres):
        score = score_mot(mot)
        if score > smax:
            smax = score
            mot_max = mot

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(mot_max)
