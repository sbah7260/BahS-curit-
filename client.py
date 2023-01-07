from tkinter import *
import tkinter as tk
import customtkinter
import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
from subprocess import call
import pymysql as pymysql
from tkinter import messagebox
import tkcalendar
root=Tk()
root.geometry("800x550+200+100")
root.iconbitmap("22926756.ico")
# root.config(background="#FFFFFF")
# root.resizable(False,False)
customtkinter.set_appearance_mode("System")
root.title("Client")
def Retour():
    root.destroy()
    call(["python","acc.py"])

# define columns

tree = ttk.Treeview(root, columns=(1,2,3,4,5,6),show='headings')

#connection à la base de données

def afficher():
    con = pymysql.connect(host="localhost", user="root", password="sidi", database="gardiennage")
    cursor = con.cursor()
    cursor.execute("select * from client ")
    tree.delete(*tree.get_children())
    records = cursor.fetchall()
    print(records)

    for i, (nom, prenom, date, numero, adresse, mode_agent) in enumerate(records, start=1):
        tree.insert("", "end", values=(nom, prenom, date, numero, adresse, mode_agent))

    con.close()


afficher()


def rechercher():
    if (e4.get() == ""):
        messagebox.showinfo("Recherche ", "Veuillez entrer le numéro du client à rechercher !!!")
    else:
        con = pymysql.connect(host="localhost", user="root", password="sidi", database="gardiennage")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM client WHERE numero ='" + e4.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            e1.insert(0, row[0])
            e2.insert(0, row[1])
            e3.delete(0, "end")
            e3.insert(0, row[2])
            e5.insert(0, row[4])
            e6.insert(0, row[5])

        con.close();


def ajouter():
    nom = e1.get()
    prenom = e2.get()
    date = e3.get()
    numero = e4.get()
    adresse = e5.get()
    mode_agent = e6.get()


    if (
            nom == "" or prenom == "" or date == "" or numero == "" or adresse == "" or mode_agent == "" ):
        messagebox.showinfo("Message d'erreur", "Tout les champs sont réquis !!!")
    else:

        con = pymysql.connect(host="localhost", user="root", password="sidi", database="gardiennage")
        cursor = con.cursor();
        cursor.execute(
            "insert into client values('" + nom + "','" + prenom + "','" + date + "','" + numero + "','" + adresse + "','" + mode_agent + "') ")
        cursor.execute("commit");

        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        e4.delete(0, "end")
        e5.delete(0, "end")
        e6.delete(0, "end")

        messagebox.showinfo("Ajouter ", "L'ajout effectuer avec succès")
    afficher()

    con.close()


def modifier():
    nom = e1.get()
    prenom = e2.get()
    date = e3.get()
    numero = e4.get()
    adresse = e5.get()
    mode_agent = e6.get()


    if (nom == "" or prenom == "" or date == "" or numero == "" or adresse == "" or mode_agent == "" ):
        messagebox.showinfo("Message d'erreur", "Aucun champ ne doit être vide !!!")
    else:
        con = pymysql.connect(host="localhost", user="root", password="sidi", database="gardiennage")
        cursor = con.cursor();
        cursor.execute("update client set nom='" + nom + "',prenom='" + prenom + "',date='" + date + "',numero='" + numero + "',adresse='" + adresse + "',mode_agent='" + mode_agent +"' where nom='" + nom + "'")
        cursor.execute("commit");

        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        e4.delete(0, "end")
        e5.delete(0, "end")
        e6.delete(0, "end")

        messagebox.showinfo("Modification ", "Modification effectuer avec succès")

        afficher()

        con.close()



frame = customtkinter.CTkFrame(master=root,fg_color="#46887C",width=2800,height=70,corner_radius=10)
frame.place(relx=0, rely=0, anchor=tkinter.CENTER)
label = tk.Label(master=root, text="client", bg="#46887C", fg='#ffffff', font=("regular", 18))
# label.place(x=400, y=17, anchor=tkinter.CENTER)
label.pack(padx=100, pady=0)
button = Button(root, text="Retour", fg='#ffffff',bg='#000000',font=("regular",12),command=Retour)
button.place(x=0,y=0)

nom = customtkinter.CTkLabel(master=root,text="Nom",text_font=('regular',15,),corner_radius=8)
nom.place(x=60, y=100, anchor=tkinter.CENTER)
prenom = customtkinter.CTkLabel(master=root,text="Prénom",text_font=('regular',15,),corner_radius=8)
prenom.place(x=70, y=150, anchor=tkinter.CENTER)
date = customtkinter.CTkLabel(master=root,text="Date",text_font=('regular',15,),corner_radius=8)
date.place(x=57, y=200, anchor=tkinter.CENTER)
numero = customtkinter.CTkLabel(master=root,text="Numéro",text_font=('regular',15,),corner_radius=8)
numero.place(x=430, y=100, anchor=tkinter.CENTER)
adresse = customtkinter.CTkLabel(master=root,text="Adresse",text_font=('regular',15,), corner_radius=8)
adresse.place(x=430, y=150, anchor=tkinter.CENTER)
mode_agent = customtkinter.CTkLabel(master=root,text="Mode agent",text_font=('regular',15,),corner_radius=8)
mode_agent.place(x=450, y=200, anchor=tkinter.CENTER)

