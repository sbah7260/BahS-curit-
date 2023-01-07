from tkinter import *
from tkinter import ttk
import customtkinter
import tkinter
from tkinter.messagebox import showinfo
import tkinter as tk
from subprocess import call
import pymysql as pymysql
from tkinter import messagebox
import tkcalendar
root=tkinter.Tk()
root.geometry("800x550+200+100")
root.iconbitmap("22926756.ico")
# root.config(background="#FFFFFF")
# root.resizable(False,False)
root.title("Equipement")
customtkinter.set_appearance_mode("System")

def Retour():
    root.destroy()
    call(["python","acc.py"])

# define columns

tree = ttk.Treeview(root, columns=(1,2,3,4),show='headings')

#connection à la base de données

def afficher():
    con = pymysql.connect(host="localhost", user="root", password="sidi", database="gardiennage")
    cursor = con.cursor()
    cursor.execute("select * from equipement ")
    tree.delete(*tree.get_children())
    records = cursor.fetchall()
    print(records)

    for i, (nom, nombre, prix, date) in enumerate(records, start=1):
        tree.insert("", "end", values=(nom, nombre, prix, date))

    con.close()


afficher()


def rechercher():
    if (e1.get() == ""):
        messagebox.showinfo("Recherche ", "Veuillez entrer le numéro de l'agent à rechercher !!!")
    else:
        con = pymysql.connect(host="localhost", user="root", password="sidi", database="gardiennage")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM equipement WHERE nom ='" + e1.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            e2.insert(0, row[1])
            e3.insert(0, row[2])
            e4.delete(0, "end")
            e4.insert(0, row[3])

        con.close();


def ajouter():
    nom = e1.get()
    nombre = e2.get()
    prix = e3.get()
    date = e4.get()


    if (
            nom == "" or nombre == "" or prix == "" or date == ""):
        messagebox.showinfo("Message d'erreur", "Tout les champs sont réquis !!!")
    else:

        con = pymysql.connect(host="localhost", user="root", password="sidi", database="gardiennage")
        cursor = con.cursor();
        cursor.execute("insert into equipement values('" + nom + "','" + nombre + "','" + prix + "','" + date + "') ")
        cursor.execute("commit");

        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        e4.delete(0, "end")

        messagebox.showinfo("Ajouter", "L'ajout effectuer avec succès")

        afficher()

        con.close()


def modifier():
    nom = e1.get()
    nombre = e2.get()
    prix = e3.get()
    date = e4.get()


    if (nom == "" or nombre == "" or prix == "" or date == ""):
        messagebox.showinfo("Message d'erreur", "Aucun champ ne doit être vide !!!")
    else:
        con = pymysql.connect(host="localhost", user="root", password="sidi", database="gardiennage")
        cursor = con.cursor();
        cursor.execute("update equipement set nom='" + nom + "',nombre='" + nombre + "',prix='" + prix + "',date='" + date + "' where nom='" + nom + "'")
        cursor.execute("commit");

        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        e4.delete(0, "end")

        messagebox.showinfo("Modification ", "Modification effectuer avec succès")

        afficher()

        con.close()



frame = customtkinter.CTkFrame(master=root,fg_color="#46887C",width=2800,height=70,corner_radius=10)
frame.place(relx=0, rely=0, anchor=tkinter.CENTER)
label = tk.Label(master=root, text="Equipement", bg="#46887C", fg='#ffffff', font=("regular", 18))
# label.place(x=400, y=17, anchor=tkinter.CENTER)
label.pack(padx=100, pady=0)
button = Button(root, text="Retour", fg='#ffffff',bg='#000000',font=("regular",12),command=Retour)
button.place(x=0,y=0)
#les textes
l1 = customtkinter.CTkLabel(master=root,text="Nom",text_font=('regular',15,),corner_radius=8)
l1.place(x=60, y=100, anchor=tkinter.CENTER)
l2 = customtkinter.CTkLabel(master=root,text="Nombre",text_font=('regular',15,),corner_radius=8)
l2.place(x=70, y=150, anchor=tkinter.CENTER)
l3 = customtkinter.CTkLabel(master=root,text="Prix",text_font=('regular',15,),corner_radius=8)
l3.place(x=477, y=100, anchor=tkinter.CENTER)
l4 = customtkinter.CTkLabel(master=root,text="Date",text_font=('regular',15,),corner_radius=8)
l4.place(x=477, y=150, anchor=tkinter.CENTER)

