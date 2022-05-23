# Créé par pouillieute, le 07/04/2022 en Python 3.7

# -*- coding: utf-8 -*-
"""

"""

from os import listdir
from os.path import isfile, join
import random
import time
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from jdlv_data import *
from jdlv_model import *
from jdlv_outils import *

def clean_grid (grid,i_min,i_max,j_min,j_max):
    if i_min != None and i_max != None \
      and j_min != None and j_max != None:
        for i in range (i_min,i_max):
            for j in range (j_min,j_max):
                grid.cases [i][j]['s'] = death_status
                grid.cases [i][j]['c'] = death_color
    else:
        for i in range (default_grid_size):
            for j in range (default_grid_size):
                grid.cases [i][j]['s'] = death_status
                grid.cases [i][j]['c'] = death_color
    return grid

def make_conway (grid, color):
    try:
        #grid = clean_grid (grid)
        cases = grid.cases
        for i in range (17, 42, 24) :
            for j in range (29, 54) :
                cases [i + 10] [j] ['s'] = life_status
                cases [i + 10] [j] ['c'] = color
        for j in range (29, 54, 24) :
            for i in range (17, 42) :
                cases [i + 10] [j] ['s'] = life_status
                cases [i + 10] [j] ['c'] = color

        for i in range (21, 38, 16) :
            for j in range (33, 50) :
                cases [i + 10] [j] ['s'] = life_status
                cases [i + 10] [j] ['c'] = color
        for j in range (33, 50, 16) :
            for i in range (21, 38) :
                cases [i + 10] [j] ['s'] = life_status
                cases [i + 10] [j] ['c'] = color

        for i in range (25, 34, 8) :
            for j in range (37, 46) :
                cases [i + 10] [j] ['s'] = life_status
                cases [i + 10] [j] ['c'] = color
        for j in range (37, 46, 8) :
            for i in range (25, 34) :
                cases [i + 10] [j] ['s'] = life_status
                cases [i + 10] [j] ['c'] = color

        for i in range (28, 31, 2) :
            for j in range (40, 43) :
                cases [i + 10] [j] ['s'] = life_status
                cases [i + 10] [j] ['c'] = color
        for j in range (40, 43, 2) :
            for i in range (28, 31) :
                cases [i + 10] [j] ['s'] = life_status
                cases [i + 10] [j] ['c'] = color
    except:
        pass
    return grid


