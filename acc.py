from tkinter import *
import tkinter as tk
import customtkinter
import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
from subprocess import call
from tkinter import messagebox as mb
import pymysql as pymysql
from tkinter import messagebox
import pickle

root=Tk()
root.geometry("800x550+200+100")
root.iconbitmap("22926756.ico")
# root.config(background="#FFFFFF")
# root.resizable(False,False)
root.title("Acc")
customtkinter.set_appearance_mode("System")
f1 = Frame(root, width=2000, height=70, bg='#46887C').place(x=0, y=0)
f2 = Frame(root, width=250, height=800, bg='#4E1B1B').place(x=0, y=70)
label = Label(f1,text="Bah Sécurité",fg="#ffffff",bg='#46887C',font=('regular',40,))
# label.place(x=310,y=15)
label.pack(padx=110, pady=0)
Label(f2,text="Acceuil",fg="#3A9EB4",bg='#4E1B1B',font=('regular',25,)).place(x=60,y=75)


def hide_me(widget):
    widget.place_forget()

def Agent():
    root.destroy()
    call(["python","agent.py"])
def Client():
    root.destroy()
    call(["python","client.py"])
def Paiement():
    root.destroy()
    call(["python","paiement.py"])
def Equipement():
    root.destroy()
    call(["python","Equipement.py"])
def rdv():
    root.destroy()
    call(["python","RDV.py"])
def Salaire():
    root.destroy()
    call(["python","salaire.py"])
def Quitter():
    res=mb.askquestion('Quitter Application','Voulez-vous quitter?')
    if res == 'yes':
        root.destroy()
        call(["python", "connexion.py"])

def nb_agent():
    con = pymysql.connect(host="localhost", user="root", password="sidi", database='gardiennage')
    curser = con.cursor()
    curser.execute("SELECT COUNT(nom) FROM agent")
    for row in curser:
        r = row[0]
        val = str(r)
    return val

    con.close();

def nb_client():
    con = pymysql.connect(host="localhost", user="root", password="sidi", database='gardiennage')
    curser = con.cursor()
    curser.execute("SELECT COUNT(nom) FROM client")
    for row in curser:
        r = row[0]
        val = str(r)
    return val

    con.close();

# DESERIALISATION
with open("test.pickle", "rb") as infile:
    res = pickle.load(infile)
print(res)
i = res[0]
profil = i[3]
nom = i[2]
idS = i[0]

    #les boutons
button1 = customtkinter.CTkButton(master=root, text="Agent", fg_color=("#3A9EB4", "#3A9EB4") ,bg_color='#4E1B1B',text_color='#ffffff',text_font=("regular",13),corner_radius=12,command=Agent)
button1.place(x=50,y=160)
button2 = customtkinter.CTkButton(master=root, text="Client", fg_color=("#3A9EB4", "#3A9EB4"),bg_color='#4E1B1B',text_color='#ffffff',text_font=("regular",13),corner_radius=12,command=Client)
button2.place(x=50,y=220)
button3 = customtkinter.CTkButton(master=root, text="Paiement", fg_color=("#3A9EB4", "#3A9EB4"),bg_color='#4E1B1B',text_color='#ffffff',text_font=("regular",13),corner_radius=12,command=Paiement)
button3.place(x=50,y=270)
button4 = customtkinter.CTkButton(master=root, text="Salaire", fg_color=("#3A9EB4", "#3A9EB4"),bg_color='#4E1B1B',text_color='#ffffff',text_font=("regular",13),corner_radius=12,command=Salaire)
button4.place(x=50,y=330)
button5 = customtkinter.CTkButton(master=root, text="Equipement", fg_color=("#3A9EB4", "#3A9EB4"),bg_color='#4E1B1B',text_color='#ffffff',text_font=("regular",13),corner_radius=10,command=Equipement)
button5.place(x=50,y=390)
button6 = customtkinter.CTkButton(master=root, text="RDV", fg_color=("#3A9EB4", "#3A9EB4"),bg_color='#4E1B1B',text_color='#ffffff',text_font=("regular",13),corner_radius=12,command=rdv)
button6.place(x=50,y=450)
button7 = customtkinter.CTkButton(master=root, text="Quitter", fg_color=("red", "red"),bg_color='#4E1B1B',text_color='#ffffff',text_font=("regular",13),corner_radius=12,command=Quitter)
button7.place(x=50,y=510)

#frame stat
stat2 = customtkinter.CTkFrame(root,fg_color='#3A9EB4',highlightthickness=4,width=300,height=150,corner_radius=10)
stat2.place(x=350,y=150)

stat1 = customtkinter.CTkFrame(root,fg_color='#46887C',highlightthickness=4,width=300,height=150,corner_radius=10)
stat1.place(x=350,y=350)

#STATISTIQUE
label1 = Label(stat1,borderwidth=0,relief=SUNKEN,text="Agent",font=("Arial bold",30),
                   bg='#46887C',fg="#FFFFFF")
label1.place(x=90,y=10)

l1= Label(stat1,borderwidth=0,relief=SUNKEN,text=nb_agent(),font=("Arial bold",20),
                   bg='#46887C',foreground="#FFFFFF")
l1.place(x=90,y=90,width=100,height=20)

label2 = Label(stat2,borderwidth=0,relief=SUNKEN,text="Client",font=("Arial bold",30),
                   bg='#3A9EB4',fg="#FFFFFF")
label2.place(x=90,y=10)

l2 = Label(stat2,borderwidth=0,relief=SUNKEN,text=nb_client(),font=("Arial bold",20),
                   bg='#3A9EB4',foreground="#FFFFFF")
l2.place(x=90,y=90,width=100,height=20)


if(profil == 'Formateur'):
    hide_me(button2)
    hide_me(button3)
    hide_me(button4)
    hide_me(button6)
    button1.place(x=50,y=200)
    button5.place(x=50,y=355)
elif(profil == 'Sécrétaire'):
    hide_me(button1)
    hide_me(button3)
    hide_me(button4)
    hide_me(button5)
    button2.place(x=50, y=200)
    button6.place(x=50, y=355)
elif(profil == 'Comptable'):
    hide_me(button1)
    hide_me(button2)
    hide_me(button5)
    hide_me(button6)
    button3.place(x=50, y=200)
    button4.place(x=50, y=355)
print(profil)
infile.close()
with open("doc.pickle","wb") as outfile:
    pickle.dump(profil,outfile)
outfile.close()
with open("id.pickle","wb") as outfile:
    pickle.dump(idS,outfile)
outfile.close()

root.mainloop()

# global root
#
#
# def oui():
#     print("GOOD BYE !!!")
#     root.destroy()
#
#
# def non():
#     print("Ok je reste !")
#     fenTop.destroy()
#     root.deiconify()
#
#
# root.withdraw()
# fenTop = tk.Toplevel()
# msg = tk.Message(fenTop, text="Voulez-vous quitter?")
# msg.pack()
# btnoui = tk.Button(fenTop, text="Oui", command=oui)
# btnoui.pack()
#
# btnnon = tk.Button(fenTop, text="Non", command=non)
# btnnon.pack()