import os
import openpyxl

from tkinter import *
import customtkinter as ctk

from tkinter import ttk
from tkinter import messagebox

window = ctk.CTk()
ctk.set_appearance_mode('dark')
window.title('User form')

frame = ctk.CTkFrame(master=window)
frame.grid(row=0, column=0, padx=20, pady=10)


def enter_data():
    terms = terms_var.get()

    if not terms == "qabul qilinmadi":
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()

        if first_name and last_name:
            age = age_spinbox.get()
            reg_status = reg_status_var.get()

            course = nums_courses_spinbox.get()
            education_degree = title_combobox.get()

            nationality = nationality_combobox.get()
            semester = nums_semesters_spinbox.get()

            print(
                """
                Ism: {} Familiya: {} Yosh: {}
                Millati: {} Talim darajasi: {}
                Ro'yhattan otish holati: {}
                
            """.format(
                    first_name, last_name, age,
                    nationality, education_degree,
                    reg_status,
                ))

            file_path = "C:\\Users\\user\\Desktop\\Tkinter\\data.xlsx"
            if not os.path.exists(file_path):
                workbook = openpyxl.Workbook()
                sheet = workbook.active

                heading = [
                    "Isim", "Familiya",
                    "Yoshi", "Millati",
                    "Talim darajasi",
                    "Registratsiya holati",
                    "Kurs", "Semistor"
                ]

                sheet.append(heading)
                workbook.save(filename=file_path)
            workbook = openpyxl.load_workbook(filename=file_path)
            sheet = workbook.active
            sheet.append(
                [
                    first_name, last_name, age,
                    nationality, education_degree,
                    reg_status, course, semester
                ]
            )
            workbook.save(filename=file_path)
            messagebox.showinfo(title='Status', message='')
        else:
            messagebox.showwarning(title='ogohlantirish', message='ism familiya majburiy')
    else:
        messagebox.showwarning(
            title='ogohlantirish',
            message='foydalanish shartlariga rozilik bildishiz shart'
        )


# user_information = LabelFrame(frame, text='Foydalanuvchi malumotlari')
# user_information.grid(row=0, column=0, padx=20, pady=10)

first_name_label = ctk.CTkLabel(frame, text='Isim', font=('times', 14))
first_name_label.grid(row=0, column=0)

last_name_label = ctk.CTkLabel(frame, text='Familiya')
last_name_label.grid(row=0, column=1)

first_name_entry = ctk.CTkEntry(
    frame, placeholder_text='isimigizni kirting',
)

first_name_entry.grid(row=1, column=0)

last_name_entry = ctk.CTkEntry(frame, placeholder_text='familyangizni kiriting')
last_name_entry.grid(row=1, column=1)

title_label = ctk.CTkLabel(frame, text='Talim darajasi')
title_label.grid(row=0, column=2)

title_combobox = ctk.CTkOptionMenu(frame, values=[
    "Boshlang'ich talim", "O'rta talim", "Yuqori talim"
])
title_combobox.grid(row=1, column=2)

age_label = ctk.CTkLabel(frame, text="Yosh")
age_label.grid(row=2, column=0)


def slider_event(value):
    age_data = value
    age_spinbox_result = ctk.CTkLabel(master=frame, text=age_data)
    age_spinbox_result.grid(row=4, column=0)


age_spinbox = ctk.CTkEntry(frame)
age_spinbox.grid(row=3, column=0)

nationality_label = ctk.CTkLabel(frame, text='Millati')
nationality_label.grid(row=2, column=1)

nationality_combobox = ctk.CTkOptionMenu(frame, values=[
    'Uzbekiston', 'Tojikiston', 'Qozoqiston', 'Turkmaniston'
])
nationality_combobox.grid(row=3, column=1)

for widget in frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# courses_frame = LabelFrame(frame)
# courses_frame.grid(row=1, column=0, sticky='news', padx=20, pady=10)

courses_frame = ctk.CTkFrame(master=window)
courses_frame.grid(row=1, column=0, sticky='news', padx=20, pady=10)

registered_label = ctk.CTkLabel(courses_frame, text='Registratsiya holati')
registered_label.grid(row=0, column=0)

reg_status_var = StringVar(value="ro'yhattan o'tmagan")
registered_check = ctk.CTkCheckBox(
    courses_frame,
    text='joriy holati',
    variable=reg_status_var,
    onvalue="ro'yhattan o'tgan",
    offvalue="ro'yhattan o'tmagan",
)

registered_check.grid(row=1, column=0)

nums_courses_label = ctk.CTkLabel(courses_frame, text='# Yakunlagan kurs')
nums_courses_label.grid(row=0, column=1)

nums_courses_spinbox = ctk.CTkEntry(courses_frame)
nums_courses_spinbox.grid(row=1, column=1)

nums_semesters_label = ctk.CTkLabel(courses_frame, text='# Semester')
nums_semesters_label.grid(row=0, column=2)

nums_semesters_spinbox = ctk.CTkEntry(courses_frame)
nums_semesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


terms_frame = ctk.CTkFrame(window)
terms_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

terms_var = StringVar(value='qabul qilinmadi')
terms_check = ctk.CTkCheckBox(
    terms_frame,
    text='Men foydalanish shartlariga roziman',
    variable=terms_var,
    onvalue='qabul qilindi',
    offvalue='qabul qilinmadi'
)
terms_check.grid(row=1, column=0)

button = ctk.CTkButton(window, text='malumot kiriting', command=enter_data)
button.grid(row=3, column=0, sticky='news', padx=20, pady=10)

window.mainloop()
