import tkinter as tk
from tkinter import messagebox
from time import sleep

def record():
    global name
    global password


    name=entry_name.get()
    password=entry_password.get()
    if name == 'test' and password == 'qwerty':
        messagebox.showinfo('SUCCESS', 'VALID LOGIN')
    else:
        print('ERROR. INVALID LOGIN')

def start_login():
    with open ('users_list.txt', 'r') as users:
        users_list=[user.strip() for user in users.readlines()]

    with open ('passwords_list.txt', 'r') as passwords:
        passwords_list=[password.strip() for password in passwords.readlines()]
    

    for user in users_list:
        for pas in passwords_list:
            
            entry_name.delete(0, tk.END)
            entry_password.delete(0, tk.END)

            entry_name.insert(0, user)
            entry_password.insert(0, tk.END)

            if user == 'test' and pas == 'qwerty':
                print(f'{user} | {pas}')
                return

            record()
            sleep(0.2)


def create_window():
    global window
    global entry_name
    global entry_password


    window=tk.Tk()
    window.title('LOGIN SCREEN')
    window.geometry('500x300')

    tk.Label(window, text='User').pack()
    entry_name=tk.Entry(window)
    entry_name.pack()

    tk.Label(window, text='Password').pack()
    entry_password=tk.Entry(window, show='*')
    entry_password.pack()

    tk.Button(window, text='LOGIN', command=record).pack()


    start_login()

    window.mainloop()