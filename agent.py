from tkinter import *
import tkinter as tk
import customtkinter as customtkinter
import tkinter
from tkinter import ttk
from tkinter import Entry
from tkinter.messagebox import showinfo
from subprocess import call
import pymysql as pymysql
from tkinter import messagebox
import tkcalendar
# import mysql.connector as Mysql

root_1 = Tk()
root_1.geometry("800x550+200+100")
root_1.iconbitmap("22926756.ico")
# root_1.config(background="#FFFFFF")
# root_1.resizable(False,False)
customtkinter.set_appearance_mode("System")
root_1.title("Agent")
# define columns

tree = ttk.Treeview(root_1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show='headings')


def Retour():
    root_1.destroy()
    call(["python", "acc.py"])



def afficher():
    con = pymysql.connect(host="localhost", user="root", password="sidi", database="gardiennage")
    cursor = con.cursor()
    cursor.execute("select * from agent ")
    tree.delete(*tree.get_children())
    records = cursor.fetchall()
    print(records)

    for i, (nom, prenom, mode_agent, date, numero, age, adresse, sexe) in enumerate(records, start=1):
        tree.insert("", "end", values=(nom, prenom, mode_agent, date, numero, age, adresse, sexe))

    con.close()


afficher()


def rechercher():
    if (e5.get() == ""):
        messagebox.showinfo("Recherche ", "Veuillez entrer le numéro de l'agent à rechercher !!!")
    else:
        con = pymysql.connect(host="localhost", user="root", password="sidi", database="gardiennage")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM agent WHERE numero ='" + e5.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            e1.insert(0, row[0])
            e2.insert(0, row[1])
            e3.insert(0, row[2])
            e4.delete(0, "end")
            e4.insert(0, row[3])
            e6.insert(0, row[5])
            e7.insert(0, row[6])
            e8.insert(0, row[7])
        con.close();


def ajouter():
    nom = e1.get()
    prenom = e2.get()
    mode_agent = e3.get()
    date = e4.get()
    numero = e5.get()
    age = e6.get()
    adresse = e7.get()
    sexe = e8.get()

    if (
            nom == "" or prenom == "" or mode_agent == "" or date == "" or numero == "" or age == "" or adresse == "" or sexe == ""):
        messagebox.showinfo("Message d'erreur", "Tout les champs sont réquis !!!")
    else:

        con = pymysql.connect(host="localhost", user="root", password="sidi", database="gardiennage")
        cursor = con.cursor();
        cursor.execute(
            "insert into agent values('" + nom + "','" + prenom + "','" + mode_agent + "','" + date + "','" + numero + "','" + age + "','" + adresse + "','" + sexe + "') ")
        cursor.execute("commit");

        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        e4.delete(0, "end")
        e5.delete(0, "end")
        e6.delete(0, "end")
        e7.delete(0, "end")
        e8.delete(0, "end")
        messagebox.showinfo("Ajouter ", "L'ajout effectuer avec succès")
    afficher()

    con.close()


def modifier():
    nom = e1.get()
    prenom = e2.get()
    mode_agent = e3.get()
    date = e4.get()
    numero = e5.get()
    age = e6.get()
    adresse = e7.get()
    sexe = e8.get()

    if (nom == "" or prenom == "" or mode_agent == "" or date == "" or numero == "" or age == "" or adresse == "" or sexe == ""):
        messagebox.showinfo("Message d'erreur", "Aucun champ ne doit être vide !!!")
    else:
        con = pymysql.connect(host="localhost", user="root", password="sidi", database="gardiennage")
        cursor = con.cursor();
        cursor.execute("update agent set nom='" + nom + "',prenom='" + prenom + "',mode_agent='" + mode_agent + "',date='" + date + "',numero='" + numero + "',age='" + age + "',adresse='" + adresse + "',sexe='" + sexe + "' where nom='" + nom + "'")
        cursor.execute("commit");

        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        e4.delete(0, "end")
        e5.delete(0, "end")
        e6.delete(0, "end")
        e7.delete(0, "end")
        e8.delete(0, "end")
        messagebox.showinfo("Modification ", "Modification effectuer avec succès")

        afficher()

        con.close()


# frame
frame = customtkinter.CTkFrame(master=root_1, fg_color="#46887C", width=2800, height=70, corner_radius=10)
frame.place(relx=0, rely=0, anchor=tkinter.CENTER)
label = tk.Label(master=root_1, text="Agent", bg="#46887C", fg='#ffffff', font=("regular", 18))
# label.place(x=400, y=17, anchor=tkinter.CENTER)
label.pack(padx=100, pady=0)
button = Button(master=root_1, text="Retour", fg='#ffffff', bg='#000000', font=("regular", 12), command=Retour)
button.place(x=0, y=0)
# les labels

