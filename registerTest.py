import customtkinter
from tkinter import messagebox
import tkinter
from PIL import ImageTk, Image
import pyodbc as dbo

# database connection
global conn
try:
    conn = dbo.connect(
        "DRIVER={SQL SERVER};"
        "SERVER=Velagasseth\\SQLEXPRESS;"
        "DATABASE=velagasdb;"
        "TRUSTED_CONNECTION=YES")
    print("connection successfull!")



except Exception:
    print("Connection Faill")

global name1, surname1


def put(conn):
    global name1, surname1
    try:
        surname = entry.get()
        name = entry1.get()
        test_password = entry2.get()
        if name[0].islower() or surname[0].islower():
            name1 = name.capitalize()
            surname1 = surname.capitalize()
            password1 = entry3.get()
            # putting restrictions
            cursor = conn.cursor()
            query = "SELECT * FROM Student_1"
            cursor.execute(query)
            cursor.commit()

            if password1 != test_password:
                entry3.configure(placeholder_text="*incorrect match!", placeholder_text_color="red", border_color="red")
            else:
                ID = entry4.get()
                if 8 < len(ID) > 8:
                    entry4.configure(placeholder_text="*invalid format", placeholder_text_color="red",
                                     border_color="red")
                else:
                    cursor = conn.cursor()

                    cursor.execute("SELECT * FROM Student_1 WHERE Surname=?", surname1)
                    rows = cursor.fetchone()
                    print(rows)
                    if rows:
                        messagebox.showerror("fail", 'User already exists!')
                    else:
                        query3 = "INSERT INTO Student_1(Surname, Username, Password, ID_No) values(?, ?, ?, ?) "
                        data = (surname1, name1, password1, ID)
                        cursor.execute(query3, data)
                        cursor.commit()
                        full.pack()

        else:
            password1 = entry3.get()
            # putting restrictions
            cursor = conn.cursor()
            query = "SELECT * FROM Student_1"
            cursor.execute(query)
            cursor.commit()

            if password1 != test_password:
                entry3.configure(placeholder_text="*incorrect match!", placeholder_text_color="red", border_color="red")
            else:
                ID = entry4.get()
                if 8 < len(ID) > 8:
                    entry4.configure(placeholder_text="*invalid format", placeholder_text_color="red",
                                     border_color="red")
                elif 4 < entry2.get() > 4:
                    entry2.configure(border_color="red",text_color="red")
                    entry2.insert(0, "*invalid format")
                else:
                    cursor = conn.cursor()

                    cursor.execute("SELECT * FROM Student_1 WHERE Surname=?", surname)
                    rows = cursor.fetchone()
                    print(rows)
                    if rows:
                        messagebox.showerror("fail", 'User already exists!')
                    else:
                        query3 = "INSERT INTO Student_1(Surname, Username, Password, ID_No) values(?, ?, ?, ?) "
                        data = (surname, name, password1, ID)
                        cursor.execute(query3, data)
                        cursor.commit()
                        full.pack()






    except IndexError:
        entry1.configure(placeholder_text="*enter username", placeholder_text_color="red", border_color="red")
    except NameError:
        entry1.configure(placeholder_text="*invalid format", placeholder_text_color="red", border_color="red")


def write():
    put(conn)


def login():
    window1.destroy()
    import loginTest


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
window1 = customtkinter.CTk()
HEIGHT1 = 600
WIDTH1 = 600
screen_height = window1.winfo_screenheight()
screen_width = window1.winfo_screenwidth()
x = int((screen_width / 2) - (WIDTH1 / 2))
y = int((screen_height / 2) - (HEIGHT1 / 2))
window1.geometry(f"{WIDTH1}X{HEIGHT1}+{x}+{y}")
window1.title("SethVelagas")
#window.resizable(False, False)

label3 = customtkinter.CTkLabel(window1, text="Velagasseth-TECH", font=("constantia", 36, "bold"))
label3.pack(pady=60)

my_image = ImageTk.PhotoImage(Image.open("pictures\\Business Salesman.gif"))
li = customtkinter.CTkLabel(window1, image=my_image)
li.pack()

frame1 = customtkinter.CTkFrame(li, corner_radius=20, )
frame1.place(relx=0.5, rely=0.5, y=-60, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(frame1, text="register here", font=("constantia", 36, "bold"))
label.pack(padx=60, pady=40)

full = customtkinter.CTkLabel(frame1, font=("Ink Free", 20, "bold"), text="Sign in successful 👍!", text_color="green")
full.pack_forget()
loginBtn2 = customtkinter.CTkButton(frame1, text="login!", font=("Century Gothic", 14),
                                    text_color="blue", fg_color="transparent",
                                    width=50, hover=False, cursor="hand2", command=login)
loginBtn2.place(x=200, y=505)
logLabel = customtkinter.CTkLabel(frame1, text=" have an account?", font=("Century Gothic", 14))
logLabel.place(x=80, y=505)

entry = customtkinter.CTkEntry(frame1, font=("Ink Free", 20, "bold"), placeholder_text="Surname", width=250,
                               height=40)
entry.pack(padx=20, pady=20)

entry1 = customtkinter.CTkEntry(frame1, font=("Ink Free", 20, "bold"), placeholder_text="Username", width=250,
                                height=40)
entry1.pack(padx=20, pady=20)
entry2 = customtkinter.CTkEntry(frame1, font=("Ink Free", 20, "bold"), placeholder_text="Pin", width=250, show="*",
                                height=40)
entry2.pack(padx=20, pady=20)
entry3 = customtkinter.CTkEntry(frame1, font=("Ink Free", 20, "bold"), placeholder_text="Confirm pin",
                                width=250,
                                height=40)
entry3.pack(padx=20, pady=20)

entry4 = customtkinter.CTkEntry(frame1, font=("Ink Free", 20, "bold"), placeholder_text="ID_Number",
                                width=250,
                                height=40)
entry4.pack(padx=20, pady=20)

submitBtn2 = customtkinter.CTkButton(frame1, text="Sign up", font=("constantia", 20, 'bold'), width=250,
                                     command=write)
submitBtn2.pack(padx=60, pady=10)

window1.mainloop()
