
from tkinter import *
import tkinter as tk
import sqlite3
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter import messagebox
import subprocess


conn = sqlite3.connect('student.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      firstname TEXT, lastname TEXT, email TEXT, contact TEXT,
                      phone TEXT, dob TEXT, password TEXT, usertype TEXT)''')
conn.commit()




def signup_user():
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    phone = phone_entry.get()
    dob = dob_entry.get()
    password = password_entry.get()
    usertype = usertype_combobox.get()

    if not all([firstname, lastname, email, contact, phone, dob, password, usertype]) or usertype == "Select":
        messagebox.showerror("Error", "All fields are required")
    else:
        conn = sqlite3.connect('student.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (firstname, lastname, email, contact, phone, dob, password, usertype) "
                       "VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (firstname, lastname, email, contact, phone, dob, password, usertype))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Registration successful!")
        Tobi.destroy() 
        signin_page()  


# Sign-in Functionality
def signin_user():
    email = signin_email_entry.get()
    password = signin_password_entry.get()
    usertype = signin_usertype_combobox.get()

    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=? AND password=? AND usertype=?", (email, password, usertype))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Success", f"Welcome, {user[1]}! You are logged in as {usertype}.")
        if usertype == "Student":
            subprocess.Popen(["python", "student result.py"])
            student_dashboard()
        elif usertype == "Admin":
            subprocess.Popen(["python", "adminn.py"])
            admin_dashboard()
    else:
        messagebox.showerror("Error", "Invalid credentials. Please try again.")
    conn.close()


# Clear sign-up form fields
def clear_signup_fields():
    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    email_entry.delete(0, END)
    contact_entry.delete(0, END)
    phone_entry.delete(0, END)
    dob_entry.delete(0, END)
    password_entry.delete(0, END)
    usertype_combobox.set("Select")


# Open Sign-up Window
def signup_page():
    global Tobi, firstname_entry, lastname_entry, email_entry, contact_entry, phone_entry, dob_entry, password_entry, usertype_combobox

    Tobi = tk.Tk()
    Tobi.geometry("1300x700+0+0")
    Tobi.title("Sign Up")
    Tobi.config(bg="red")
    Tobi.resizable(0, 0)

    background_image = Image.open("images/6.1.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(Tobi, image=background_photo)
    background_label.place(x=0, y=60, relwidth=1, relheight=1)

    reg=Label(Tobi, text="Register as Student or Admin", font=("times new roman", 20, "bold"), bg="#CC3366", fg="white")
    reg.place(x=0, y=0, relwidth=1, height=60)

    firstname=Label(Tobi, text="Firstname:", font=("sanserif", 20), fg="#fff", bg="#057ABF")
    firstname.place(x=70, y=100)
    firstname_entry = Entry(Tobi, width=50)
    firstname_entry.place(x=235, y=110)

    lastname=Label(Tobi, text="Lastname:", font=("sanserif", 20), fg="#fff", bg="#00A3E6")
    lastname.place(x=650, y=100)
    lastname_entry = Entry(Tobi, width=50)
    lastname_entry.place(x=800, y=110)

    email=Label(Tobi, text="Email:", font=("sanserif", 20), fg="#fff", bg="#057ABF")
    email.place(x=70, y=170)
    email_entry = Entry(Tobi, width=50)
    email_entry.place(x=235, y=180)

    contact=Label(Tobi, text="Contact:", font=("sanserif", 20), fg="#fff", bg="#00A3E6")
    contact.place(x=650, y=170)
    contact_entry = Entry(Tobi, width=50)
    contact_entry.place(x=800, y=180)

    age=Label(Tobi, text="Age:", font=("sanserif", 20), fg="#fff", bg="#057ABF")
    age.place(x=70, y=240)
    phone_entry = Entry(Tobi, width=50)
    phone_entry.place(x=235, y=250)

    dob=Label(Tobi, text="DOB:", font=("sanserif", 20), fg="#fff", bg="#00A3E6")
    dob.place(x=650, y=240)
    dob_entry = Entry(Tobi, width=50)
    dob_entry.place(x=800, y=250)

    password=Label(Tobi, text="Password:", font=("sanserif", 20), fg="#fff", bg="#057ABF")
    password.place(x=70, y=310)
    password_entry = Entry(Tobi, width=50, show="*")
    password_entry.place(x=235, y=320)

    usertype=Label(Tobi, text="User Type", font=("sanserif", 20, "bold"), bg="#00A3E6", fg="white")
    usertype.place(x=650, y=300)
    usertype_combobox = Combobox(Tobi, font=("sanserif", 15), state="readonly", justify=CENTER)
    usertype_combobox['values'] = ("Select", "Student", "Admin")
    usertype_combobox.place(x=800, y=300, width=150)

    signup=Button(Tobi, text="Sign-up", height=2, width=25, bg="#CC3366", fg="#fff", command=signup_user)
    signup.place(x=70, y=600)
    signup1=Button(Tobi, text="Clear", height=2, width=25, bg="orange", fg="#fff", command=clear_signup_fields)
    signup1.place(x=300, y=600)
    signup2=Button(Tobi, text="sign in", height=2, width=25, bg="green", fg="#fff", command=lambda: [Tobi.destroy(), signin_page()])
    signup2.place(x=530, y=600)
    Tobi.mainloop()



def signin_page():
    global signin_email_entry, signin_password_entry, signin_usertype_combobox

    TOBI = tk.Tk()
    TOBI.geometry("1300x700+0+0")
    TOBI.title("Sign In")
    TOBI.resizable(0, 0)

    Label(TOBI, text="Sign in", font=("times new roman", 20, "bold"), bg="#CC3366", fg="white").place(x=0, y=0, relwidth=1, height=60)

    background_image = Image.open("images/6.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(TOBI, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    Framelogin = Frame(TOBI, bg="gray")
    Framelogin.place(x=450, y=100, height=550, width=500)

    lab = Label(Framelogin, text="LOGIN HERE", font=("sanserif", 30, "bold"), fg="green", bg="gray", underline=5)
    lab.place(x=130, y=10)

    inframe = Image.open("images/logo1.jpg")
    inframe_photo = ImageTk.PhotoImage(inframe)
    inframe_label = tk.Label(Framelogin, image=inframe_photo)
    inframe_label.place(x=150, y=80)

    lab1 = Label(Framelogin, text="Username:", font=("sanserif", 20), fg="black", bg="gray", underline=5)
    lab1.place(x=70, y=270)
    signin_email_entry = Entry(Framelogin, width=50, bg="lightyellow")
    signin_email_entry.place(x=70, y=320)

    lab2 = Label(Framelogin, text="Password:", font=("sanserif", 20), fg="black", bg="gray", underline=5)
    lab2.place(x=70, y=350)
    signin_password_entry = Entry(Framelogin, width=50, bg="lightyellow", show="*")
    signin_password_entry.place(x=70, y=400)

    user=Label(Framelogin, text="User Type", font=("sanserif", 20, "bold"), bg="gray", fg="black")
    user.place(x=70, y=420)
    signin_usertype_combobox = Combobox(Framelogin, font=("sanserif", 15), state="readonly", justify=CENTER)
    signin_usertype_combobox['values'] = ("Select", "Student", "Admin")
    signin_usertype_combobox.place(x=70, y=460, width=150)

    loginbtn = Button(Framelogin, text="Sign-in", height=2, width=25, bg="red", fg="#fff", command=signin_user)
    loginbtn.place(x=70, y=500)

    backtobtn = Button(Framelogin, text="Sign up", height=2, width=25, bg="green", fg="#fff", command=lambda: [TOBI.destroy(), signup_page()])
    backtobtn.place(x=250, y=500)

    TOBI.mainloop()


# Placeholder functions for student and admin dashboards
def student_dashboard():
    messagebox.showinfo("Dashboard", "Welcome to the Student Dashboard")

def admin_dashboard():
    messagebox.showinfo("Dashboard", "Welcome to the Admin Dashboard")

if __name__ == "__main__":
    signup_page()
