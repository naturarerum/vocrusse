#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Olivier
#
# Created:     23-07-2016
#-------------------------------------------------------------------------------
# TODO modifier les entetes
import tkinter as tk
import random
import codecs

# Variables Globales
ficIn = 'D:\\Temp\\russe_vocabulearn.txt'


f = codecs.open(ficIn, encoding='utf-8')
listVoc = []
for line in f:
    #print(line)
    splitted = line.rstrip().split(",")
    listVoc.append(splitted)
    count = 0

# print(listVoc)


def choix_question(langue_choisie):
    """choix aleatoire d un element source ou cible"""

    value = langue_choisie
    un_element = random.choice(listVoc)
    if value == 'Russe':
        langue_source = (un_element[0])
    else:
        langue_source = (un_element[1])
    print(langue_source)
    print(un_element)
    print(value)
    return langue_source



"""cresultat = choix_question()
print(resultat)


def check_reponse(rep):
    question = resultat
    if rep == question:
        statut = 1
    else:
        statut = 0
    return statut

finale = check_reponse("pomme")
print(finale)"""



