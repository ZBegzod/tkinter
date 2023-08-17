from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title('User form')
# window.geometry('600x400')

frame = Frame(window)
frame.pack(side=LEFT)


# frame2 = Frame(window, highlightthickness=3, highlightbackground='red')
# frame2.pack(side=RIGHT)

def enter_data():
    terms = terms_var.get()

    if not terms == "qabul qilinmadi":
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()

        if first_name and last_name:
            age = age_spinbox.get()
            reg_status = reg_status_var.get()

            education_degree = title_combobox.get()
            nationality = nationality_combobox.get()

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
        else:
            messagebox.showwarning(title='ogohlantirish', message='ism familiya majburiy')
    else:
        messagebox.showwarning(
            title='ogohlantirish',
            message='foydalanish shartlariga rozilik bildishiz shart'
        )


user_information = LabelFrame(frame, text='Foydalanuvchi malumotlari')
user_information.grid(row=0, column=0, padx=20, pady=10)

first_name_label = Label(user_information, text='Isim')
first_name_label.grid(row=0, column=0)

last_name_label = Label(user_information, text='Familiya')
last_name_label.grid(row=0, column=1)

first_name_entry = Entry(user_information)
first_name_entry.grid(row=1, column=0)

last_name_entry = Entry(user_information)
last_name_entry.grid(row=1, column=1)

title_label = Label(user_information, text='Talim darajasi')
title_label.grid(row=0, column=2)

title_combobox = ttk.Combobox(user_information, values=[
    "Boshlang'ich talim", "O'rta talim", "Yuqori talim"
])
title_combobox.grid(row=1, column=2)

age_label = Label(user_information, text="Yosh")
age_label.grid(row=2, column=0)

age_spinbox = Spinbox(user_information, from_=18, to=100)
age_spinbox.grid(row=3, column=0)

nationality_label = Label(user_information, text='Millati')
nationality_label.grid(row=2, column=1)

nationality_combobox = ttk.Combobox(user_information, values=[
    'Uzbekiston', 'Tojikiston', 'Qozoqiston', 'Turkmaniston'
])
nationality_combobox.grid(row=3, column=1)

for widget in user_information.winfo_children():
    widget.grid_configure(padx=10, pady=5)

courses_frame = LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky='news', padx=20, pady=10)

registered_label = Label(courses_frame, text='Registratsiya holati')
registered_label.grid(row=0, column=0)

reg_status_var = StringVar(value="ro'yhattan o'tmagan")
registered_check = Checkbutton(
    courses_frame,
    text='joriy holati',
    variable=reg_status_var,
    onvalue="ro'yhattan o'tgan",
    offvalue="ro'yhattan o'tmagan",
)

registered_check.grid(row=1, column=0)

nums_courses_label = Label(courses_frame, text='# Yakunlagan kurs')
nums_courses_label.grid(row=0, column=1)

nums_courses_spinbox = Spinbox(courses_frame, from_=0, to='infinity')
nums_courses_spinbox.grid(row=1, column=1)

nums_semesters_label = Label(courses_frame, text='# Simistor')
nums_semesters_label.grid(row=0, column=2)

nums_semesters_spinbox = Spinbox(courses_frame, from_=0, to='infinity')
nums_semesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = LabelFrame(frame, text='Foydalanish Shartlari')
terms_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

terms_var = StringVar(value='qabul qilinmadi')
terms_check = Checkbutton(
    terms_frame,
    text='Men foydalanish shartlariga roziman',
    variable=terms_var,
    onvalue='qabul qilindi',
    offvalue='qabul qilinmadi'
)
terms_check.grid(row=1, column=0)

button = Button(frame, text='malumot kiriting', command=enter_data)
button.grid(row=3, column=0, sticky='news', padx=20, pady=10)

window.mainloop()