e1 = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
e1.place(x=250,y=100, anchor=tkinter.CENTER)
e2 = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
e2.place(x=250,y=150, anchor=tkinter.CENTER)
# e3 = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
# e3.place(x=250,y=200, anchor=tkinter.CENTER)
e3 = tkcalendar.DateEntry(root,bd=2,font=("Times New Roman",12),date_pattern = "YYYY-MM-DD")
e3.place(x=150,y=190,width=200)
e4 = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
e4.place(x=650,y=100, anchor=tkinter.CENTER)
e5 = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
e5.place(x=650,y=150, anchor=tkinter.CENTER)
# entry = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
# entry.place(x=650,y=200, anchor=tkinter.CENTER)

e6 = ttk.Combobox(root,values = ['7H-18H','18H-7H','24H/24H'],width=20,height=100,font=(30))
e6.place(x=550,y=190)
e6.current()

style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", background="gray90", fieldbackground="white",highlightthickness=0, bd=0, foreground="black")
style.configure("mystyle.Treeview.Heading", font=('Calibri', 8,'bold'))

# define headings
tree.heading(1, text='Nom')
tree.heading(2, text='Prénom')
tree.heading(3, text='Date')
tree.heading(4, text='Numéro')
tree.heading(5, text='Adresse')
tree.heading(6, text='Mode agent')
tree.column(1,width=15)
tree.column(2,width=15)
tree.column(3,width=15)
tree.column(4,width=15)
tree.column(5,width=15)
tree.column(6,width=15)

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)
tree.place(x=0,y=320,width=780,height=220)
# tree.place(x=0,y=280, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x=780,y=320,height=220)

button = customtkinter.CTkButton(master=root, text="Ajouter", fg_color=("#4F805D", "#4F805D"),text_color='#ffffff',text_font=("regular",15),command=ajouter)
button.place(x=80,y=250)
button = customtkinter.CTkButton(master=root, text="Modifier", fg_color=("#58A8A3", "#58A8A3"),text_color='#ffffff',text_font=("regular",15),command=modifier)
button.place(x=270,y=250)
button = customtkinter.CTkButton(master=root, text="Rechercher", fg_color=("#455785", "#455785"),text_color='#ffffff',text_font=("regular",15),command=rechercher)
button.place(x=450,y=250)


root.mainloop()


# button = Button(root, text="Ajouter", fg='#000000',bg='#4F805D',font=("regular",15))
# button.place(x=100,y=280)
# button = Button(root, text="Modifier", fg='#000000',bg='#58A8A3',font=("regular",15))
# button.place(x=300,y=280)
# button = Button(root, text="Rechercher", fg='#000000',bg='#455785',font=("regular",15))
# button.place(x=500,y=280)
# button = Button(root, text="Retour", fg='#ffffff',bg='#000000',font=("regular",12))
# button.place(x=0,y=5)
# Label(root,text="Nom",fg="#000000",bg='white',font=('regular',15,)).place(x=40,y=80)
# Label(root,text="Prenom",fg="#000000",bg='white',font=('regular',15,)).place(x=40,y=130)
# Label(root,text="Date d'arrivée",fg="#000000",bg='white',font=('regular',15,)).place(x=40,y=180)
# Label(root,text="Numéro",fg="#000000",bg='white',font=('regular',15,)).place(x=435,y=80)
# Label(root,text="Adresse",fg="#000000",bg='white',font=('regular',15,)).place(x=435,y=130)
# Label(root,text="Mode d'agent",fg="#000000",bg='white',font=('regular',15,)).place(x=435,y=180)
# e2 = Entry(root,width=25,font=(30),border=3)
# e2.place(x=185,y=85)
# e3 = Entry(root,width=25,font=(30),border=3)
# e3.place(x=185,y=140)
# e5 = Entry(root,width=25,font=(30),border=3)
# e5.place(x=185,y=210)
# e6 = Entry(root,width=25,font=(30),border=3)
# e6.place(x=560,y=85)
# e7 = Entry(root,width=25,font=(30),border=3)
# e7.place(x=560,y=140)
# # e8 = Entry(root,width=25,font=(30),border=3)
# # e8.place(x=560,y=190)
# comboExample = ttk.Combobox(root,values = ['7H-18H','18H-7H','24H/24H'],width=23,font=(30))
# # pprint(dict(comboExample))
# comboExample.place(x=560,y=210)
# comboExample.current(0)