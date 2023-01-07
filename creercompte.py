from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter
from subprocess import call
import customtkinter as customtkinter
import pymysql as pymysql
from tkinter import messagebox
root = Tk()
root.geometry("800x550+200+100")
root.iconbitmap("22926756.ico")
# root.config(background="#FFFFFF")
# root.resizable(False,False)
customtkinter.set_appearance_mode("System")

root.title("Créercompte")

def Annuler():
    root.destroy()
    call(["python","connexion.py"])

def valider():
    nom = e1.get()
    prenom = e2.get()
    numero = e3.get()
    profil = e4.get()
    mdp = e5.get()
    rmdp = e6.get()

    if(nom==""or prenom=="" or numero==""or profil==""or mdp=="" or rmdp==""):
        messagebox.showinfo("Erreur:", "Aucun champ ne doit être vide")
    elif (mdp != rmdp):
        messagebox.showinfo("Information", "Votre mot de passe est différent de celui de la confirmation")
    elif (len(mdp)<8):
        messagebox.showinfo("Information", "Votre mot de passe ne doit pas être inferieur à 8 caractère")
    else:
        sql = "INSERT INTO personnels(nom,prenom,numero,profil,mdp,rmdp)" \
              " VALUES (%s,%s,%s,%s,%s,%s) "


        valeur = (nom,prenom,numero,profil,mdp,rmdp)
        con = pymysql.connect(host="localhost", user="root", password="sidi", database="gardiennage")
        cursor = con.cursor()
        cursor.execute(sql, valeur)
        con.commit()
        messagebox.showinfo("Information", "insertion effectuer")
        root.destroy()
        call(["python","connexion.py"])


f1 = Frame(root, width=2000, height=70, bg='#46887C').place(x=0, y=0)
l1 = Label(f1,text="Inscription",fg="#ffffff",bg='#46887C',font=('regular',25,))
# l1.place(x=310,y=12)
l1.pack(padx=110, pady=5)
nom = Label(root,text="Nom",fg="#000000",font=('regular',15,)).place(x=80,y=80)
prenom =  Label(root,text="Prénom",fg="#000000",font=('regular',15,)).place(x=80,y=160)
numero = Label(root,text="Numéro",fg="#000000",font=('regular',15,)).place(x=80,y=240)
profil = Label(root,text="Profil",fg="#000000",font=('regular',15,)).place(x=450,y=80)
mdp = Label(root,text="Mot de passe",fg="#000000",font=('regular',15,)).place(x=450,y=160)
rmdp = Label(root,text="Répéter mot de passe",fg="#000000",font=('regular',15,)).place(x=450,y=240)


e1 = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
e1.place(x=180,y=130, anchor=tkinter.CENTER)
e2 = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
e2.place(x=180,y=215, anchor=tkinter.CENTER)
e3 = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
e3.place(x=180,y=300, anchor=tkinter.CENTER)
e4 = ttk.Combobox(root,values = ['DG','Sécrétaire','Comptable','Formateur'],width=20,height=100,font=(30))
e4.place(x=450,y=120)
e4.current()
e5 = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
e5.place(x=550,y=215, anchor=tkinter.CENTER)
e6 = customtkinter.CTkEntry(master=root,width=200,height=30,fg_color="#ffffff",corner_radius=8)
e6.place(x=550,y=300, anchor=tkinter.CENTER)
style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", background="gray90", fieldbackground="white",highlightthickness=0, bd=0, foreground="black")
style.configure("mystyle.Treeview.Heading", font=('Calibri', 8,'bold'))

button = customtkinter.CTkButton(master=root, text="Annuler", fg_color=("#46887C", "#46887C"),text_color='#ffffff',text_font=("regular",15),command=Annuler)
button.place(x=300,y=370)
button = customtkinter.CTkButton(master=root, text="Valider", fg_color=("#46887C", "#46887C"),text_color='#ffffff',text_font=("regular",15),command=valider)
button.place(x=500,y=370)


root.mainloop()