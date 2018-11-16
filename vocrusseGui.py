# -------------------------------------------------------------------------------
# Name:         VocRusse 1.1.0
# Purpose:     - refactoring into OOP - first stage (classes)
#              - ui improvements
#
#
# Author:      Olivier
#
# Created:     28-06-2018
#
# -------------------------------------------------------------------------------

from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
import codecs
import sys
from tkinter import filedialog
from tkinter import messagebox
import Stats


class AppGui(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.title('VocTrainer')
        self.iconbitmap(r'C:\Users\GrandMage\PycharmProjects\vocrusse\ressources\Cactus.ico')
        self.geometry('248x123')
        self.menuBar = Menu(master=self)
        self.filemenu = Menu(self.menuBar, tearoff=0)
        self.aboutmenu = Menu(self.menuBar, tearoff=0)
        self.config(menu=self.menuBar)
        self.createWidgets()
        self.version = '1.1.0'

    def createWidgets(self):
        # Class variables
        main_frame = tk.Frame(self, bg='lightgrey').grid(row=0, sticky=W)
        self.langue_choisie = tk.StringVar()
        self.reponse = tk.StringVar()
        self.mot_demande = tk.StringVar()
        self.mot_compare = tk.StringVar()
        self.value = tk.StringVar()
        self.resultat = tk.StringVar()
        self.affichrep = tk.StringVar()
        self.cpte_reponses_totales = tk.IntVar()
        self.cpte_reponses_ok = tk.IntVar()
        self.cpte_reponses_nok = tk.IntVar()
        self.affiche_score = tk.IntVar()
        self.list_v = []

        # Création du label liste déroulante choix de langue source
        lbl_choix_langue = tk.Label(main_frame, text="Matière            : ").grid(row=0)

        # Adding items to the Menu
        self.menuBar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Open", command=self.read_file)
        self.filemenu.add_command(label="Quit", command=self.quit)
        self.menuBar.add_cascade(label="About", menu=self.aboutmenu)
        self.aboutmenu.add_command(label="Version", command=self.affiche_version)

        # Creates a Button for the random selection of a word
        btn_selection = tk.Button(main_frame, text="Selection", command=self.choix_question).grid(column=2, row=0)

        # Création d'un  bouton pour soumettre la réponse
        btn_reponse = tk.Button(main_frame, text="Vérifier", width=7, command=self.check_reponse).grid(column=2, row=2)

        # Création d'un  bouton pour soumettre les champs a zero
        btn_reset = tk.Button(main_frame, text="Reset", width=7, command=self.check_reponse).grid(column=2, row=3)

        # Création du label liste déroulante choix de langue source
        lbl_choix_langue = tk.Label(main_frame, text="Matière            : ").grid(column=0, row=0)

        # Création du label mot a trouver
        lbl_mot_demande = tk.Label(main_frame, text="Question         : ").grid(column=0, row=2)

        # Création du label qui affiche le  mot a trouver
        lbl_mot_demande_affiche = tk.Label(main_frame, background="light blue", foreground="black", width=13,
                                           textvariable=self.mot_demande).grid(column=1, row=2)

        # Création du label reponse
        lbl_reponse = tk.Label(main_frame, text="Réponse           : ").grid(column=0, row=3)

        # Création du widget liste déroulante choix de langue source
        self.choix_langue = tk.StringVar()
        self.choix_langue = ttk.Combobox(main_frame, width=12, textvariable=self.langue_choisie)
        self.choix_langue['values'] = ('Français', 'Russe', 'Addition', 'Multiplication')
        self.choix_langue.grid(column=1, row=0)
        self.choix_langue.state(['readonly'])
        self.choix_langue.current(0)
        self.choix_langue.focus()
        self.choix_langue.bind("<<ComboboxSelected>>", self.selection_langue)

        # Création du widget saisie de la réponse
        self.saisie_reponse = tk.Entry(main_frame, width=15, textvariable=self.reponse)
        self.saisie_reponse.grid(column=1, row=3)

        # Création de la barre de statut
        lbl_result = tk.Label(main_frame, relief=tk.SUNKEN, anchor=tk.W, font=('arial', 16, 'normal'), fg='blue',
                              width=8,
                              textvariable=self.affichrep).grid(column=0, row=5, columnspan=2, sticky=W)
        lbl_score = tk.Label(main_frame, relief=tk.SUNKEN, anchor=tk.W, font=('arial', 16, 'normal'), fg='blue',
                             width=13,
                             textvariable=self.affiche_score).grid(column=1, row=5, columnspan=2, sticky=E)

    def read_file(self):
        print('----read file  Début-----')
        filename = filedialog.askopenfilename()
        count = 0
        try:
            f = codecs.open(filename, encoding='utf-8')
        except IOError as e:
            messagebox.showerror("Error", "I/O error({0}): {1}".format(e.errno, e.strerror))
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
        self.cpte_reponses_totales = 0
        self.cpte_reponses_ok = 0
        self.cpte_reponses_nok = 0
        return self.langue_choisie

    def check_reponse(self):
        self.resultat = self.reponse.get()
        mymot2 = self.mot_compare.get()
        print("res : ", self.resultat)
        print(mymot2)
        if self.resultat == mymot2:
            statut = 1
            res = "OK"
            self.cpte_reponses_nok += 1
        else:
            statut = 0
            res = "NOK"
            self.cpte_reponses_nok += 1
        print(statut)
        self.affichrep.set(res)
        self.cpte_reponses_totales += 1
        return statut

    #     """choix aleatoire d un element source ou cible"""
    def choix_question(self):
        self.reponse.set('')
        self.affichrep.set('')
        self.langue_source = []
        self.langue_cible = []
        try:
            un_element = random.choice(self.list_v)
        except IndexError:
            messagebox.showerror("Erreur", "Sélectionnez un fichier")
        if self.langue_choisie == 'Russe' or 'Addition' or 'Multiplication':
            print('----si russe -----', self.value)
            self.langue_source = (un_element[0])
            self.langue_cible = (un_element[1])
            myvar = self.langue_source
            myvarcible = self.langue_cible
        else:
            print('----si autre -----', self.value)
            self.langue_source = (un_element[1])
            self.langue_cible = (un_element[0])
        self.mot_demande.set(self.langue_source)
        self.mot_compare.set(self.langue_cible)
        print(self.langue_source)
        print(un_element)
        return self.langue_source, self.langue_cible

    def affiche_version(self):
        messagebox.showinfo("Version : ", self.version)

    # def compte_score(self):

if __name__ == "__main__":
    app = AppGui(None)
    app.mainloop()
