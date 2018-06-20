# -------------------------------------------------------------------------------
# Name:        VocRusse 2
# Purpose:     refactoring into OOP
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
import sys
from tkinter import filedialog
from tkinter import messagebox
import logging



# TODO : Mettre les methodes en premier
# TODO : listVoc comme parametre 
# TODO : appeler les methodes
# TODO : redesign interface
# TODO : implementer logs

class AppGui(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("Vocabulaire")
        self.master.iconbitmap(r'C:\Users\GrandMage\PycharmProjects\vocrusse\ressources\Cactus.ico')
        self.master.geometry('270x120')
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(sticky="NSEW")
        self.create_widgets()


    def create_widgets(self):
        # Class variables
        self.langue_choisie = tk.StringVar()
        self.reponse = tk.StringVar()
        self.mot_demande = tk.StringVar()
        self.mot_compare = tk.StringVar()
        self.value = tk.StringVar()
        self.resultat = tk.StringVar()
        self.affichrep = tk.StringVar()
        self.list_v = []


        mainFrame = ttk.Frame(self, borderwidth=2, relief="groove")
        mainFrame.grid(column=0, row=0, sticky="NSEW")
        # Creates a Button for the random selection of a word

        btn_selection = ttk.Button(mainFrame, text="Selection", command=self.choix_question).grid(column=2, row=0)

        # Création d'un bouton pour le choix du fichier
        btn_fichier = ttk.Button(mainFrame, text="Fichier", command=self.read_file).grid(column=2, row=4)

        # Création d'un  bouton pour soumettre la réponse
        btn_reponse = ttk.Button(mainFrame, text="Réponse", command=self.check_reponse).grid(column=2, row=3)

        # Création du label liste déroulante choix de langue source
        lbl_choix_langue = ttk.Label(mainFrame, text="Langue            : ").grid(column=0, row=0)

        # Création du label mot a trouver
        lbl_mot_demande = ttk.Label(mainFrame, text="Mot a trouver  : ").grid(column=0, row=2)

        # Création du label qui affiche le  mot a trouver
        lbl_mot_demande_affiche = ttk.Label(mainFrame, textvariable=self.mot_demande).grid(column=1, row=2)

        # Création du label reponse
        lbl_reponse = ttk.Label(mainFrame, text="Réponse           : ").grid(column=0, row=3)

        # Création du widget liste déroulante choix de langue source
        self.choix_langue = ttk.Combobox(mainFrame, width=12, textvariable=self.langue_choisie)
        self.choix_langue['values'] = ('Français', 'Russe')
        self.choix_langue.grid(column=1, row=0)
        self.choix_langue.current(0)
        self.choix_langue.focus()
        self.choix_langue.bind("<<ComboboxSelected>>", self.selection_langue)

        # Création du widget saisie de la réponse
        self.saisie_reponse = ttk.Entry(mainFrame, width=15, textvariable=self.reponse)
        self.saisie_reponse.grid(column=1, row=3)

        # Création du label qui indique si la reponse est bonne
        lbl_result = ttk.Label(mainFrame, textvariable=self.affichrep).grid(column=0, row=4)

    def read_file(self):
        print('----read file  Début-----')
        filename = filedialog.askopenfilename()
        count = 0
        try:
            f = codecs.open(filename, encoding='utf-8')
        except IOError as e:
            messagebox.showerror("Erreur", "I/O error({0}): {1}".format(e.errno, e.strerror))
        except:  # handle other exceptions such as attribute errors
            messagebox.showerror("Unexpected error:", sys.exc_info()[0])
        listVoc = []
        for line in f:
            splitted = line.rstrip().split(",")
            listVoc.append(splitted)
            count += 1
            print(count)
        print(listVoc)
        self.list_v = listVoc
        return listVoc

        # Selection de la langue dans la liste déroulante
    def selection_langue(self, event):
        print('----Langue choisie Début-----')
        self.langue_choisie = self.choix_langue.get()
        print('Langue choisie : ', self.langue_choisie)
        return self.langue_choisie


    def check_reponse(self):
        self.resultat = self.reponse.get()
        mymot2 = self.mot_compare.get()
        print("res : ", self.resultat)
        print(mymot2)
        if self.resultat == mymot2:
            statut = 1
            res = "OK"
        else:
            statut = 0
            res = "NOK"
        print(statut)
        self.affichrep.set(res)
        return statut

    #     """choix aleatoire d un element source ou cible"""
    def choix_question(self):
        print('----Choix question debut-----')
        self.value = self.langue_choisie
        un_element = random.choice(self.list_v)
        if self.value == 'Russe':
            self.langue_source = (un_element[0])
            self.langue_cible = (un_element[1])
            myvar = self.langue_source
            myvarcible = self.langue_cible
        else:
            self.langue_source = (un_element[1])
            self.langue_cible = (un_element[0])
            myvar = self.langue_source
            myvarcible = self.langue_cible
        self.mot_demande.set(myvar)
        self.mot_compare.set(myvarcible)
        print(self.langue_source)
        print(un_element)
        return self.langue_source, self.langue_cible

# =================================================================================#
#                                 START GUI                                        #
#==================================================================================#


def main():
    app = AppGui()
    logging.basicConfig(filename='vocrusse_log.log', level=logging.DEBUG)
    logging.debug('Loggin Started')
    app.create_widgets()
    logging.debug('Loggin Finished')
    app.mainloop()


if __name__ == '__main__':
    main()
