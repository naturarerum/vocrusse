# -------------------------------------------------------------------------------
# Name:         VocRusse 1.2.0
# Purpose:     - refactoring into OOP - first stage (classes)
#              - ui improvements
#
#
# Author:      Olivier
#
# Created:     28--06-2018
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


class appGui(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.title('titre')
        self.iconbitmap(r'C:\Users\GrandMage\PycharmProjects\vocrusse\ressources\Cactus.ico')
        self.geometry('270x146')
        self.menuBar = Menu(master=self)
        self.filemenu = Menu(self.menuBar, tearoff=0)
        self.statmenu = Menu(self.menuBar, tearoff=0)
        self.config(menu=self.menuBar)
        self.createWidgets()

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
        self.list_v = []

        # Création du label liste déroulante choix de langue source
        lbl_choix_langue = tk.Label(main_frame, text="Matière            : ").grid(row=0)


        # Adding items to the Menu
        self.menuBar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Open", command=self.read_file)
        self.filemenu.add_command(label="Quit", command=self.quit)
        self.menuBar.add_cascade(label="Stats", menu=self.statmenu)

        # Status bar
        # status = tk.Label(main_frame, text="Réponse : ").grid(column=0, row=4, sticky=W+E)

        # Creates a Button for the random selection of a word
        # btn_selection = tk.Button(main_frame, text="Selection", command=self.choix_question).grid(row = 1)

        # Creates a Button for the random selection of a word
        btn_selection = tk.Button(main_frame, text="Selection", command=self.choix_question).grid(column=2, row=0)

        # Création d'un bouton pour le choix du fichier
        #btn_fichier = tk.Button(main_frame, text="Fichier", command=self.read_file).grid(column=2, row=4)

        # Création d'un  bouton pour soumettre la réponse
        btn_reponse = tk.Button(main_frame, text="Vérifier", width=7, command=self.check_reponse).grid(column=2, row=3)

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
        self.choix_langue = ttk.Combobox(main_frame, width=12, textvariable=self.langue_choisie)
        self.choix_langue['values'] = ('Français', 'Russe')
        self.choix_langue.grid(column=1, row=0)
        self.choix_langue.current(0)
        self.choix_langue.focus()
        self.choix_langue.bind("<<ComboboxSelected>>", self.selection_langue)

        # Création du widget saisie de la réponse
        self.saisie_reponse = tk.Entry(main_frame, width=15, textvariable=self.reponse)
        self.saisie_reponse.grid(column=1, row=3)

        # Création du label qui indique si la reponse est bonne
        lbl_result = tk.Label(main_frame, textvariable=self.affichrep).grid(column=0, row=4)

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
        self.langue_source = []
        self.langue_cible = []
        try:
            un_element = random.choice(self.list_v)
        except IndexError:
            messagebox.showerror("Error", "Sélectionnez un fichier")
        if self.langue_choisie == 'Russe':
            print('----si russe -----', self.value)
            self.langue_source = (un_element[0])
            self.langue_cible = (un_element[1])
            myvar = self.langue_source
            myvarcible = self.langue_cible
        else:
            print('----si auitre -----', self.value)
            self.langue_source = (un_element[1])
            self.langue_cible = (un_element[0])
            myvar = self.langue_source
            myvarcible = self.langue_cible
        # self.mot_demande.set(myvar)
        # self.mot_compare.set(myvarcible)
        self.mot_demande.set(self.langue_source)
        self.mot_compare.set(self.langue_cible)
        print(self.langue_source)
        print(un_element)
        return self.langue_source, self.langue_cible


class StatusBar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.variable = tk.StringVar()
        self.label = tk.Label(self, relief=tk.SUNKEN, anchor=tk.W,
                              textvariable=self.variable,
                              font=('arial', 16, 'normal'))
        self.variable.set('Status Bar')
        self.label.grid(column=0, row=4, columnspan=2, sticky=W + E)
        self.grid()

    def clear_status(self):
        pass

if __name__ == "__main__":
    app = appGui(None)
    d = StatusBar(app)
    app.mainloop()