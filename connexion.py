from tkinter import *
import tkinter
import customtkinter
from PIL import Image,ImageTk
import pymysql as pymysql
from tkinter import messagebox
from tkinter import Entry
from tkinter import ttk
from subprocess import call

import pickle
root=Tk()
root.geometry("800x550+200+100")
root.iconbitmap("22926756.ico")
root.config(background="#E00FFF")
# root.resizable(False,False)
root.title("Connexion")
customtkinter.set_appearance_mode("System")

def cachermdp():

    if champ2.cget('show') == '':
        champ2.configure(show='*')
        btn_afficher.config(image=image2)
    else:
        champ2.configure(show='')
        btn_afficher.config(image=image)

def connecter():
    nomutl = champ1.get()
    mdp = champ2.get()
    if (nomutl == "" or mdp == ""):
        messagebox.showinfo("Echec", "Aucun champs ne doit être vide")
    else:
        try:
            sql = "SELECT * FROM personnels WHERE profil =%s AND mdp =%s"
            valeur = (nomutl,mdp)
            con = pymysql.connect(host="localhost", user="root", password="sidi", database='gardiennage')
            curser = con.cursor()
            curser.execute(sql,valeur)
            resultat =curser.fetchall()
            if resultat:
                messagebox.showinfo("INFO", "Connecter avec succès")
                res = resultat
                with open("test.pickle", "wb") as outfile:
                    pickle.dump(res, outfile)
                outfile.close()
                root.destroy()
                call(["python", "acc.py"])
            else:
                messagebox.showinfo("Erreur", "Nom d'utilisateur ou mot de passe incorrect")
        except:
            messagebox.showinfo("Erreur", "Problème de connexion")


def inscrire():
    root.destroy()
    call(["python","creercompte.py"])



frame = Frame(root, width=400, height=400)
frame.pack(padx=190, pady=80)
frame1 = Frame(frame, width=400, height=50, bg='#46887C').place(x=0, y=0)

Label(frame,text="Connexion",fg="#ffffff",bg='#46887C',font=('regular',25,)).place(x=130,y=0)
nomutl = customtkinter.CTkLabel(master=frame,text="Nom d'utilisateur",text_font=('regular',12,),corner_radius=8)
nomutl.place(x=160 , y=95, anchor=tkinter.CENTER)
Label(frame,text="*",fg="red",font=('regular',30,)).place(x=250,y=80)
# champ1 = ttk.Entry(master=frame, width=13,font=('regular',20,))
# champ1.place(x=100,y=100)
champ1 = ttk.Combobox(master=frame,values = ['DG','Sécrétaire','Comptable','Formateur'],width=20,height=200,font=(30))
champ1.place(x=100,y=120)
champ1.current()
mdp =  customtkinter.CTkLabel(master=frame,text="Mot de passe",text_font=('regular',12,),corner_radius=8)
mdp.place(x=150 , y=170, anchor=tkinter.CENTER)
Label(frame,text="*",fg="red",font=('regular',30,)).place(x=220,y=155)
champ2 = ttk.Entry(master=frame, show="*", width=13,font=('regular',20,))
champ2.place(x=100,y=200)

# placeholder_text="Entrez mot de passe",
# ,placeholder_text="Entrez nom d'utilisateur"
image = PhotoImage(file="eye.png")
image2 = PhotoImage(file="invisible.png")
btn_afficher = Button(frame,image=image2, command=cachermdp)
btn_afficher.place(x=265,y=205)
button = customtkinter.CTkButton(master=frame ,text="Se connecter", fg_color=("#46887C", "#46887C"),width=200,height=30,text_color='#ffffff',text_font=("regular",15),command=connecter)
button.place(x=100,y=280)


label = customtkinter.CTkLabel(master=frame,text="Pas de compte ?",text_font=('regular',12,),corner_radius=8)
label.place(x=150, y=350, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=frame ,text="S’inscrire", fg_color=("#ffffff", "#ffffff"),text_color='#46887C',text_font=("regular",15),command=inscrire)
button.place(x=240,y=335)


style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", background="gray90", fieldbackground="white", highlightthickness=0, bd=0,
                foreground="black")
style.configure("mystyle.Treeview.Heading", font=('Calibri', 8, 'bold'))

root.mainloop()


# e1= Entry(frame,textvariable=a,width=30,font=("", 12))
# e1.place(x=20,y=100)
# e1.insert(0,"Nom d’utilisateur")
# e1.bind("<Button>",userText)
#
# # Label(frame,text="Mot de passe",bg="#FFFFFF").place(x=320,y=180)
# e2= Entry(frame,textvariable=b,width=30,font=("", 13))
# e2.place(x=20,y=150)
# e2.insert(0,"Mot de passe")
# e2.bind("<Button>",passText)


# button = Button(frame, text="Se connecter", bg='#46887C', fg='#ffffff', width=30,  font=("regular",13),command=connecter)
# button.place(x=20,y=200)
# def userText(event):
#     e1.delete(0,END)
#     usercheck=True
## Label(frame,text="Pas de compte ?",fg="#000000",font=('regular',12,)).place(x=100,y=360)
# def passText(event):
#     e2.delete(0, END)
#     passcheck=True
# a=StringVar()
# b=StringVar()
# usercheck=True
# passcheck=True
# button = Button(frame, text="S’inscrire", fg='#46887C', font=("regular",12),command=inscrire)
# button.place(x=220,y=320)
# Label(frame,text="Nom d’utilisateur",bg="#FFFFFF").place(x=320,y=130)
# image1=PhotoImage(file="C:\\Users\\BAH\\PycharmProjects\\Gardiennage\\ferme3.png")
# x=Label(root,image=image1)
# image2=PhotoImage(file="C:\\Users\\BAH\\PycharmProjects\\Gardiennage\\ferme3.png")
# y=Label(root,image=image2)
#
# bt_affiche=Button(frame,command=cachermdp,image=image1,width=30,height=30)
# bt_affiche.place(x=250,y=170)