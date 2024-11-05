from tkinter import *
import tkinter as tk
import tkinter.messagebox as message
import sqlite3
import subprocess
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter import messagebox

Tobi = tk.Tk()
Tobi.title("student result")
Tobi.geometry("1300x700+0+0")
Tobi.resizable(0,0)
Tobi.config(bg="gray")

def save_student_results():
    matric_no = matric_entry.get()
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    department = department_cb.get()
    course1 = course_cb1.get()
    course2 = course_cb2.get()
    course3 = course_cb3.get()
    course4 = course_cb4.get()
    course5 = course_cb5.get()
    test1 = rol.get()
    test2 = rol1.get()
    exam1 = rol2.get()
    test3 = crol.get()
    test4 = crol1.get()
    exam2 = crol2.get()
    test5 = trol.get()
    test6 = trol1.get()
    exam3 = trol2.get()
    test7 = trol1.get()
    test8 = trol11.get()
    exam4 = trol21.get()
    test9 = trol12.get()
    test10 = trol112.get()
    exam5 = trol212.get()
    
    if matric_no and firstname and lastname and department != "Select":
        try:
            # Connect and create table if not exists
            conn = sqlite3.connect("student.db")
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS student_results (
                    matric_no TEXT PRIMARY KEY,
                    firstname TEXT,
                    lastname TEXT,
                    department TEXT,
                    course1 TEXT,
                    course2 TEXT,
                    course3 TEXT,
                    course4 TEXT,
                    course5 TEXT,
                    test1 TEXT,
                    test2 TEXT,
                    exam1 TEXT,
                    test3 TEXT,
                    test4 TEXT,
                    exam2 TEXT,
                    test5 TEXT,
                    test6 TEXT,
                    exam3 TEXT,
                    test7 TEXT,
                    test8 TEXT,
                    exam4 TEXT,
                    test9 TEXT,
                    test10 TEXT,
                    exam5 TEXT
                )
            """)
            
            cursor.execute("""
                INSERT OR REPLACE INTO student_results VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (matric_no, firstname, lastname, department, course1, course2, course3, course4, course5,
                  test1, test2, exam1, test3, test4, exam2, test5, test6, exam3, test7, test8, exam4, test9, test10, exam5))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Student results saved successfully!")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error saving results: {e}")
    else:
        messagebox.showwarning("Input Error", "Please fill in all required fields")

def close_app():
    Tobi.destroy()




matric=Label(Tobi, text="Matric No.", font=("times new roman", 25, "bold"), bg="gray")
matric.place(x=10, y=80)
matric_entry = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
matric_entry.place(x=200, y=85, width=250)

firstname=Label(Tobi, text="Firstname.", font=("times new roman", 25, "bold"), bg="gray")
firstname.place(x=10, y=140)
firstname_entry = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
firstname_entry.place(x=200, y=145, width=250)

lastname=Label(Tobi, text="Lastname.", font=("times new roman", 25, "bold"), bg="gray")
lastname.place(x=10, y=200)
lastname_entry = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
lastname_entry.place(x=200, y=205, width=250)

dep=Label(Tobi, text="Department.", font=("times new roman", 25, "bold"), bg="gray")
dep.place(x=10, y=260)
department_cb = Combobox(Tobi, font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
department_cb['values'] = ("Select", "Mass Communication", "Computer Science", "Agric Science", "Business Admin", "Medical Lab", "Others")
department_cb.place(x=200, y=265, width=200)

first_text=Label(Tobi, text="1st test.", font=("times new roman", 25, "bold"), bg="gray")
first_text.place(x=400, y=340)

second_text=Label(Tobi, text="Second test.", font=("times new roman", 25, "bold"), bg="gray")
second_text.place(x=700, y=340)

exam=Label(Tobi, text="Exam.", font=("times new roman", 25, "bold"), bg="gray")
exam.place(x=1000, y=340)

reg=Label(Tobi, text="add student results", font=("times new roman", 20, "bold"), bg="#CC3366", fg="white")
reg.place(x=0, y=0, relwidth=1, height=60)

cou=Label(Tobi, text="Course", font=("times new roman", 15, "bold"), bg="gray")
cou.place(x=25, y=400)
course_cb1 = Combobox(Tobi, font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
course_cb1['values'] = ("Select", "COM111", "COM112", "STA111", "GNS101", "GNS127")
course_cb1.place(x=165, y=400, width=140)

cou1=Label(Tobi, text="Course", font=("times new roman", 15, "bold"), bg="gray")
cou1.place(x=25, y=450)
course_cb2 = Combobox(Tobi, font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
course_cb2['values'] = ("Select", "COM111", "COM112", "STA111", "GNS101", "GNS127")
course_cb2.place(x=165, y=450, width=140)

cou3=Label(Tobi, text="Course", font=("times new roman", 15, "bold"), bg="gray")
cou3.place(x=25, y=500)
course_cb3 = Combobox(Tobi, font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
course_cb3['values'] = ("Select", "COM111", "COM112", "STA111", "GNS101", "GNS127")
course_cb3.place(x=165, y=500, width=140)

cou4=Label(Tobi, text="Course", font=("times new roman", 15, "bold"), bg="gray")
cou4.place(x=25, y=550)
course_cb4 = Combobox(Tobi, font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
course_cb4['values'] = ("Select", "COM111", "COM112", "STA111", "GNS101", "GNS127")
course_cb4.place(x=165, y=550, width=140)

cou5=Label(Tobi, text="Course", font=("times new roman", 15, "bold"), bg="gray")
cou5.place(x=25, y=600)
course_cb5 = Combobox(Tobi, font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
course_cb5['values'] = ("Select", "COM111", "COM112", "STA111", "GNS101", "GNS127")
course_cb5.place(x=165, y=600, width=140)

rol = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
rol.place(x=400, y=400, width=200)

rol1 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
rol1.place(x=700, y=400, width=200)

rol2 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
rol2.place(x=1000, y=400, width=200)

crol = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
crol.place(x=400, y=450, width=200)

crol1 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
crol1.place(x=700, y=450, width=200)

crol2 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
crol2.place(x=1000, y=450, width=200)

trol = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
trol.place(x=400, y=500, width=200)

trol1 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
trol1.place(x=700, y=500, width=200)

trol2 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
trol2.place(x=1000, y=500, width=200)

trol1 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
trol1.place(x=400, y=550, width=200)

trol11 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
trol11.place(x=700, y=550, width=200)

trol21 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
trol21.place(x=1000, y=550, width=200)

trol12 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
trol12.place(x=400, y=600, width=200)

trol112 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
trol112.place(x=700, y=600, width=200)

trol212 = Entry(Tobi, font=("times new roman", 15, "bold"), bg="lightyellow")
trol212.place(x=1000, y=600, width=200)

add=Button(Tobi, text="save student results", height=5, width=30, bg="#CC3366", fg="#fff", command=save_student_results)
add.place(x=600, y=130)
close=Button(Tobi, text="close", height=5, width=30, bg="green", fg="#fff", command=close_app)
close.place(x=900, y=130)
Tobi.mainloop()