def make_cible (grid, i, j, color):
    try:
        #grid = clean_grid (grid)
        cases = grid.cases
    #mot CIBLE
    #lettre C
        #ligne horizontale haut du C
        cases [i + 68] [j + 11] ['s'] = life_status
        cases [i + 68] [j + 11] ['c'] = color
        cases [i + 68] [j + 12] ['s'] = life_status
        cases [i + 68] [j + 12] ['c'] = color
        cases [i + 68] [j + 13] ['s'] = life_status
        cases [i + 68] [j + 13] ['c'] = color
        cases [i + 68] [j + 14] ['s'] = life_status
        cases [i + 68] [j + 14] ['c'] = color
        cases [i + 68] [j + 15] ['s'] = life_status
        cases [i + 68] [j + 15] ['c'] = color
        #ligne horizontale bas du C
        cases [i + 74] [j + 11] ['s'] = life_status
        cases [i + 74] [j + 11] ['c'] = color
        cases [i + 74] [j + 12] ['s'] = life_status
        cases [i + 74] [j + 12] ['c'] = color
        cases [i + 74] [j + 13] ['s'] = life_status
        cases [i + 74] [j + 13] ['c'] = color
        cases [i + 74] [j + 14] ['s'] = life_status
        cases [i + 74] [j + 14] ['c'] = color
        cases [i + 74] [j + 15] ['s'] = life_status
        cases [i + 74] [j + 15] ['c'] = color
        #ligne verticale du C
        cases [i + 68] [j + 11] ['s'] = life_status
        cases [i + 68] [j + 11] ['c'] = color
        cases [i + 69] [j + 11] ['s'] = life_status
        cases [i + 69] [j + 11] ['c'] = color
        cases [i + 70] [j + 11] ['s'] = life_status
        cases [i + 70] [j + 11] ['c'] = color
        cases [i + 71] [j + 11] ['s'] = life_status
        cases [i + 71] [j + 11] ['c'] = color
        cases [i + 72] [j + 11] ['s'] = life_status
        cases [i + 72] [j + 11] ['c'] = color
        cases [i + 73] [j + 11] ['s'] = life_status
        cases [i + 73] [j + 11] ['c'] = color
    #lettre I
        #ligne horizontale haut du I
        cases [i + 68] [j + 19] ['s'] = life_status
        cases [i + 68] [j + 19] ['c'] = color
        cases [i + 68] [j + 20] ['s'] = life_status
        cases [i + 68] [j + 20] ['c'] = color
        cases [i + 68] [j + 21] ['s'] = life_status
        cases [i + 68] [j + 21] ['c'] = color
        cases [i + 68] [j + 22] ['s'] = life_status
        cases [i + 68] [j + 22] ['c'] = color
        cases [i + 68] [j + 23] ['s'] = life_status
        cases [i + 68] [j + 23] ['c'] = color
        #ligne verticale du I
        cases [i + 68] [j + 21] ['s'] = life_status
        cases [i + 68] [j + 21] ['c'] = color
        cases [i + 69] [j + 21] ['s'] = life_status
        cases [i + 69] [j + 21] ['c'] = color
        cases [i + 70] [j + 21] ['s'] = life_status
        cases [i + 70] [j + 21] ['c'] = color
        cases [i + 71] [j + 21] ['s'] = life_status
        cases [i + 71] [j + 21] ['c'] = color
        cases [i + 72] [j + 21] ['s'] = life_status
        cases [i + 72] [j + 21] ['c'] = color
        cases [i + 72] [j + 21] ['c'] = color
        cases [i + 73] [j + 21] ['s'] = life_status
        cases [i + 73] [j + 21] ['c'] = color
        #ligne horizontale bas du I
        cases [i + 74] [j + 19] ['s'] = life_status
        cases [i + 74] [j + 19] ['c'] = color
        cases [i + 74] [j + 19] ['s'] = life_status
        cases [i + 74] [j + 19] ['c'] = color
        cases [i + 74] [j + 20] ['s'] = life_status
        cases [i + 74] [j + 20] ['c'] = color
        cases [i + 74] [j + 21] ['s'] = life_status
        cases [i + 74] [j + 21] ['c'] = color
        cases [i + 74] [j + 22] ['s'] = life_status
        cases [i + 74] [j + 22] ['c'] = color
        cases [i + 74] [j + 23] ['s'] = life_status
        cases [i + 74] [j + 23] ['c'] = color
    #lettre B
        #ligne vertical gauche B
        cases [i + 68] [j + 27] ['s'] = life_status
        cases [i + 68] [j + 27] ['c'] = color
        cases [i + 69] [j + 27] ['s'] = life_status
        cases [i + 69] [j + 27] ['c'] = color
        cases [i + 70] [j + 27] ['s'] = life_status
        cases [i + 70] [j + 27] ['c'] = color
        cases [i + 71] [j + 27] ['s'] = life_status
        cases [i + 71] [j + 27] ['c'] = color
        cases [i + 72] [j + 27] ['s'] = life_status
        cases [i + 72] [j + 27] ['c'] = color
        cases [i + 73] [j + 27] ['s'] = life_status
        cases [i + 73] [j + 27] ['c'] = color
        #ligne horizontale bas du B
        cases [i + 74] [j + 27] ['s'] = life_status
        cases [i + 74] [j + 27] ['c'] = color
        cases [i + 74] [j + 28] ['s'] = life_status
        cases [i + 74] [j + 28] ['c'] = color
        cases [i + 74] [j + 29] ['s'] = life_status
        cases [i + 74] [j + 29] ['c'] = color
        cases [i + 74] [j + 30] ['s'] = life_status
        cases [i + 74] [j + 30] ['c'] = color
        #ligne horizontale haut
        cases [i + 68] [j + 27] ['s'] = life_status
        cases [i + 68] [j + 27] ['c'] = color
        cases [i + 68] [j + 28] ['s'] = life_status
        cases [i + 68] [j + 28] ['c'] = color
        cases [i + 68] [j + 29] ['s'] = life_status
        cases [i + 68] [j + 29] ['c'] = color
        cases [i + 68] [j + 30] ['s'] = life_status
        cases [i + 68] [j + 30] ['c'] = color
        #ligne horizontale mileu du B
        cases [i + 71] [j + 27] ['s'] = life_status
        cases [i + 71] [j + 27] ['c'] = color
        cases [i + 71] [j + 28] ['s'] = life_status
        cases [i + 71] [j + 28] ['c'] = color
        cases [i + 71] [j + 29] ['s'] = life_status
        cases [i + 71] [j + 29] ['c'] = color
        cases [i + 71] [j + 30] ['s'] = life_status
        cases [i + 71] [j + 30] ['c'] = color
        #ligne verticale droite du B
        cases [i + 69] [j + 31] ['s'] = life_status
        cases [i + 69] [j + 31] ['c'] = color
        cases [i + 70] [j + 31] ['s'] = life_status
        cases [i + 70] [j + 31] ['c'] = color
        cases [i + 72] [j + 31] ['s'] = life_status
        cases [i + 72] [j + 31] ['c'] = color
        cases [i + 73] [j + 31] ['s'] = life_status
        cases [i + 73] [j + 31] ['c'] = color
    #lettre L
        #ligne verticale du L
        cases [i + 68] [j + 34] ['s'] = life_status
        cases [i + 68] [j + 34] ['c'] = color
        cases [i + 69] [j + 34] ['s'] = life_status
        cases [i + 69] [j + 34] ['c'] = color
        cases [i + 70] [j + 34] ['s'] = life_status
        cases [i + 70] [j + 34] ['c'] = color
        cases [i + 71] [j + 34] ['s'] = life_status
        cases [i + 71] [j + 34] ['c'] = color
        cases [i + 72] [j + 34] ['s'] = life_status
        cases [i + 72] [j + 34] ['c'] = color
        cases [i + 73] [j + 34] ['s'] = life_status
        cases [i + 73] [j + 34] ['c'] = color
        #ligne horizontale bas du L
        cases [i + 74] [j + 34] ['s'] = life_status
        cases [i + 74] [j + 34] ['c'] = color
        cases [i + 74] [j + 35] ['s'] = life_status
        cases [i + 74] [j + 35] ['c'] = color
        cases [i + 74] [j + 36] ['s'] = life_status
        cases [i + 74] [j + 36] ['c'] = color
        cases [i + 74] [j + 37] ['s'] = life_status
        cases [i + 74] [j + 37] ['c'] = color
        cases [i + 74] [j + 38] ['s'] = life_status
        cases [i + 74] [j + 38] ['c'] = color
    #lettre E
        #ligne vertical gauche E
        cases [i + 68] [j + 41] ['s'] = life_status
        cases [i + 68] [j + 41] ['c'] = color
        cases [i + 69] [j + 41] ['s'] = life_status
        cases [i + 69] [j + 41] ['c'] = color
        cases [i + 70] [j + 41] ['s'] = life_status
        cases [i + 70] [j + 41] ['c'] = color
        cases [i + 71] [j + 41] ['s'] = life_status
        cases [i + 71] [j + 41] ['c'] = color
        cases [i + 72] [j + 41] ['s'] = life_status
        cases [i + 72] [j + 41] ['c'] = color
        cases [i + 73] [j + 41] ['s'] = life_status
        cases [i + 73] [j + 41] ['c'] = color
        #ligne horizontale bas du E
        cases [i + 74] [j + 41] ['s'] = life_status
        cases [i + 74] [j + 41] ['c'] = color
        cases [i + 74] [j + 42] ['s'] = life_status
        cases [i + 74] [j + 42] ['c'] = color
        cases [i + 74] [j + 43] ['s'] = life_status
        cases [i + 74] [j + 43] ['c'] = color
        cases [i + 74] [j + 44] ['s'] = life_status
        cases [i + 74] [j + 44] ['c'] = color
        cases [i + 74] [j + 45] ['s'] = life_status
        cases [i + 74] [j + 45] ['c'] = color
        #ligne horizontale haut du E
        cases [i + 68] [j + 41] ['s'] = life_status
        cases [i + 68] [j + 41] ['c'] = color
        cases [i + 68] [j + 42] ['s'] = life_status
        cases [i + 68] [j + 42] ['c'] = color
        cases [i + 68] [j + 43] ['s'] = life_status
        cases [i + 68] [j + 43] ['c'] = color
        cases [i + 68] [j + 44] ['s'] = life_status
        cases [i + 68] [j + 44] ['c'] = color
        cases [i + 68] [j + 45] ['s'] = life_status
        cases [i + 68] [j + 45] ['c'] = color
        #ligne horizontale mileu du E
        cases [i + 71] [j + 41] ['s'] = life_status
        cases [i + 71] [j + 41] ['c'] = color
        cases [i + 71] [j + 42] ['s'] = life_status
        cases [i + 71] [j + 42] ['c'] = color
        cases [i + 71] [j + 43] ['s'] = life_status
        cases [i + 71] [j + 43] ['c'] = color
        cases [i + 71] [j + 44] ['s'] = life_status
        cases [i + 71] [j + 44] ['c'] = color


    except:
        pass
    return grid


