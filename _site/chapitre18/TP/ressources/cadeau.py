# -*- coding: utf-8 -*-

import re
from random import random
import matplotlib.pyplot as plt
import numpy as np

def nettoyerFichier(fichier):
    f = open(fichier, 'r')
    data = f.read()
    data = re.sub(r'[^\w\s]', ' ', data)
    data = re.sub(r'\s+',' ', data)
    f.close()
    return data.lower()