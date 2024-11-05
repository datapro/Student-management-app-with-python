from tkinter import *
import tkinter as tk
import sqlite3
import subprocess
from PIL import Image, ImageTk
from tkinter import ttk

def open_add_student_result():
    subprocess.Popen(["python", "listresults.py"]) 

def register():
    subprocess.Popen(["python", "register student.py"]) 
def view_student_result():
    subprocess.Popen(["python", "student result.py"])
def open_view_student():
    # Create a new Tkinter window
    tobi = tk.Toplevel()
    tobi.title("Registered Students")
    tobi.geometry("1300x700+0+0")

    # Connect to the database
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")  
    rows = cursor.fetchall()
    conn.close()

    
    tree = ttk.Treeview(tobi, columns=("DOB", "FirstName","LastName", "Email", "Contact"), show="headings")
    tree.heading("DOB", text="DOB")
    tree.heading("FirstName", text="FirstName")
    tree.heading("LastName", text="LastName")
    tree.heading("Email", text="Email")
    tree.heading("Contact", text="Contact")
    tree.pack(fill="both", expand=True)

    # Insert data into the Treeview
    for row in rows:
        tree.insert("", tk.END, values=row)

    # If no students are registered, show a message
    if not rows:
        label = tk.Label(tobi, text="No registered students found.")
        label.pack()

        
Tobi = tk.Tk()
Tobi.title("Register student")
Tobi.geometry("1300x1000+0+0")
Tobi.resizable(0,0,)
background_image = Image.open("images/6.2.webp")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(Tobi, image=background_photo)
background_label.place(x=0, y=50, relwidth=1, relheight=1)

reg=Label(Tobi, text="admin dashboard", font=("times new roman", 20, "bold"), bg="#CC3366", fg="white")
reg.place(x=0, y=0, relwidth=1, height=60)

signup=Button(Tobi, text="register student", height=5, width=30, bg="#CC3366", fg="#fff", command=register)
signup.place(x=100, y=150)
signup1=Button(Tobi, text="add student result", height=5, width=30, bg="orange", fg="#fff", command=open_add_student_result)
signup1.place(x=330, y=150)
signup2=Button(Tobi, text="view student", height=5, width=30, bg="green", fg="#fff", command=open_view_student)
signup2.place(x=560, y=150)
signup3=Button(Tobi, text="view student result", height=5, width=30, bg="gray", fg="#fff", command=view_student_result)
signup3.place(x=790, y=150)
Tobi.mainloop()