def make_viseur(grid, i, j, color):
    try:
        #grid = clean_grid (grid)
        cases = grid.cases
        #mot VISEUR
    #lettre V
        #partie gauche
        cases [i + 68] [j + 11] ['s'] = life_status
        cases [i + 68] [j + 11] ['c'] = color
        cases [i + 69] [j + 11] ['s'] = life_status
        cases [i + 69] [j + 11] ['c'] = color
        cases [i + 70] [j + 12] ['s'] = life_status
        cases [i + 70] [j + 12] ['c'] = color
        cases [i + 71] [j + 12] ['s'] = life_status
        cases [i + 71] [j + 12] ['c'] = color
        cases [i + 72] [j + 13] ['s'] = life_status
        cases [i + 72] [j + 13] ['c'] = color
        cases [i + 73] [j + 13] ['s'] = life_status
        cases [i + 73] [j + 13] ['c'] = color
        cases [i + 74] [j + 14] ['s'] = life_status
        cases [i + 74] [j + 14] ['c'] = color
        #partie droite
        cases [i + 68] [j + 17] ['s'] = life_status
        cases [i + 68] [j + 17] ['c'] = color
        cases [i + 69] [j + 17] ['s'] = life_status
        cases [i + 69] [j + 17] ['c'] = color
        cases [i + 70] [j + 16] ['s'] = life_status
        cases [i + 70] [j + 16] ['c'] = color
        cases [i + 71] [j + 16] ['s'] = life_status
        cases [i + 71] [j + 16] ['c'] = color
        cases [i + 72] [j + 15] ['s'] = life_status
        cases [i + 72] [j + 15] ['c'] = color
        cases [i + 73] [j + 15] ['s'] = life_status
        cases [i + 73] [j + 15] ['c'] = color
    #lettre I
        #ligne horizontale haut du I
        cases [i + 68] [j + 19] ['s'] = life_status
        cases [i + 68] [j + 19] ['c'] = color
        cases [i + 68] [j + 20] ['s'] = life_status
        cases [i + 68] [j + 20] ['c'] = color
        cases [i + 68] [j + 21] ['s'] = life_status
        cases [i + 68] [j + 21] ['c'] = color
        cases [i + 68] [j + 22] ['s'] = life_status
        cases [i + 68] [j + 22] ['c'] = color
        cases [i + 68] [j + 23] ['s'] = life_status
        cases [i + 68] [j + 23] ['c'] = color
        #ligne verticale du I
        cases [i + 68] [j + 21] ['s'] = life_status
        cases [i + 68] [j + 21] ['c'] = color
        cases [i + 69] [j + 21] ['s'] = life_status
        cases [i + 69] [j + 21] ['c'] = color
        cases [i + 70] [j + 21] ['s'] = life_status
        cases [i + 70] [j + 21] ['c'] = color
        cases [i + 71] [j + 21] ['s'] = life_status
        cases [i + 71] [j + 21] ['c'] = color
        cases [i + 72] [j + 21] ['s'] = life_status
        cases [i + 72] [j + 21] ['c'] = color
        cases [i + 73] [j + 21] ['s'] = life_status
        cases [i + 73] [j + 21] ['c'] = color
        #ligne horizontale bas du I
        cases [i + 74] [j + 19] ['s'] = life_status
        cases [i + 74] [j + 19] ['c'] = color
        cases [i + 74] [j + 19] ['s'] = life_status
        cases [i + 74] [j + 19] ['c'] = color
        cases [i + 74] [j + 20] ['s'] = life_status
        cases [i + 74] [j + 20] ['c'] = color
        cases [i + 74] [j + 21] ['s'] = life_status
        cases [i + 74] [j + 21] ['c'] = color
        cases [i + 74] [j + 22] ['s'] = life_status
        cases [i + 74] [j + 22] ['c'] = color
        cases [i + 74] [j + 23] ['s'] = life_status
        cases [i + 74] [j + 23] ['c'] = color
    #lettre S
        cases [i + 68] [j + 27] ['s'] = life_status
        cases [i + 68] [j + 27] ['c'] = color
        cases [i + 68] [j + 28] ['s'] = life_status
        cases [i + 68] [j + 28] ['c'] = color
        cases [i + 68] [j + 29] ['s'] = life_status
        cases [i + 68] [j + 29] ['c'] = color
        cases [i + 69] [j + 26] ['s'] = life_status
        cases [i + 69] [j + 26] ['c'] = color
        cases [i + 70] [j + 26] ['s'] = life_status
        cases [i + 70] [j + 26] ['c'] = color
        cases [i + 74] [j + 26] ['s'] = life_status
        cases [i + 74] [j + 26] ['c'] = color
        cases [i + 74] [j + 27] ['s'] = life_status
        cases [i + 74] [j + 27] ['c'] = color
        cases [i + 74] [j + 28] ['s'] = life_status
        cases [i + 74] [j + 28] ['c'] = color
        cases [i + 73] [j + 29] ['s'] = life_status
        cases [i + 73] [j + 29] ['c'] = color
        cases [i + 72] [j + 29] ['s'] = life_status
        cases [i + 72] [j + 29] ['c'] = color
        cases [i + 72] [j + 29] ['s'] = life_status
        cases [i + 72] [j + 29] ['c'] = color
        cases [i + 71] [j + 27] ['s'] = life_status
        cases [i + 71] [j + 27] ['c'] = color
        cases [i + 71] [j + 28] ['s'] = life_status
        cases [i + 71] [j + 28] ['c'] = color
    #lettre E
        #ligne vertical gauche E
        cases [i + 68] [j + 32] ['s'] = life_status
        cases [i + 68] [j + 32] ['c'] = color
        cases [i + 69] [j + 32] ['s'] = life_status
        cases [i + 69] [j + 32] ['c'] = color
        cases [i + 70] [j + 32] ['s'] = life_status
        cases [i + 70] [j + 32] ['c'] = color
        cases [i + 71] [j + 32] ['s'] = life_status
        cases [i + 71] [j + 32] ['c'] = color
        cases [i + 72] [j + 32] ['s'] = life_status
        cases [i + 72] [j + 32] ['c'] = color
        cases [i + 73] [j + 32] ['s'] = life_status
        cases [i + 73] [j + 32] ['c'] = color
        #ligne horizontale bas du E
        cases [i + 74] [j + 32] ['s'] = life_status
        cases [i + 74] [j + 32] ['c'] = color
        cases [i + 74] [j + 33] ['s'] = life_status
        cases [i + 74] [j + 33] ['c'] = color
        cases [i + 74] [j + 34] ['s'] = life_status
        cases [i + 74] [j + 34] ['c'] = color
        cases [i + 74] [j + 35] ['s'] = life_status
        cases [i + 74] [j + 35] ['c'] = color
        cases [i + 74] [j + 36] ['s'] = life_status
        cases [i + 74] [j + 36] ['c'] = color
        #ligne horizontale haut du E
        cases [i + 68] [j + 32] ['s'] = life_status
        cases [i + 68] [j + 32] ['c'] = color
        cases [i + 68] [j + 33] ['s'] = life_status
        cases [i + 68] [j + 33] ['c'] = color
        cases [i + 68] [j + 34] ['s'] = life_status
        cases [i + 68] [j + 34] ['c'] = color
        cases [i + 68] [j + 35] ['s'] = life_status
        cases [i + 68] [j + 35] ['c'] = color
        cases [i + 68] [j + 36] ['s'] = life_status
        cases [i + 68] [j + 36] ['c'] = color
        #ligne horizontale mileu du E
        cases [i + 71] [j + 32] ['s'] = life_status
        cases [i + 71] [j + 32] ['c'] = color
        cases [i + 71] [j + 33] ['s'] = life_status
        cases [i + 71] [j + 33] ['c'] = color
        cases [i + 71] [j + 34] ['s'] = life_status
        cases [i + 71] [j + 34] ['c'] = color
        cases [i + 71] [j + 35] ['s'] = life_status
        cases [i + 71] [j + 35] ['c'] = color
    #lettre U
        #ligne verticale gauche du U
        cases [i + 68] [j + 39] ['s'] = life_status
        cases [i + 68] [j + 39] ['c'] = color
        cases [i + 69] [j + 39] ['s'] = life_status
        cases [i + 69] [j + 39] ['c'] = color
        cases [i + 70] [j + 39] ['s'] = life_status
        cases [i + 70] [j + 39] ['c'] = color
        cases [i + 71] [j + 39] ['s'] = life_status
        cases [i + 71] [j + 39] ['c'] = color
        cases [i + 72] [j + 39] ['s'] = life_status
        cases [i + 72] [j + 39] ['c'] = color
        cases [i + 73] [j + 39] ['s'] = life_status
        cases [i + 73] [j + 39] ['c'] = color
        #ligne verticale droite du U
        cases [i + 68] [j + 44] ['s'] = life_status
        cases [i + 68] [j + 44] ['c'] = color
        cases [i + 69] [j + 44] ['s'] = life_status
        cases [i + 69] [j + 44] ['c'] = color
        cases [i + 70] [j + 44] ['s'] = life_status
        cases [i + 70] [j + 44] ['c'] = color
        cases [i + 71] [j + 44] ['s'] = life_status
        cases [i + 71] [j + 44] ['c'] = color
        cases [i + 72] [j + 44] ['s'] = life_status
        cases [i + 72] [j + 44] ['c'] = color
        cases [i + 73] [j + 44] ['s'] = life_status
        cases [i + 73] [j + 44] ['c'] = color
        #ligne horizontale du U
        cases [i + 74] [j + 40] ['s'] = life_status
        cases [i + 74] [j + 40] ['c'] = color
        cases [i + 74] [j + 41] ['s'] = life_status
        cases [i + 74] [j + 41] ['c'] = color
        cases [i + 74] [j + 42] ['s'] = life_status
        cases [i + 74] [j + 42] ['c'] = color
        cases [i + 74] [j + 43] ['s'] = life_status
        cases [i + 74] [j + 43] ['c'] = color
    #lettre R
        #ligne verticale gauche du R
        cases [i + 68] [j + 47] ['s'] = life_status
        cases [i + 68] [j + 47] ['c'] = color
        cases [i + 69] [j + 47] ['s'] = life_status
        cases [i + 69] [j + 47] ['c'] = color
        cases [i + 70] [j + 47] ['s'] = life_status
        cases [i + 70] [j + 47] ['c'] = color
        cases [i + 71] [j + 47] ['s'] = life_status
        cases [i + 71] [j + 47] ['c'] = color
        cases [i + 72] [j + 47] ['s'] = life_status
        cases [i + 72] [j + 47] ['c'] = color
        cases [i + 73] [j + 47] ['s'] = life_status
        cases [i + 73] [j + 47] ['c'] = color
        cases [i + 74] [j + 47] ['s'] = life_status
        cases [i + 74] [j + 47] ['c'] = color
        #ligne horizontale haut du R
        cases [i + 68] [j + 48] ['s'] = life_status
        cases [i + 68] [j + 48] ['c'] = color
        cases [i + 68] [j + 49] ['s'] = life_status
        cases [i + 68] [j + 49] ['c'] = color
        cases [i + 68] [j + 50] ['s'] = life_status
        cases [i + 68] [j + 50] ['c'] = color
        #ligne horizontale milieu du R
        cases [i + 71] [j + 48] ['s'] = life_status
        cases [i + 71] [j + 48] ['c'] = color
        cases [i + 71] [j + 49] ['s'] = life_status
        cases [i + 71] [j + 49] ['c'] = color
        cases [i + 71] [j + 50] ['s'] = life_status
        cases [i + 71] [j + 50] ['c'] = color
        #ligne verticale droite du R
        cases [i + 69] [j + 51] ['s'] = life_status
        cases [i + 69] [j + 51] ['c'] = color
        cases [i + 70] [j + 51] ['s'] = life_status
        cases [i + 70] [j + 51] ['c'] = color
        cases [i + 74] [j + 51] ['s'] = life_status
        cases [i + 74] [j + 51] ['c'] = color
        #fin du R
        cases [i + 72] [j + 49] ['s'] = life_status
        cases [i + 72] [j + 49] ['c'] = color
        cases [i + 73] [j + 50] ['s'] = life_status
        cases [i + 73] [j + 50] ['c'] = color


    except:
        pass
    return grid

def apply_game_of_life_rules (grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, 67):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            nbre_alive_voisins = count_alive_voisins (voisins)
            if nbre_alive_voisins == 3:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    for i in range (67, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            next_cases [i] [j] = cases [i] [j]
    return next_grid


def apply_rules (grid, compteur):
    print(compteur)
    if compteur == 0:
        print ("COMPTEUR % 5  is  0")
        next_grid = make_conway(grid,'black')
    elif compteur == 1:
        next_grid = make_cible(grid,0,13,'red')
    elif compteur == 57:
        next_grid = clean_grid(grid,67,75,0,70)
    elif compteur == 58:
        next_grid = make_viseur(grid,0,10,'red')
    else:
        print ("COMPTEUR % 5 is NOT 0")
        time.sleep (0.2)
        next_grid = apply_game_of_life_rules(grid)
    return next_grid