nom = customtkinter.CTkLabel(master=root_1, text="Nom", text_font=('regular', 15,), corner_radius=8)
nom.place(x=42, y=100, anchor=tkinter.CENTER)
prenom = customtkinter.CTkLabel(master=root_1, text="Prénom", text_font=('regular', 15,), corner_radius=8)
prenom.place(x=50, y=150, anchor=tkinter.CENTER)
mode_agent = customtkinter.CTkLabel(master=root_1, text="Mode agent", text_font=('regular', 15,), corner_radius=8)
mode_agent.place(x=70, y=200, anchor=tkinter.CENTER)
date = customtkinter.CTkLabel(master=root_1, text="Date", text_font=('regular', 15,), corner_radius=8)
date.place(x=40, y=250, anchor=tkinter.CENTER)
numero = customtkinter.CTkLabel(master=root_1, text="Numéro", text_font=('regular', 15,), corner_radius=8)
numero.place(x=450, y=100, anchor=tkinter.CENTER)
age = customtkinter.CTkLabel(master=root_1, text="Âge", text_font=('regular', 15,), corner_radius=8)
age.place(x=435, y=150, anchor=tkinter.CENTER)
adresse = customtkinter.CTkLabel(master=root_1, text="Adresse", text_font=('regular', 15,), corner_radius=8)
adresse.place(x=450, y=200, anchor=tkinter.CENTER)
sexe = customtkinter.CTkLabel(master=root_1, text="Sexe", text_font=('regular', 15,), corner_radius=8)
sexe.place(x=435, y=250, anchor=tkinter.CENTER)
# les champs

e1 = customtkinter.CTkEntry(master=root_1, width=200, height=30, fg_color="#ffffff", corner_radius=8)
e1.place(x=250, y=100, anchor=tkinter.CENTER)
e2 = customtkinter.CTkEntry(master=root_1, width=200, height=30, fg_color="#ffffff", corner_radius=8)
e2.place(x=250, y=150, anchor=tkinter.CENTER)
e3 = ttk.Combobox(root_1, values=['7H-18H', '18H-7H', '24H/24H'], width=20, height=100, font=(30))
e3.place(x=150, y=190)
e3.current()
# e4 = customtkinter.CTkEntry(master=root_1, width=200, height=30, fg_color="#ffffff", corner_radius=8)
# e4.place(x=250, y=250, anchor=tkinter.CENTER)
e4 = tkcalendar.DateEntry(root_1,bd=2,font=("Times New Roman",12),date_pattern = "YYYY-MM-DD")
e4.place(x=150,y=240,width=200)
e5 = customtkinter.CTkEntry(master=root_1, width=200, height=30, fg_color="#ffffff", corner_radius=8)
e5.place(x=650, y=100, anchor=tkinter.CENTER)
e6 = customtkinter.CTkEntry(master=root_1, width=200, height=30, fg_color="#ffffff", corner_radius=8)
e6.place(x=650, y=150, anchor=tkinter.CENTER)
e7 = customtkinter.CTkEntry(master=root_1, width=200, height=30, fg_color="#ffffff", corner_radius=8)
e7.place(x=650, y=200, anchor=tkinter.CENTER)
e8 = ttk.Combobox(root_1, values=['Homme', 'Femme'], width=20, height=100, font=(30))
e8.place(x=550, y=240)
e8.current()

style = ttk.Style(root_1)
style.theme_use("clam")
style.configure("Treeview", background="gray90", fieldbackground="white", highlightthickness=0, bd=0,
                foreground="black")
style.configure("mystyle.Treeview.Heading", font=('Calibri', 8, 'bold'))

# define headings
tree.heading(1, text='Nom')
tree.heading(2, text='Prénom')
tree.heading(3, text='Mode agent')
tree.heading(4, text='Date')
tree.heading(5, text='Numéro')
tree.heading(6, text='Âge')
tree.heading(7, text='Adresse')
tree.heading(8, text='Sexe')
tree.column(1, width=15)
tree.column(2, width=15)
tree.column(3, width=15)
tree.column(4, width=15)
tree.column(5, width=15)
tree.column(6, width=15)
tree.column(7, width=15)
tree.column(8, width=15)


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)
tree.place(x=0, y=320, width=780, height=220)
# tree.place(x=0,y=280, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root_1, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x=780, y=320, height=220)

button = customtkinter.CTkButton(master=root_1, text="Ajouter", fg_color=("#4F805D", "#4F805D"), text_color='#ffffff',
                                 text_font=("regular", 15), command=ajouter)
button.place(x=80, y=280)
button = customtkinter.CTkButton(master=root_1, text="Modifier", fg_color=("#58A8A3", "#58A8A3"), text_color='#ffffff',
                                 text_font=("regular", 15), command=modifier)
button.place(x=270, y=280)
button = customtkinter.CTkButton(master=root_1, text="Rechercher", fg_color=("#455785", "#455785"), text_color='#ffffff',
                                 text_font=("regular", 15), command=rechercher)
button.place(x=450, y=280)

root_1.mainloop()
