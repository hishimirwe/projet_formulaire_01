# import des tkinter comme tk
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from os import path


# creation de la classe d'application tk
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.init_file_csv()
        self.fn_creer_widgets()
         #self.load_bdd()

    def msg(self, erreur):
        messagebox.showerror("erreur", erreur)

    def msg_saved(self):
        messagebox.showinfo("Information", "données correctement encodées")

    def init_file_csv(self):
        self.init_formulaire_csv = "Ishimirwe Hozana 6TTB tkinter formulaire d'encodage.csv"
        if not path.exists(self.init_formulaire_csv):
            try:
                self.formulaire_csv = open("Ishimirwe Hozana 6 TTB tkinter formulaire d'encodage.csv", "w", encoding="utf-8")
            except FileNotFoundError:
                self.msg("fichier introuvable")
            except IOError:
                self.msg(" Erreur d'ouverture ")
            header = "Nom, Prénom ,Date de naissance "
            self.formulaire_csv.write(header)
            self.formulaire_csv.write("\n")
            self.formulaire_csv.close()

    def file_csv(self, liste_value):
        print(liste_value)
        line = ""
        sep = ","
        for x in liste_value:
            line = line + x + sep
        line = line[:-1]
        print(line)
        try:
            self.formulaire_csv = open("Ishimirwe Hozana 6 TTB tkinter formulaire d'encodage.csv", "w", encoding="utf-8")
        except FileNotFoundError:
            self.msg_error("fichier introuvable")
        except IOError:
            self.msg_error(" Erreur d'ouverture ")
        self.formulaire_csv.write(line)
        self.formulaire_csv.write("\n")
        self.formulaire_csv.close()

    def fn_read_file_csv(self):
        try:
            self.formulaire_csv = open("Ishimirwe Hozana 6 TTB tkinter formulaire d'encodage.csv", "w", encoding="utf-8")
        except FileNotFoundError:
            self.msg_error("fichier introuvable")
        except IOError:
            self.msg_error(" Erreur d'ouverture ")
        self.record_formulaire1 = self.formulaire_csv.readlines()
        self.formulaire_csv.close()
        # initialisation des variables
        self.nom_record = []
        self.prenom_record = []
        self.date_de_naissance_record = []

        for line in self.record_formulaire1:
            self.line_formulaire1 = line.split(",")
            self.nom_record.append(self.line_formulaire1(0))
            self.prenom_record.append(self.line_formulaire1(1))
            self.date_de_naissance_record.append(self.line_formulaire1(2))

            


    def fn_creer_widgets(self):
        # variables
        self.nom_var = tk.StringVar()
        self.prenom_var = tk.StringVar()
        self.date_de_naissance_var = tk.StringVar()

        # definition de mes labels
        self.nom_label = tk.Label(self, text="Entrez votre nom")
        self.prenom_label = tk.Label(self, text="Entrez votre prénom")
        self.date_de_naissance_label = tk.Label(self, text="Entrez votre date de naissance")

        # definition des entry
        self.nom_entry = tk.Entry(self, textvariable=self.nom_var)
        self.prenom_entry = tk.Entry(self, textvariable=self.prenom_var)
        self.date_de_naissance_entry = tk.Entry(self, textvariable=self.date_de_naissance_var)

        # definition des boutons
        self.enregistrer_b = tk.Button(self, text="Enregistrer", command=self.fn_enregistrer)
        self.line_b = tk.Button(self, text="Charge la base de données", command=self.fn_read_file_csv)
        self.quitter_b = tk.Button(self, text="Quitter", command=self.quit)

        # implementation des widgets
        self.nom_label.grid(column=0, row=0, pady=5)
        self.nom_entry.grid(column=1, row=0, pady=5)
        self.prenom_label.grid(column=0, row=1, pady=5)
        self.prenom_entry.grid(column=1, row=1, pady=5)
        self.date_de_naissance_label.grid(column=0, row=2, pady=5)
        self.date_de_naissance_entry.grid(column=1, row=2, pady=5)
        self.enregistrer_b.grid(columnspan=1, pady=10)
        self.quitter_b.grid(columnspan=1)

    def fn_enregistrer(self):
        self.nom = self.nom_var.get()
        self.prenom = self.prenom_var.get()
        self.date_de_naissance = self.date_de_naissance_var.get()
        self.erreur_nom = False
        self.erreur_prenom = False
        self.erreur_date_de_naissance = False
        self.erreur_nom_txt = ""
        self.erreur_prenom_txt = ""
        self.erreur_date_de_naissance_txt = ""
        self.liste_value = []

        # verification du nom
        if not self.nom.isalpha():
            self.erreur_nom = True
            self.erreur_nom_txt = "caractere invalides dans le nom \n"

        # verification du prenom
        if not self.prenom.isalpha():
            self.erreur_prenom = True
            self.erreur_prenom_txt = "caractere invalides dans le prenom \n"

        # verification du datetime
        try:
            datetime.strptime(self.date_de_naissance, "%d-%m-%Y")
        except ValueError:
            self.erreur_date_de_naissance = True
            self.erreur_date_de_naissance_txt = "format de date incorrecte\n"

        if self.erreur_nom or self.erreur_prenom or self.erreur_date_de_naissance:
            self.erreur_global = self.erreur_nom_txt + self.erreur_prenom_txt + self.erreur_date_de_naissance_txt
            self.msg(self.erreur_global)
        if not (self.erreur_nom or self.erreur_prenom or self.erreur_date_de_naissance):
            self.liste_value.append(self.nom)
            self.liste_value.append(self.prenom)
            self.liste_value.append(self.date_de_naissance)
            self.file_csv(self.liste_value)
            self.msg_saved()
            self.nom_var.set("")
            self.prenom_var.set("")
            self.date_de_naissance_var.set("")


if __name__ == "__main__":
    app = Application()
    app.title("Formulaire 01")
    app.geometry("250x200")
    app.configure(bg='grey')
    app.mainloop()
