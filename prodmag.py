
#page produit magasinier

from subprocess import call
from tkinter import *
from tkinter import Entry
import customtkinter as customtkinter
from tkinter import ttk
import pymysql as pymysql
from tkinter import messagebox



def retour():
    fenetre8.destroy()
    call(["python","accmag.py"])





fenetre8=Tk()
fenetre8.title("Les produits Mag ")
fenetre8.geometry("1000x620")
# fenetre8.resizable(False, False)
fenetre8.configure(bg="white")
fenetre8.iconbitmap('C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\22926756.ico')
#affichage resultat
aff= ttk.Treeview(fenetre8, columns=(1,2,3,4,5,6),height=10,show="headings")
aff.place(x='',y='290',width=1000,height=280)

def afficher():

    con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor=con.cursor()
    cursor.execute("select * from produit ")
    aff.delete(*aff.get_children())
    records = cursor.fetchall()
    print(records)

    for i, (id,nom,quantite,date_arrive,fournisseur,telephone) in enumerate (records,start=1):
            aff.insert ("", "end", values=(id,nom,quantite,date_arrive,fournisseur,telephone))

    con.close()

afficher()


#les fonctions


def recuperer():
    id = idchamp.get()

    con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor = con.cursor()
    cursor.execute("select * from produit where id='" + idchamp.get() + "'")
    rows = cursor.fetchall()
    cursor.execute("commit")

    idchamp.delete(0, "end")
    for row in rows:
        idchamp.insert(0, row[0])
        nomchamp.insert(0, row[1])
        datechamp.insert(0, row[3])
        quantitechamp.insert(0, row[2])
        fournisseurchamp.insert(0, row[4])
        telephonechamp.insert(0, row[5])


        afficher()
        con.close()

def ajouter():

    id = idchamp.get()
    nom = nomchamp.get()
    date_arrivee = datechamp.get()
    quantite = quantitechamp.get()
    fournisseur = fournisseurchamp.get()
    telephone = telephonechamp.get()


    if (id == " " or nom == " " or date_arrivee == " " or quantite == " " or fournisseur == " " or telephone == " "):
        messagebox.showinfo("Message d'erreur", "Tout les champs sont réquis")
    else:

        con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
        cursor = con.cursor()
        cursor.execute("insert into produit values('" + id + "','" + nom + "','" + quantite + "','" + date_arrivee + "','" + fournisseur + "','" + telephone + "') ")
        cursor.execute("commit")

        idchamp.delete(0, "end")
        nomchamp.delete(0, "end")
        quantitechamp.delete(0,"end")
        fournisseurchamp.delete(0,"end")
        telephonechamp.delete(0,"end")
        datechamp.delete(0,"end")
    afficher()

    con.close()


def supprimer():
    if (idchamp.get() == " " ):
        messagebox.showinfo("Message d'erreur", "Inserer l'ID");
    else:
        con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
        cursor = con.cursor()
        cursor.execute("delete from produit where id='" + idchamp.get() + "' ")
        cursor.execute("commit")
        afficher()
        con.close()

    idchamp.delete(0, "end")
    nomchamp.delete(0, "end")
    quantitechamp.delete(0, "end")
    fournisseurchamp.delete(0, "end")
    telephonechamp.delete(0, "end")
    datechamp.delete(0,"end")
    afficher()


def modifier():
    id = idchamp.get()
    nom = nomchamp.get()
    date_arrivee = datechamp.get()
    quantite = quantitechamp.get()
    fournisseur = fournisseurchamp.get()
    telephone=telephonechamp.get()

    con = pymysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
    cursor = con.cursor()
    cursor.execute("update produit set id='" + id + "',nom='" + nom + "',quantite='" + quantite + "',date_arr='" + date_arrivee + "',fournisseur='" + fournisseur + "',telephone='" + telephone + "' where id='" + id + " '")
    cursor.execute("commit")

    idchamp.delete(0, "end")
    nomchamp.delete(0, "end")
    quantitechamp.delete(0, "end")
    fournisseurchamp.delete(0, "end")
    telephonechamp.delete(0, "end")
    datechamp.delete(0, "end")


    afficher()
    con.close()

