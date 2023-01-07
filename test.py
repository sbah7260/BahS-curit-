import tkinter
import customtkinter

# root_tk = tkinter.Tk()  # create the Tk window like you normally do
# root_tk.geometry("400x240")
# root_tk.title("CustomTkinter Test")

# def button_function():
#     print("button pressed")
#
# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#
# root_tk.mainloop()
# def button_event():
#     print("button pressed")

# customtkinter.set_appearance_mode("Dark") # Other: "Light", "System" (only macOS)
#
# button = customtkinter.CTkButton(master=root_tk,
#                                  fg_color=("white", "lightgray"),  # <- tuple color for light and dark theme
#                                  text="CTkButton",
#                                  command=button_event)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# customtkinter.enable_macos_darkmode()
# customtkinter.set_appearance_mode("System")
#
#
#
# customtkinter.disable_macos_darkmode()
# label = customtkinter.CTkLabel(master=root_tk,
#                                text="CTkLabel",
#                                width=120,
#                                height=25,
#                                corner_radius=8)
# label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#
# entry = customtkinter.CTkEntry(master=root_tk,
#                                width=120,
#                                height=25,
#                                corner_radius=10)
# entry.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)
#
# text = entry.get()
#
#
#
#
# frame = customtkinter.CTkFrame(master=root_tk,
#                                width=200,
#                                height=200,
#                                corner_radius=10)
# frame.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)
#
# def slider_event(value):
#     print(value)
#
# slider = customtkinter.CTkSlider(master=root_tk,
#                                  width=160,
#                                  height=16,
#                                  border_width=5.5,
#                                  command=slider_event)
# slider.place(relx=0.8, rely=0.9, anchor=tkinter.CENTER)

# progressbar = customtkinter.CTkProgressBar(master=root_tk,
#                                            width=160,
#                                            height=20,
#                                            border_width=5)
# progressbar.place(relx=0.9, rely=0.1, anchor=tkinter.CENTER)
#
# progressbar.set()

# root_tk.mainloop()


# from tkcalendar import Calendar, DateEntry
# def example1():
#     def print_sel():
#         print(cal.selection_get())
#         cal.see(datetime.date(year=2016, month=2, day=5))
#
#     top = tk.Toplevel(root)
#
#     import datetime
#     today = datetime.date.today()
#
#     mindate = datetime.date(year=2018, month=1, day=21)
#     maxdate = today + datetime.timedelta(days=5)
#     print(mindate, maxdate)
#
#     cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
#                    mindate=mindate, maxdate=maxdate, disabledforeground='red',
#                    cursor="hand1", year=2018, month=2, day=5)
#     cal.pack(fill="both", expand=True)
#     ttk.Button(top, text="ok", command=print_sel).pack()
#
#
# def example2():
#
#     top = tk.Toplevel(root)
#
#     cal = Calendar(top, selectmode='none')
#     date = cal.datetime.today() + cal.timedelta(days=2)
#     cal.calevent_create(date, 'Hello World', 'message')
#     cal.calevent_create(date, 'Reminder 2', 'reminder')
#     cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
#     cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')
#
#     cal.tag_config('reminder', background='red', foreground='yellow')
#
#     cal.pack(fill="both", expand=True)
#     ttk.Label(top, text="Hover over the events.").pack()
#
#
# def example3():
#     top = tk.Toplevel(root)
#
#     ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
#
#     cal = DateEntry(top, width=12, background='darkblue',
#                     foreground='white', borderwidth=2, year=2010)
#     cal.pack(padx=10, pady=10)
#
#
# root = tk.Tk()
# ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
# ttk.Button(root, text='Calendar with events', command=example2).pack(padx=10, pady=10)
# ttk.Button(root, text='DateEntry', command=example3).pack(padx=10, pady=10)
#
#
#
# root.mainloop()
from tkinter import *
from tkinter import ttk
import tkinter



import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
#
# root = tk.Tk()
# root.title('Treeview demo')
# root.geometry('620x200')
#
# # define columns
# columns = ('first_name', 'last_name', 'email','prix')
#
# tree = ttk.Treeview(root, columns=columns, show='headings')
#
# # define headings
# tree.heading('first_name', text='First Name')
# tree.heading('last_name', text='Last Name')
# tree.heading('email', text='Email')
# tree.heading('prix', text='Prix')
#
# # generate sample data
# # contacts = []
# # for n in range(1, 100):
# #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
# #
# # # add data to the treeview
# # for contact in contacts:
# #     tree.insert('', tk.END, values=contact)
#
#
# def item_selected(event):
#     for selected_item in tree.selection():
#         item = tree.item(selected_item)
#         record = item['values']
#         # show a message
#         showinfo(title='Information', message=','.join(record))
#
#
# tree.bind('<<TreeviewSelect>>', item_selected)
# tree.place(x=0,y=280)
# # grid(row=100, column=100, sticky='nsew')
#
# # add a scrollbar
# scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
# tree.configure(yscroll=scrollbar.set)
# scrollbar.place(x=800,y=300)
# # grid(row=100, column=200, sticky='ns')
# # t.place(x=0,y=280)
#
# # run the app
# root.mainloop()
import tkinter as tk

import customtkinter as CTk
import customtkinter


root_tk = tk.Tk()
root_tk.geometry("400x340")
# custom_entry = customtkinter.CTkEntry(root_tk)   #CTkEntry
# custom_entry.pack()
entry = customtkinter.CTkEntry(root_tk)
entry.pack(pady=100, padx=100)

root_tk.mainloop()
