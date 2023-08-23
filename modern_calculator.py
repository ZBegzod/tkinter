from tkinter import *
import customtkinter as ctk

window = ctk.CTk()
ctk.set_appearance_mode('light')
window.geometry("334x308")
# window.resizable(False, False)
window.title("Calculator")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def btn_clear():
    global expression
    expression = ""
    input_text.set(expression)


def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


expression = ""
input_text = StringVar()

input_frame = ctk.CTkFrame(
    window,
    border_width=0,
    width=312, height=50,
)
input_frame.pack()

input_field = ctk.CTkEntry(
    input_frame,
    textvariable=input_text,
    width=330, font=('times', 24, 'bold'),
    bg_color="#eee", border_width=0,
    justify=RIGHT
)

input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btn_frame = ctk.CTkFrame(
    master=window,
    width=312,
    height=270,
)
btn_frame.pack()

clear = ctk.CTkButton(
    btn_frame,
    text="C",

    fg_color="orange",
    border_width=0,
    bg_color="#eee",
    width=250, height=50,
    command=btn_clear
)
clear.grid(
    row=0, column=0,
    columnspan=3,
    padx=1, pady=1
)

divide = ctk.CTkButton(
    btn_frame,
    border_width=0, text="/",
    cursor="hand2",
    fg_color="orange",
    width=80, height=50,
    # text_color="#eee",
    command=lambda: btn_click("/"),
)

divide.grid(
    row=0, column=3,
    padx=1, pady=1
)

seven = ctk.CTkButton(
    btn_frame,
    text="7",
    # cursor='hand2',
    width=80, height=50, border_width=0,
    fg_color="black",
    # bg_color="#fff",
    command=lambda: btn_click(7)
)
seven.grid(row=1, column=0, padx=1, pady=1)

eight = ctk.CTkButton(
    btn_frame,
    text="8",
    width=80, height=50,
    border_width=0,
    # cursor='hand2',
    # text_color="#fff",
    fg_color="black",
    command=lambda: btn_click(8)
)
eight.grid(row=1, column=1, padx=1, pady=1)

nine = ctk.CTkButton(
    btn_frame,
    text="9", fg_color="black",
    width=80, height=50,
    border_width=0,
    # cursor="hand2",
    command=lambda: btn_click(9),
    # text_color="#fff",
)
nine.grid(
    row=1, column=2,
    padx=1, pady=1
)

multiply = ctk.CTkButton(
    btn_frame,
    width=80, height=50,
    text="*", fg_color="orange",
    border_width=0, bg_color="#eee",
    # cursor="hand2",
    command=lambda: btn_click("*")
)
multiply.grid(row=1, column=3, padx=1, pady=1)

four = ctk.CTkButton(
    btn_frame, text="4",
    width=80, height=50,
    # text_color="#fff",
    fg_color="black",
    command=lambda: btn_click(4),
    # cursor="hand2",
    border_width=0,
)
four.grid(row=2, column=0, padx=1, pady=1)

five = ctk.CTkButton(
    btn_frame, text="5",
    fg_color="black",
    # text_color="#fff",
    width=80, height=50,
    border_width=0,
    # cursor="hand2",
    command=lambda: btn_click(5)
)
five.grid(row=2, column=1, padx=1, pady=1)

six = ctk.CTkButton(
    btn_frame,
    text="6", fg_color="black", width=80, height=50,
    border_width=0, bg_color="#fff",
    # cursor="hand2",
    command=lambda: btn_click(6)
)
six.grid(
    row=2, column=2,
    padx=1, pady=1
)

minus = ctk.CTkButton(
    btn_frame,
    text="-", fg_color="orange",
    width=80, height=50,
    border_width=0, bg_color="#eee",
    # cursor="hand2",
    command=lambda: btn_click("-")
)
minus.grid(
    row=2, column=3,
    padx=1, pady=1
)
one = ctk.CTkButton(
    btn_frame,
    text="1", fg_color="black",
    width=80, height=50,
    border_width=0, bg_color="#fff",
    # cursor="hand2",
    command=lambda: btn_click(1)
)
one.grid(
    row=3, column=0,
    padx=1, pady=1
)

two = ctk.CTkButton(
    btn_frame,
    text="2", fg_color="black",
    width=80, height=50,
    border_width=0, bg_color="#fff",
    command=lambda: btn_click(2)
)
two.grid(
    row=3, column=1,
    padx=1, pady=1
)

three = ctk.CTkButton(
    btn_frame,
    text="3", fg_color="black",
    width=80, height=50,
    border_width=0, bg_color="#fff",
    command=lambda: btn_click(3)
)
three.grid(
    row=3, column=2,
    padx=1, pady=1
)

plus = ctk.CTkButton(
    btn_frame,
    text="+", fg_color="orange", width=80,
    height=50, border_width=0, bg_color="#eee",
    command=lambda: btn_click("+"))
plus.grid(row=3, column=3, padx=1, pady=1)

zero = ctk.CTkButton(
    btn_frame,
    text="0", fg_color="black",
    width=160, height=50,
    border_width=0, bg_color="#fff",
    # cursor="hand2",
    command=lambda: btn_click(0)
)
zero.grid(
    row=4, column=0,
    padx=1, pady=1,
    columnspan=2,
)

point = ctk.CTkButton(
    btn_frame,
    text=".", fg_color="black",
    width=80, height=50,
    border_width=0, bg_color="#eee",
    command=lambda: btn_click(".")
)

point.grid(
    row=4, column=2,
    padx=1, pady=1
)

equals = ctk.CTkButton(
    btn_frame,
    text="=", fg_color="orange",
    width=80, height=50,
    border_width=0, bg_color="#eee",
    command=lambda: bt_equal()
)
equals.grid(
    row=4, column=3,
    padx=1, pady=1
)

window.mainloop()
