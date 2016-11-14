#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Olivier
#
# Created:     23-07-2016
#-------------------------------------------------------------------------------
# TODO modifier les entetes
import random
import codecs

ficIn = 'D:\\Temp\\russe_vocabulearn.txt'


f = codecs.open(ficIn, encoding='utf-8')
listVoc = []
for line in f:
    print(line)
    splitted = line.rstrip().split(",")
    listVoc.append(splitted)
    count = 0

# print(listVoc)


def choix_question():
    """choix aleatoire d un element source ou cible"""
    # TODO gerer langue source et cible avec des conditions
    un_element = random.choice(listVoc)
    langue_source = (un_element[0])
    langue_cible = (un_element[1])
    return langue_source


resultat = choix_question()
print(resultat)


def check_reponse(rep):
    question = resultat
    if rep == question:
        statut = 1
    else:
        statut = 0
    return statut

finale = check_reponse("pomme")
print(finale)



