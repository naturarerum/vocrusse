# -------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Olivier
#
# Created:     23-07-2016
#
# -------------------------------------------------------------------------------

import tkinter as tk
from tkinter import ttk
import random
import codecs

from tkinter import Menu
from tkinter import messagebox as msBox

import vocrusse

# Main window
win = tk.Tk()
win.title("Vocrusse")
win.iconbitmap(r'C:\Python34\DLLs\pyc.ico')

# Variables Globales
ficIn = 'D:\\Temp\\russe_vocabulearn.txt'
count = 0

f = codecs.open(ficIn, encoding='utf-8')
listVoc = []
for line in f:
    splitted = line.rstrip().split(",")
    listVoc.append(splitted)
    count += 1
    print(count)

# Variables Globales
langue_choisie = tk.StringVar()
langue_cible = tk.StringVar()
reponse = tk.StringVar()
mot_demande = tk.StringVar()
mot_compare = tk.StringVar()
value = tk.StringVar()
resultat = tk.StringVar()
affichrep = tk.StringVar()

# Création du label liste déroulante choix de langue source
lbl_choix_langue = ttk.Label(win, text="Langue            : ").grid(column=0, row=0)

# Création du label mot a trouver
lbl_mot_demande = ttk.Label(win, text="Mot a trouver  : ").grid(column=0, row=1)

# Création du label qui affiche le  mot a trouver
lbl_mot_demande_affiche = ttk.Label(win, textvariable=mot_demande).grid(column=1, row=1)

# Création du label reponse
lbl_reponse = ttk.Label(win, text="Réponse           : ").grid(column=0, row=2)

# Création du label qui indique si la reponse est bonne
lbl_result = ttk.Label(win, textvariable=affichrep).grid(column=1, row=3)

def choix_question(langue):

    """choix aleatoire d un element source ou cible"""
    value = langue
    un_element = random.choice(listVoc)
    if value == 'Russe':
        langue_source = (un_element[0])
        langue_cible = (un_element[1])
        myvar = langue_source
        myvarcible = langue_cible
    else:
        langue_source = (un_element[1])
        langue_cible = (un_element[0])
        myvar = langue_source
        myvarcible = langue_cible
    mot_demande.set(myvar)
    mot_compare.set(myvarcible)
    print(langue_source)
    print(un_element)
    return langue_source, langue_cible



# Selection de la langue dans la liste déroulante
def selection_langue(event):
    langue_choisie = choix_langue.get()
    return langue_choisie

# Selection du mot a demander
def selection_mot():
    valeur = langue_choisie.get()
    choix_question(valeur)


def check_reponse():
    resultat = reponse.get()
    mymot2 = mot_compare.get()
    print("res : ", resultat)
    print(mymot2)
    if resultat == mymot2:
        statut = 1
        res="OK"
    else:
        statut = 0
        res = "NOK"
    print(statut)
    affichrep.set(res)
    return statut


# Création du widget liste déroulante choix de langue source
choix_langue = ttk.Combobox(win, width=12, textvariable=langue_choisie)
choix_langue['values'] = ('Français','Russe' )
choix_langue.grid(column=1, row=0)
choix_langue.current(0)
choix_langue.focus()
choix_langue.bind("<<ComboboxSelected>>", selection_langue)

# Création du widget saisie de la réponse
saisie_reponse = ttk.Entry(win, width=15, textvariable=reponse)
saisie_reponse.grid(column=1, row=2)


# Création d'un widget bouton pour la selection aleatoire du mot
btn_selection = ttk.Button(win, text="Selection", command=selection_mot).grid(column=0, row=3)

# Création d'un widget bouton pour la verification de la reponse
btn_reponse = ttk.Button(win, text="Réponse", command=check_reponse).grid(column=2, row=3)

# =================================================================================#                                                                             #
#                                 START GUI                                        #
#==================================================================================#

win.mainloop()
