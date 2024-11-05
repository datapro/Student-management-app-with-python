from tkinter import *
import tkinter as tk
import tkinter.messagebox as message
import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    matric_no TEXT PRIMARY KEY,
                    name TEXT,
                    course TEXT,
                    marks1 INTEGER,
                    marks2 INTEGER,
                    exam INTEGER
                  )''')
conn.commit()


def search_student():
    matric_no = txt_entry.get()
    cursor.execute("SELECT * FROM student_results WHERE matric_no=?", (matric_no,))
    student = cursor.fetchone()

    if student:
        name_entry.insert(0, f"{student[2]} {student[1]}")
        matric_entry.insert(0, student[0])
        course.config(text=student[4])
        course1.config(text=student[5])
        course2.config(text=student[6])
        course3.config(text=student[7])
        course4.config(text=student[8])
        marks.config(text=student[9])
        marks1.config(text=student[10])
        marks2.config(text=student[12])
        marks3.config(text=student[13])
        marks4.config(text=student[15])
        full.config(text=student[16])
        full1.config(text=student[18])
        full2.config(text=student[19])
        full3.config(text=student[21])
        full4.config(text=student[22])
        percentage.config(text=student[11])
        percentage1.config(text=student[14])
        percentage2.config(text=student[17])
        percentage3.config(text=student[20])
        percentage4.config(text=student[23])
    else:
        message.showerror("Error", "No record found for this matric number.")

def close_app():
    Tobi.destroy()

def clear():
    txt_entry.delete(0, END)
    name_entry.delete(0, END)
    matric_entry.delete(0, END)
    course.delete(0, END)
    course1.delete(0, END)
    course2.delete(0, END)
    course3.delete(0, END)
    course4.delete(0, END)
    marks.delete(0, END)
    marks1.delete(0, END)
    marks2.delete(0, END)
    marks3.delete(0, END)
    marks4.delete(0, END)
    full.delete(0, END)
    full1.delete(0, END)
    full2.delete(0, END)
    full3.delete(0, END)
    full4.delete(0, END)
    percentage.delete(0, END)
    percentage1.delete(0, END)
    percentage2.delete(0, END)
    percentage3.delete(0, END)
    percentage4.delete(0, END)


Tobi = tk.Tk()
Tobi.title("Register student")
Tobi.geometry("1300x700+0+0")
Tobi.resizable(0,0)
Tobi.config(bg="gray")


title=Label(Tobi,text="Student Results Management ",font=("times new roman",20,"bold"),bg="#CC3366",fg="white")
title.place(x=0,y=0,relwidth=1,height=40)

lbl_select = Label(Tobi,text="Enter Your Matric No.",font=("times new roman",20,"bold"),bg="gray")
lbl_select.place(x=240,y=100)
txt_entry= Entry(Tobi,font=("times new roman",20),bg="lightyellow")
txt_entry.place(x=520,y=100,width=150)

name = Label(Tobi,text="Name.",font=("times new roman",20,"bold"),bg="gray")
name.place(x=240,y=150)
name_entry= Entry(Tobi,font=("times new roman",20),bg="lightyellow")
name_entry.place(x=520,y=150,width=380)

matric = Label(Tobi,text="Matric num.",font=("times new roman",20,"bold"),bg="gray")
matric.place(x=240,y=195)
matric_entry= Entry(Tobi,font=("times new roman",20),bg="lightyellow")
matric_entry.place(x=520,y=195,width=380)

btn_search=Button(Tobi,text="Search",font=("times new roman",15,"bold"),bg="lightblue",fg="black",cursor="hand2", command=search_student)
btn_search.place(x=680,y=100,width=100,height=35)

btn_clear=Button(Tobi,text="Clear",font=("times new roman",15,"bold"),bg="lightgreen",fg="black",cursor="hand2", command=clear)
btn_clear.place(x=800,y=100,width=100,height=35)

lbl_course = Label(Tobi,text="Course",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
lbl_course.place(x=300,y=250,width=150,height=50)
lbl_marks = Label(Tobi,text="1st Text",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
lbl_marks.place(x=450,y=250,width=150,height=50)
lbl_full = Label(Tobi,text="2nd Text",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
lbl_full.place(x=600,y=250,width=150,height=50)
lbl_percentage = Label(Tobi,text="Exam",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
lbl_percentage.place(x=750,y=250,width=150,height=50)


course = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
course.place(x=300,y=300,width=150,height=50)
marks = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
marks.place(x=450,y=300,width=150,height=50)
full = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
full.place(x=600,y=300,width=150,height=50)
percentage = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
percentage.place(x=750,y=300,width=150,height=50)


course1 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
course1.place(x=300,y=350,width=150,height=50)
marks1 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
marks1.place(x=450,y=350,width=150,height=50)
full1 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
full1.place(x=600,y=350,width=150,height=50)
percentage1 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
percentage1.place(x=750,y=350,width=150,height=50)


course2 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
course2.place(x=300,y=400,width=150,height=50)
marks2 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
marks2.place(x=450,y=400,width=150,height=50)
full2 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
full2.place(x=600,y=400,width=150,height=50)
percentage2 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
percentage2.place(x=750,y=400,width=150,height=50)


course3 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
course3.place(x=300,y=450,width=150,height=50)
marks3 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
marks3.place(x=450,y=450,width=150,height=50)
full3 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
full3.place(x=600,y=450,width=150,height=50)
percentage3 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
percentage3.place(x=750,y=450,width=150,height=50)


course4 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
course4.place(x=300,y=500,width=150,height=50)
marks4= Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
marks4.place(x=450,y=500,width=150,height=50)
full4 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
full4.place(x=600,y=500,width=150,height=50)
percentage4 = Label(Tobi,font=("times new roman",15,"bold"),bg="white",relief=GROOVE)
percentage4.place(x=750,y=500,width=150,height=50)

btn_delete=Button(Tobi,text="close",font=("times new roman",15,"bold"),bg="#CC3366",fg="white",cursor="hand2", command=close_app)
btn_delete.place(x=500,y=580,width=150,height=35)
Tobi.mainloop()