#les champs
# entry = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
# entry.place(x=250,y=100, anchor=tkinter.CENTER)
e2 = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
e2.place(x=250,y=150, anchor=tkinter.CENTER)
e3 = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
e3.place(x=650,y=100, anchor=tkinter.CENTER)
# e4 = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
# e4.place(x=650,y=150, anchor=tkinter.CENTER)
e4 = tkcalendar.DateEntry(root,bd=2,font=("Times New Roman",12),date_pattern = "YYYY-MM-DD")
e4.place(x=550,y=140,width=200)
e1 = ttk.Combobox(root,values = ['Arme','Tenue','Chaussure'],width=20,height=100,font=(30))
# pprint(dict(comboExample))
e1.place(x=150,y=90)
e1.current()

#Les boutons
button = customtkinter.CTkButton(master=root, text="Ajouter", fg_color=("#4F805D", "#4F805D"),text_color='#ffffff',text_font=("regular",15),command=ajouter)
button.place(x=80,y=250)
button = customtkinter.CTkButton(master=root, text="Modifier", fg_color=("#58A8A3", "#58A8A3"),text_color='#ffffff',text_font=("regular",15),command=modifier)
button.place(x=270,y=250)
button = customtkinter.CTkButton(master=root, text="Rechercher", fg_color=("#455785", "#455785"),text_color='#ffffff',text_font=("regular",15),command=rechercher)
button.place(x=450,y=250)
# button = customtkinter.CTkButton(master=root, text="Supprimer", fg_color=("red", "red"),text_color='#ffffff',text_font=("regular",15),command=quit)
# button.place(x=620,y=250)

style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", background="gray90", fieldbackground="white",highlightthickness=0, bd=0, foreground="black")
style.configure("mystyle.Treeview.Heading", font=('Calibri', 8,'bold'))


# define headings
tree.heading(1, text='Nom')
tree.heading(2, text='Nombre')
tree.heading(3, text='Prix')
tree.heading(4, text='Date')

tree.column(1,width=15)
tree.column(2,width=15)
tree.column(3,width=15)
tree.column(4,width=15)


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

root.mainloop()



# e2 = Entry(root,width=25,font=(30),border=3)
# e2.place(x=80,y=200)
# e3 = Entry(root,width=25,font=(30),border=3)
# e3.place(x=450,y=120)
# e4 = Entry(root,width=25,font=(30),border=3)
# e4.place(x=450,y=200)


#
# button = Button(root, text="Retour", fg='#ffffff',bg='#000000',font=("regular",12))
# button.place(x=0,y=5)
# button = Button(root, text="Ajouter", fg='#000000',bg='#4F805D',font=("regular",15))
# button.place(x=100,y=250)
# button = Button(root, text="Modifier", fg='#000000',bg='#58A8A3',font=("regular",15))
# button.place(x=300,y=250)
# button = Button(root, text="Rechercher", fg='#000000',bg='#455785',font=("regular",15))
# button.place(x=500,y=250)
# Label(root,text="Nom",fg="#000000",bg='white',font=('regular',15,)).place(x=80,y=80)
# Label(root,text="Nombre",fg="#000000",bg='white',font=('regular',15,)).place(x=80,y=160)
# Label(root,text="Prix",fg="#000000",bg='white',font=('regular',15,)).place(x=450,y=80)
# Label(root,text="Date",fg="#000000",bg='white',font=('regular',15,)).place(x=450,y=160)

# e1 = Entry(root,width=25,font=(30),border=3)
# e1.place(x=80,y=120)