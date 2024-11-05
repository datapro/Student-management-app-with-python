from tkinter import *
import tkinter as tk
import tkinter.messagebox as message
import sqlite3
from tkinter.ttk import Combobox

def connect_db():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      matric_no TEXT, name TEXT, email TEXT, gender TEXT,
                      state TEXT, city TEXT, pin TEXT, address TEXT,
                      dob TEXT, contact TEXT, admission TEXT, department TEXT,
                      course1 TEXT, course2 TEXT, course3 TEXT, course4 TEXT, course5 TEXT )''')
    conn.commit()
    conn.close()

def add():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
    if rollno1.get() == "" or name1.get() == "":
        message.showerror("Error", "All fields are required")
    else:
        cursor.execute("INSERT INTO students (matric_no, name, email, gender, state, city, pin, address, dob, contact, admission, department, course1, course2, course3) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                       (rollno1.get(), name1.get(), email1.get(), gender_cb.get(), leb6.get(), var_lab.get(), pin1.get(), address.get("1.0", END), dob1.get(), contact1.get(), admission1.get(), department_cb.get(), course_cb1.get(), course_cb2.get(), course_cb3.get()))
        conn.commit()
        message.showinfo("Success", "Student added successfully")
        clear()
    conn.close()

def update():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, email=?, gender=?, state=?, city=?, pin=?, address=?, dob=?, contact=?, admission=?, department=?, course1=?, course2=?, course3=? WHERE matric_no=?",
                   (name1.get(), email1.get(), gender_cb.get(), leb6.get(), var_lab.get(), pin1.get(), address.get("1.0", END), dob1.get(), contact1.get(), admission1.get(), department_cb.get(), course_cb1.get(), course_cb2.get(), course_cb3.get(), rollno1.get()))
    conn.commit()
    message.showinfo("Success", "Student updated successfully")
    clear()
    conn.close()


def delete():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE matric_no=?", (rollno1.get(),))
    conn.commit()
    message.showinfo("Success", "Student deleted successfully")
    clear()
    conn.close()


def clear():
    rollno1.delete(0, END)
    name1.delete(0, END)
    email1.delete(0, END)
    gender_cb.set("Select")
    leb6.delete(0, END)
    var_lab.set("")
    pin1.delete(0, END)
    address.delete("1.0", END)
    dob1.delete(0, END)
    contact1.delete(0, END)
    admission1.delete(0, END)
    department_cb.set("Select")
    course_cb1.set("Select")
    course_cb2.set("Select")
    course_cb3.set("Select")

Tobi = tk.Tk()
Tobi.title("Register student")
Tobi.geometry("1300x700+0+0")
Tobi.resizable(0,0)

connect_db()

title = Label(Tobi, text="Manage Student Details", font=("times new roman",20,"bold"), bg="#CC3366", fg="white")
title.place(x=0, y=0, relwidth=1, height=40)


rollno1=Label(Tobi, text="Matric No.", font=("times new roman", 15, "bold"))
rollno1.place(x=10, y=60)
rollno1 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightgreen")
rollno1.place(x=150, y=60, width=200)

name1=Label(Tobi, text="Name", font=("times new roman", 15, "bold"))
name1.place(x=10, y=100)
name1 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightgreen")
name1.place(x=150, y=100, width=200)

email1=Label(Tobi, text="Email", font=("times new roman", 15, "bold"))
email1.place(x=10, y=140)
email1 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightgreen")
email1.place(x=150, y=140, width=200)

gender_cb=Label(Tobi, text="Gender", font=("times new roman", 15, "bold"))
gender_cb.place(x=10, y=180)
gender_cb = Combobox(Tobi, font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
gender_cb['values'] = ("Select", "Male", "Female")
gender_cb.place(x=150, y=180, width=200)

leb6=Label(Tobi, text="State", font=("times new roman", 15, "bold"))
leb6.place(x=10, y=220)
leb6 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightgreen")
leb6.place(x=150, y=220, width=150)

lab8=Label(Tobi, text="City", font=("times new roman", 15, "bold"))
lab8.place(x=330, y=220)
var_lab = StringVar()
lab8 = Entry(Tobi, textvariable=var_lab, font=("times new roman", 15, "bold"), bg="lightgreen")
lab8.place(x=380, y=220, width=110)

Label(Tobi, text="Pin", font=("times new roman", 15, "bold")).place(x=510, y=220)
pin1 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightgreen")
pin1.place(x=560, y=220, width=120)

Label(Tobi, text="Address", font=("times new roman", 15, "bold")).place(x=10, y=260)
address = Text(Tobi, font=("times new roman", 15, "bold"), bg="lightgreen")
address.place(x=150, y=260, width=540, height=100)

Label(Tobi, text="D.O.B", font=("times new roman", 15, "bold")).place(x=360, y=60)
dob1 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightgreen")
dob1.place(x=480, y=60, width=200)

Label(Tobi, text="Contact", font=("times new roman", 15, "bold")).place(x=360, y=100)
contact1 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightgreen")
contact1.place(x=480, y=100, width=200)

Label(Tobi, text="year of AD", font=("times new roman", 15, "bold")).place(x=360, y=140)
admission1 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightgreen")
admission1.place(x=480, y=140, width=200)

Label(Tobi, text="Department", font=("times new roman", 15, "bold")).place(x=360, y=180)
department_cb = Combobox(Tobi, font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
department_cb['values'] = ("Select", "Mass Communication", "Computer Science", "Agric Science", "Business Admin", "Medical Lab", "Others")
department_cb.place(x=480, y=180, width=200)

# Course selection
Label(Tobi, text="Course", font=("times new roman", 15, "bold")).place(x=10, y=400)
course_cb1 = Combobox(Tobi, font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
course_cb1['values'] = ("Select", "COM111", "COM112", "STA111", "GNS101", "GNS127")
course_cb1.place(x=150, y=400, width=140)

Label(Tobi, text="Course", font=("times new roman", 15, "bold")).place(x=10, y=450)
course_cb2 = Combobox(Tobi, font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
course_cb2['values'] = ("Select", "COM111", "COM112", "STA111", "GNS101", "GNS127")
course_cb2.place(x=150, y=450, width=140)

Label(Tobi, text="Course", font=("times new roman", 15, "bold")).place(x=10, y=500)
course_cb3 = Combobox(Tobi, font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
course_cb3['values'] = ("Select", "COM111", "COM112", "STA111", "GNS101", "GNS127")
course_cb3.place(x=150, y=500, width=140)    

# Buttons for actions
add_btn = Button(Tobi, text="Add", font=("times new roman", 15, "bold"), bg="blue", fg="white", cursor="hand2", command=add)
add_btn.place(x=150, y=600, width=120, height=50)

update_btn = Button(Tobi, text="Update", font=("times new roman", 15, "bold"), bg="green", fg="white", cursor="hand2", command=update)
update_btn.place(x=290, y=600, width=120, height=50)

delete_btn = Button(Tobi, text="Delete", font=("times new roman", 15, "bold"), bg="grey", fg="white", cursor="hand2", command=delete)
delete_btn.place(x=430, y=600, width=120, height=50)

clear_btn = Button(Tobi, text="Clear", font=("times new roman", 15, "bold"), bg="orange", fg="white", cursor="hand2", command=clear)
clear_btn.place(x=570, y=600, width=120, height=50)

Tobi.mainloop()
