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

def make_cible (grid, color):
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


def make_cible_title (grid, i, j, color):
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

def make_glisseur(grid, i, j,color):
    try:
        cases = grid.cases
        #glisseur
        cases [i + 56] [j + 83] ['s'] = life_status
        cases [i + 56] [j + 83] ['c'] = color
        cases [i + 56] [j + 84] ['s'] = life_status
        cases [i + 56] [j + 84] ['c'] = color
        cases [i + 55] [j + 84] ['s'] = life_status
        cases [i + 55] [j + 84] ['c'] = color
        cases [i + 55] [j + 85] ['s'] = life_status
        cases [i + 55] [j + 85] ['c'] = color
        cases [i + 57] [j + 85] ['s'] = life_status
        cases [i + 57] [j + 85] ['c'] = color
    except:
        pass
    return grid

def make_gun(grid, i, j,color):
    try:
        cases = grid.cases
        #glisseur
        cases [i + 2] [j + 0] ['s'] = life_status
        cases [i + 2] [j + 0] ['c'] = color
        cases [i + 3] [j + 0] ['s'] = life_status
        cases [i + 3] [j + 0] ['c'] = color

        cases [i + 1] [j + 1] ['s'] = life_status
        cases [i + 1] [j + 1] ['c'] = color
        cases [i + 4] [j + 1] ['s'] = life_status
        cases [i + 4] [j + 1] ['c'] = color
        cases [i + 5] [j + 1] ['s'] = life_status
        cases [i + 5] [j + 1] ['c'] = color

        cases [i + 0] [j + 2] ['s'] = life_status
        cases [i + 0] [j + 2] ['c'] = color
        cases [i + 2] [j + 2] ['s'] = life_status
        cases [i + 2] [j + 2] ['c'] = color
        cases [i + 3] [j + 2] ['s'] = life_status
        cases [i + 3] [j + 2] ['c'] = color
        cases [i + 6] [j + 2] ['s'] = life_status
        cases [i + 6] [j + 2] ['c'] = color

        cases [i + 1] [j + 3] ['s'] = life_status
        cases [i + 1] [j + 3] ['c'] = color
        cases [i + 4] [j + 3] ['s'] = life_status
        cases [i + 4] [j + 3] ['c'] = color
        cases [i + 7] [j + 3] ['s'] = life_status
        cases [i + 7] [j + 3] ['c'] = color
        cases [i + 11] [j + 3] ['s'] = life_status
        cases [i + 11] [j + 3] ['c'] = color
        cases [i + 12] [j + 3] ['s'] = life_status
        cases [i + 12] [j + 3] ['c'] = color
        cases [i + 16] [j + 3] ['s'] = life_status
        cases [i + 16] [j + 3] ['c'] = color
        cases [i + 17] [j + 3] ['s'] = life_status
        cases [i + 17] [j + 3] ['c'] = color
        cases [i + 18] [j + 3] ['s'] = life_status
        cases [i + 18] [j + 3] ['c'] = color
        cases [i + 20] [j + 3] ['s'] = life_status
        cases [i + 20] [j + 3] ['c'] = color

        cases [i + 2] [j + 4] ['s'] = life_status
        cases [i + 2] [j + 4] ['c'] = color
        cases [i + 5] [j + 4] ['s'] = life_status
        cases [i + 5] [j + 4] ['c'] = color
        cases [i + 8] [j + 4] ['s'] = life_status
        cases [i + 8] [j + 4] ['c'] = color
        cases [i + 10] [j + 4] ['s'] = life_status
        cases [i + 10] [j + 4] ['c'] = color
        cases [i + 13] [j + 4] ['s'] = life_status
        cases [i + 13] [j + 4] ['c'] = color
        cases [i + 15] [j + 4] ['s'] = life_status
        cases [i + 15] [j + 4] ['c'] = color
        cases [i + 19] [j + 4] ['s'] = life_status
        cases [i + 19] [j + 4] ['c'] = color
        cases [i + 21] [j + 4] ['s'] = life_status
        cases [i + 21] [j + 4] ['c'] = color

        cases [i + 3] [j + 5] ['s'] = life_status
        cases [i + 3] [j + 5] ['c'] = color
        cases [i + 6] [j + 5] ['s'] = life_status
        cases [i + 6] [j + 5] ['c'] = color
        cases [i + 9] [j + 5] ['s'] = life_status
        cases [i + 9] [j + 5] ['c'] = color
        cases [i + 11] [j + 5] ['s'] = life_status
        cases [i + 11] [j + 5] ['c'] = color
        cases [i + 12] [j + 5] ['s'] = life_status
        cases [i + 12] [j + 5] ['c'] = color
        cases [i + 14] [j + 5] ['s'] = life_status
        cases [i + 14] [j + 5] ['c'] = color
        cases [i + 20] [j + 5] ['s'] = life_status
        cases [i + 20] [j + 5] ['c'] = color
        cases [i + 22] [j + 5] ['s'] = life_status
        cases [i + 22] [j + 5] ['c'] = color

        cases [i + 4] [j + 6] ['s'] = life_status
        cases [i + 4] [j + 6] ['c'] = color
        cases [i + 7] [j + 6] ['s'] = life_status
        cases [i + 7] [j + 6] ['c'] = color
        cases [i + 10] [j + 6] ['s'] = life_status
        cases [i + 10] [j + 6] ['c'] = color
        cases [i + 13] [j + 6] ['s'] = life_status
        cases [i + 13] [j + 6] ['c'] = color
        cases [i + 15] [j + 6] ['s'] = life_status
        cases [i + 15] [j + 6] ['c'] = color
        cases [i + 16] [j + 6] ['s'] = life_status
        cases [i + 16] [j + 6] ['c'] = color
        cases [i + 20] [j + 6] ['s'] = life_status
        cases [i + 20] [j + 6] ['c'] = color
        cases [i + 22] [j + 6] ['s'] = life_status
        cases [i + 22] [j + 6] ['c'] = color

        cases [i + 5] [j + 7] ['s'] = life_status
        cases [i + 5] [j + 7] ['c'] = color
        cases [i + 8] [j + 7] ['s'] = life_status
        cases [i + 8] [j + 7] ['c'] = color
        cases [i + 11] [j + 7] ['s'] = life_status
        cases [i + 11] [j + 7] ['c'] = color
        cases [i + 14] [j + 7] ['s'] = life_status
        cases [i + 14] [j + 7] ['c'] = color
        cases [i + 16] [j + 7] ['s'] = life_status
        cases [i + 16] [j + 7] ['c'] = color
        cases [i + 19] [j + 7] ['s'] = life_status
        cases [i + 19] [j + 7] ['c'] = color
        cases [i + 22] [j + 7] ['s'] = life_status
        cases [i + 22] [j + 7] ['c'] = color

        cases [i + 6] [j + 8] ['s'] = life_status
        cases [i + 6] [j + 8] ['c'] = color
        cases [i + 9] [j + 8] ['s'] = life_status
        cases [i + 9] [j + 8] ['c'] = color
        cases [i + 12] [j + 8] ['s'] = life_status
        cases [i + 12] [j + 8] ['c'] = color
        cases [i + 13] [j + 8] ['s'] = life_status
        cases [i + 13] [j + 8] ['c'] = color
        cases [i + 16] [j + 8] ['s'] = life_status
        cases [i + 16] [j + 8] ['c'] = color
        cases [i + 18] [j + 8] ['s'] = life_status
        cases [i + 18] [j + 8] ['c'] = color
        cases [i + 20] [j + 8] ['s'] = life_status
        cases [i + 20] [j + 8] ['c'] = color
        cases [i + 21] [j + 8] ['s'] = life_status
        cases [i + 21] [j + 8] ['c'] = color

        cases [i + 7] [j + 9] ['s'] = life_status
        cases [i + 7] [j + 9] ['c'] = color
        cases [i + 10] [j + 9] ['s'] = life_status
        cases [i + 10] [j + 9] ['c'] = color
        cases [i + 13] [j + 9] ['s'] = life_status
        cases [i + 13] [j + 9] ['c'] = color
        cases [i + 16] [j + 9] ['s'] = life_status
        cases [i + 16] [j + 9] ['c'] = color
        cases [i + 17] [j + 9] ['s'] = life_status
        cases [i + 17] [j + 9] ['c'] = color
        cases [i + 18] [j + 9] ['s'] = life_status
        cases [i + 18] [j + 9] ['c'] = color
        cases [i + 19] [j + 9] ['s'] = life_status
        cases [i + 19] [j + 9] ['c'] = color
        cases [i + 21] [j + 9] ['s'] = life_status
        cases [i + 21] [j + 9] ['c'] = color

        cases [i + 8] [j + 10] ['s'] = life_status
        cases [i + 8] [j + 10] ['c'] = color
        cases [i + 11] [j + 10] ['s'] = life_status
        cases [i + 11] [j + 10] ['c'] = color
        cases [i + 13] [j + 10] ['s'] = life_status
        cases [i + 13] [j + 10] ['c'] = color
        cases [i + 21] [j + 10] ['s'] = life_status
        cases [i + 21] [j + 10] ['c'] = color
        cases [i + 22] [j + 10] ['s'] = life_status
        cases [i + 22] [j + 10] ['c'] = color

        cases [i + 9] [j + 11] ['s'] = life_status
        cases [i + 9] [j + 11] ['c'] = color
        cases [i + 12] [j + 11] ['s'] = life_status
        cases [i + 12] [j + 11] ['c'] = color
        cases [i + 14] [j + 11] ['s'] = life_status
        cases [i + 14] [j + 11] ['c'] = color
        cases [i + 20] [j + 11] ['s'] = life_status
        cases [i + 20] [j + 11] ['c'] = color
        cases [i + 23] [j + 11] ['s'] = life_status
        cases [i + 23] [j + 11] ['c'] = color

        cases [i + 10] [j + 12] ['s'] = life_status
        cases [i + 10] [j + 12] ['c'] = color
        cases [i + 13] [j + 12] ['s'] = life_status
        cases [i + 13] [j + 12] ['c'] = color
        cases [i + 15] [j + 12] ['s'] = life_status
        cases [i + 15] [j + 12] ['c'] = color
        cases [i + 16] [j + 12] ['s'] = life_status
        cases [i + 16] [j + 12] ['c'] = color
        cases [i + 20] [j + 12] ['s'] = life_status
        cases [i + 20] [j + 12] ['c'] = color
        cases [i + 24] [j + 12] ['s'] = life_status
        cases [i + 24] [j + 12] ['c'] = color

        cases [i + 11] [j + 13] ['s'] = life_status
        cases [i + 11] [j + 13] ['c'] = color
        cases [i + 12] [j + 13] ['s'] = life_status
        cases [i + 12] [j + 13] ['c'] = color
        cases [i + 13] [j + 13] ['s'] = life_status
        cases [i + 13] [j + 13] ['c'] = color
        cases [i + 14] [j + 13] ['s'] = life_status
        cases [i + 14] [j + 13] ['c'] = color
        cases [i + 15] [j + 13] ['s'] = life_status
        cases [i + 15] [j + 13] ['c'] = color
        cases [i + 17] [j + 13] ['s'] = life_status
        cases [i + 17] [j + 13] ['c'] = color
        cases [i + 18] [j + 13] ['s'] = life_status
        cases [i + 18] [j + 13] ['c'] = color
        cases [i + 19] [j + 13] ['s'] = life_status
        cases [i + 19] [j + 13] ['c'] = color
        cases [i + 25] [j + 13] ['s'] = life_status
        cases [i + 25] [j + 13] ['c'] = color
        cases [i + 26] [j + 13] ['s'] = life_status
        cases [i + 26] [j + 13] ['c'] = color

        cases [i + 12] [j + 14] ['s'] = life_status
        cases [i + 12] [j + 14] ['c'] = color
        cases [i + 14] [j + 14] ['s'] = life_status
        cases [i + 14] [j + 14] ['c'] = color
        cases [i + 20] [j + 14] ['s'] = life_status
        cases [i + 20] [j + 14] ['c'] = color
        cases [i + 27] [j + 14] ['s'] = life_status
        cases [i + 27] [j + 14] ['c'] = color

        cases [i + 13] [j + 15] ['s'] = life_status
        cases [i + 13] [j + 15] ['c'] = color
        cases [i + 21] [j + 15] ['s'] = life_status
        cases [i + 21] [j + 15] ['c'] = color
        cases [i + 28] [j + 15] ['s'] = life_status
        cases [i + 28] [j + 15] ['c'] = color
        cases [i + 29] [j + 15] ['s'] = life_status
        cases [i + 29] [j + 15] ['c'] = color

        cases [i + 22] [j + 16] ['s'] = life_status
        cases [i + 22] [j + 16] ['c'] = color
        cases [i + 30] [j + 16] ['s'] = life_status
        cases [i + 30] [j + 16] ['c'] = color

        cases [i + 23] [j + 17] ['s'] = life_status
        cases [i + 23] [j + 17] ['c'] = color
        cases [i + 31] [j + 17] ['s'] = life_status
        cases [i + 31] [j + 17] ['c'] = color

    except:
        pass
    return grid

def apply_game_of_life_rules_original (grid):
	previous_grid = grid
	previous_cases = previous_grid.cases
	cases = grid.cases # cases is a list of lists of dictionnaries
	next_grid = Grid (len (cases))
	next_cases = next_grid.cases
	for i in range (1, len (cases) - 1):
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
	return next_grid

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
        next_grid = make_cible(grid,'black')
    elif compteur == 1:
        next_grid = make_cible_title(grid,0,13,'red')
    elif compteur == 3 :
        next_grid = make_gun(grid, 65, 68, 'black')
    elif compteur == 57:
        next_grid = clean_grid(grid,67,75,0,70)
    elif compteur == 58:
        next_grid = make_viseur(grid,0,10,'red')
    elif compteur == 10:
        next_grid = make_glisseur(grid,4 ,-20 ,'red')
    elif compteur == 80:
        next_grid= make_cible(grid,'black')
    elif compteur > 80:
        next_grid = apply_game_of_life_rules_original (grid)
    else:
        time.sleep (0.2)
        next_grid = apply_game_of_life_rules(grid)
    return next_grid
