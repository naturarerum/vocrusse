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
from tkinter import Menu
from tkinter import messagebox as msBox

import vocrusse

# Main window
win = tk.Tk()
win.title("Vocrusse")
win.iconbitmap(r'C:\Python34\DLLs\pyc.ico')

# Création d'un widget Label
#  question = StringVar()
# Label(fenetre, textvariable=question).pack(padx=30, pady=10)

"""def validation(un_element):
    if value.get() == un_element[1]:
       showinfo("Bon")
else:
    showinfo("Mauvaise reponse")
    value.set('')

# Création d'un widget Entry (champ de saisie)

value = StringVar()
value.set("Valeur")
entree = Entry(fenetre, textvariable=value, width=30)
entree.focus_set()
entree.pack()"""

# Création d'un widget bouton (champ Valider)
# bouton = Button(fenetre, text="Valider", command=validation).pack(side=LEFT, padx=5, pady=5)

win.mainloop()