#corrps du code
texte=Label (fenetre8,text="Produits",font=('Calistoga',25),bg="white")
texte.place(x=400,y='',)
ret = Button(fenetre8, text="<<Retour", font=('Calistoga', 15), bg="#d9d9d9",command=retour)
ret.place(x=5, y='', )

id = Label(fenetre8, text="ID",bg="#ffffff",fg="#000000").place(x=50, y=80)
idchamp=Entry(fenetre8,bg="white",width=25,font=('Calistoga',12))
idchamp.place(x=50,y=100,)

nom = Label(fenetre8, text="Nom",bg="#ffffff",fg="#000000").place(x=50, y=130)

nomchamp=Entry(fenetre8,bg="white",width=25,font=('Calistoga',12))
nomchamp.place(x=50,y=150,)

quantite = Label(fenetre8, text="Quantité",bg="#ffffff",fg="#000000").place(x=50, y=180)

quantitechamp=Entry(fenetre8,bg="white",width=25,font=('Calistoga',12))
quantitechamp.place(x=50,y=210,)

date = Label(fenetre8, text="Date d'arrivée",bg="#ffffff",fg="#000000").place(x=340, y=80)

datechamp=Entry(fenetre8,bg="white",width=25,font=('Calistoga',12))
datechamp.place(x=340,y=100,)

fournisseur = Label(fenetre8, text="Fournisseur",bg="#ffffff",fg="#000000").place(x=340, y=130)

fournisseurchamp=Entry(fenetre8,bg="white",width=25,font=('Calistoga',12))
fournisseurchamp.place(x=340,y=150,)

telephone = Label(fenetre8, text="Téléphone",bg="#ffffff",fg="#000000").place(x=340, y=180)

telephonechamp=Entry(fenetre8,bg="white",width=25,font=('Calistoga',12))
telephonechamp.place(x=340,y=210,)


#en tete
aff.heading(1,text="ID")
aff.heading(2,text="Nom")
aff.heading(3,text="Quantité")
aff.heading(4,text="Date d'arrivée")
aff.heading(5,text="Fournisseur")
aff.heading(6,text="Téléphone Founisseur")
#dimension des colonnes
aff.column(1,width=10)
aff.column(2,width=10)
aff.column(3,width=10)
aff.column(4,width=10)
aff.column(5,width=10)
aff.column(6,width=10)

# les buttons modification
pad = customtkinter.CTkButton(master=fenetre8, text="Ajouter", command=ajouter, text_font=('Calistoga', 15),text_color='white',
                              height=20, width=100, border_width=1, corner_radius=3, fg_color="#319BFE")
pad.place(x=150, y=250)
pad = customtkinter.CTkButton(master=fenetre8, text="Supprimer", text_font=('Calistoga', 15), command=supprimer,text_color='white',
                              height=20, width=100, border_width=1, corner_radius=3, fg_color="red")
pad.place(x=300, y=250)
pad = customtkinter.CTkButton(master=fenetre8, text="Modifier", text_font=('Calistoga', 15), command=modifier,text_color='white',
                              height=20, width=100, border_width=1, corner_radius=3, fg_color="#6d071a")
pad.place(x=450, y=250)
pad = customtkinter.CTkButton(master=fenetre8, text="Récupérer", text_font=('Calistoga', 15), command=recuperer,text_color='white',
                              height=20, width=100, border_width=1, corner_radius=3, fg_color="green")
pad.place(x=600, y=250)


#suivante et precedente
pad=Button(master=fenetre8,text="<<Précedente",font=('Calistoga',11),command=quit,fg="#000000",
                                      width=11,bg="#ffffff")
pad.place(x=700,y=580)

pad=Button(master=fenetre8,text="Suivante>>",font=('Calistoga',11),command=quit,fg="#000000",
                                     width=10,bg="#ffffff")
pad.place(x=850,y=580)


#affichage resultat
# aff= ttk.Treeview(fenetre8, columns=(1,2,3,4,5,6),height=10,show="headings")
# aff.place(x='',y='290',width=980,height=280)
#defilement
# bar= ttk.Scrollbar(fenetre8,orient="vertical",command=aff.yview)
# bar.place(x=980,y=290,height=280)


fenetre8.mainloop()