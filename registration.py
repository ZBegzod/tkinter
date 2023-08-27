from tkinter import *

# from tkinter.ttk import *

base = Tk()
base.geometry('500x500')
base.title("Registration Form")

labl_0 = Label(base, text="Ro'yhattan o'tish", width=20, font=("bold", 20))
labl_0.place(x=120, y=53)

labl_1 = Label(base, text="F.I.O", width=20, font=("bold", 10))
labl_1.place(x=120, y=130)

entry_1 = Entry(base)
entry_1.place(x=240, y=130)

labl_2 = Label(base, text="Email", width=20, font=("bold", 10))
labl_2.place(x=120, y=180)

entry_02 = Entry(base)
entry_02.place(x=240, y=180)

labl_3 = Label(base, text="Jinsi", width=20, font=("bold", 10))
labl_3.place(x=120, y=230)
# varblbl = ()

Radiobutton(base, text="Erkak", padx=5, value=1).place(x=235, y=230)
Radiobutton(base, text="Ayol", padx=20, value=2).place(x=290, y=230)

labl_4 = Label(base, text="Yosh:", width=20, font=("bold", 10))
labl_4.place(x=120, y=280)

entry_02 = Entry(base)
entry_02.place(x=240, y=280)

Button(base, text='Saqlash', width=20, bg='brown', fg='white').place(x=225, y=340)
# it will be used for displaying the registration form onto the window
base.mainloop()
