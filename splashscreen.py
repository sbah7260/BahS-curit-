import time
from tkinter import *
from PIL import ImageTk, Image
from subprocess import call
import tkinter
import customtkinter as customtkinter

# Create object
root=Tk()
root.geometry("800x550+200+100")
root.iconbitmap("22926756.ico")
root.config(background="#FFFFFF")
root.title("splashscreen")
# root.resizable(False,False)
label = customtkinter.CTkLabel(master=root,text="Bah Sécurité",text_color='#46887C',text_font=('regular',50),corner_radius=8)
label.place(x=400, y=200,anchor=tkinter.CENTER)
# main window function
def main():
    # destroy splash window
    root.destroy()
    root.after(2500, main)
    call(["python", "connexion.py"])
    # Execute tkinter
    # root = Tk()
    # Adjust size
    # root.geometry("400x400")

    # # Set Interval





# label1 = Label(root, text="Loading ....", font=20)
# label1.configure(font=("Calibri", 11))
# label1.place(x=80, y=200)


image_b = ImageTk.PhotoImage(Image.open('c2.png'))
image_a = ImageTk.PhotoImage(Image.open('image1.png'))



for i in range (5):
    l1 = Label(root, image=image_b,bg="#000000", border=0, relief=SUNKEN).place(x=320,y=280)
    l2 = Label(root, image=image_a,bg="#000000",  border=0, relief=SUNKEN).place(x=350, y=280)
    l3 = Label(root, image=image_a,bg="#000000",  border=0, relief=SUNKEN).place(x=380, y=280)
    l4 = Label(root, image=image_a,bg="#000000",  border=0, relief=SUNKEN).place(x=410, y=280)
    root.update_idletasks()
    time.sleep(0.5)

    l1 = Label(root, image=image_a,bg="#000000",  border=0, relief=SUNKEN).place(x=320,y=280)
    l2 = Label(root, image=image_b,bg="#000000",  border=0, relief=SUNKEN).place(x=350,y=280)
    l3 = Label(root, image=image_a,bg="#000000",  border=0, relief=SUNKEN).place(x=380,y=280)
    l4 = Label(root, image=image_a,bg="#000000",  border=0, relief=SUNKEN).place(x=410,y=280)
    root.update_idletasks()
    time.sleep(0.5)


    l1 = Label(root, image=image_a,bg="#000000",  border=0, relief=SUNKEN).place(x=320,y=280)
    l2 = Label(root, image=image_a,bg="#000000",  border=0, relief=SUNKEN).place(x=350,y=280)
    l3 = Label(root, image=image_b,bg="#000000",  border=0, relief=SUNKEN).place(x=380,y=280)
    l4 = Label(root, image=image_a,bg="#000000",  border=0, relief=SUNKEN).place(x=410,y=280)
    root.update_idletasks()
    time.sleep(0.5)

    l1 = Label(root, image=image_a,bg="#000000",  border=0, relief=SUNKEN).place(x=320,y=280)
    l2 = Label(root, image=image_a,bg="#000000",  border=0, relief=SUNKEN).place(x=350,y=280)
    l3 = Label(root, image=image_a,bg="#000000",  border=0, relief=SUNKEN).place(x=380,y=280)
    l4 = Label(root, image=image_b,bg="#000000",  border=0, relief=SUNKEN).place(x=410,y=280)
    root.update_idletasks()
    time.sleep(0.5)


main()
# Execute tkinter
root.mainloop()