import pyodbc as dbo
import customtkinter
import tkinter
from tkinter import messagebox
from time import *

#Database connection
try:
    conn = dbo.connect(
        "DRIVER={SQL SERVER};"
        "SERVER=Velagasseth\\SQLEXPRESS;"
        "DATABASE=velagasdb;"
        "TRUSTED_CONNECTION=YES")
    print("connection successfull!")

except Exception:
    print("Connection Faill")

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
window = customtkinter.CTk()
HEIGHT = 600
WIDTH = 600
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
x = int((screen_width / 2) - (WIDTH / 2))
y = int((screen_height / 2) - (HEIGHT / 2))
window.geometry(f"{WIDTH}X{HEIGHT}+{x}+{y}")
window.title("SethVelagas")


#window.resizable(False, False)


def push():
    new_ctk(conn)


def register():
    loading.pack()
    sleep(1)
    window.destroy()
    import registerTest


#loading background image
my_image = tkinter.PhotoImage(file="pictures\\Business Salesman.gif")
li = customtkinter.CTkLabel(window, image=my_image)
li.pack()

frame = customtkinter.CTkFrame(li, corner_radius=20, )
frame.place(relx=0.5, rely=0.5, y=-40, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(frame, text="Login System", font=("constantia", 36, "bold"))
label.pack(padx=60, pady=40)

entry1 = customtkinter.CTkEntry(frame, font=("Ink Free", 20, "bold"), placeholder_text="Username", width=250, height=40)
entry1.pack(padx=20, pady=20)
entry2 = customtkinter.CTkEntry(frame, font=("Ink Free", 20, "bold"), placeholder_text="Password", show="*", width=250,
                                height=40)
entry2.pack(padx=20, pady=20)
l2 = customtkinter.CTkLabel(frame, text="forget password", font=("Century Gothic", 13), cursor="hand2")
l2.place(x=230, y=320)
loading = customtkinter.CTkLabel(frame, text=" ", font=("Century Gothic", 20, "bold"),
                                 text_color="#0B7EF3")
loading.pack_forget()


def my_terms():
    pass


def my_check():
    if check_var.get() == "on":
        checkBox.configure(text="Procceed!")
    else:
        checkBox.configure(text="remember me?")


check_var = customtkinter.StringVar(value="off")
checkBox = customtkinter.CTkCheckBox(frame, text="remember me?", font=("constantia", 16,), fg_color="white",
                                     hover_color="white", variable=check_var, onvalue="on", command=my_check)
checkBox.pack(padx=5, pady=10)
lc = customtkinter.CTkLabel(frame, text="don't have an account?", font=("Century Gothic", 14))
lc.pack(pady=10, padx=20, anchor=tkinter.W)
loginBtn = customtkinter.CTkButton(frame, text="register!", font=("Century Gothic", 14),
                                   text_color="blue", fg_color="transparent",
                                   width=50, hover=False, cursor="hand2", command=register)
loginBtn.place(x=180, y=340)
check_error = customtkinter.CTkLabel(frame, text="")
check_error.place(x=60, y=100)

global username1, userEntry


def new_ctk(conn):
    global username1, userEntry
    username = entry1.get().lower()
    password = entry2.get()

    if username == "" or password == "":
        entry1.configure(placeholder_text="*Username", placeholder_text_color="red")
        entry2.configure(placeholder_text="*Password", placeholder_text_color="red")

        check_error.configure(text="Fill the place with Asterisk(s)!", text_color="red", font=("ink free", 18, 'bold'))
    else:
        try:
            if username[0].islower():
                username1 = username.capitalize()
                dialog = customtkinter.CTkInputDialog(
                    text=f"Hello {username1}, please enter your age\nto access the platform",
                    title="Scan test",
                    font=("constantia", 18, 'bold'))
                userEntry = int(dialog.get_input())
                print("Age is ", userEntry)
            else:
                dialog = customtkinter.CTkInputDialog(
                    text=f"Hello {username}, please enter your age\nto access the platform",
                    title="Scan test",
                    font=("constantia", 18, 'bold'))
                userEntry = int(dialog.get_input())
                print("Age is ", userEntry)

        except NameError:
            check_error.configure(text="Invalid credential!", text_color="red",
                                  font=("ink free", 22, 'bold'))
            entry1.configure(border_color="red")
        except ValueError:
            check_error.configure(text="   Login fail!!", text_color="red",
                                  font=("ink free", 24, 'bold'))
            submitBtn.configure(text="retry")

        except TypeError:
            check_error.configure(text="   Login fail!!", text_color="red",
                                  font=("ink free", 24, 'bold'))
            submitBtn.configure(text="retry")

        if userEntry >= 18:
            cursor5 = conn.cursor()
            cursor6 = conn.cursor()
            cursor5.execute("SELECT * FROM Student_1 WHERE Username=?", username1)
            rows = cursor5.fetchone()
            print(rows)

            if rows is None:
                messagebox.showerror("Invalid", "Invalid credentials please register ")
            else:
                customtkinter.set_appearance_mode('light')
                customtkinter.set_default_color_theme('green')
                new_root = customtkinter.CTk()

                # setting up the resizable geometry
                HEIGHT2 = 700
                WIDTH2 = 800
                screen2_height = new_root.winfo_screenheight()
                screen2_width = new_root.winfo_screenwidth()
                x1 = int((screen2_width / 2) - (WIDTH2 / 2))
                y2 = int((screen2_height / 2) - (HEIGHT2 / 2))

                new_root.geometry(f"{WIDTH}X{HEIGHT}+{x1}+{y2}")

                new_root.title('Velagasseth')
                #new_root.resizable(False, False)

                welcome = customtkinter.CTkLabel(new_root, text=f"Welcome {username1} 👋",
                                                 font=("constantia", 34, 'bold'))
                welcome.pack(padx=10, pady=5)
                logoBtn = customtkinter.CTkButton(new_root, text=f"{username1[0]}", font=("constantia", 38, 'bold'),
                                                  height=50, width=50, corner_radius=100, state='disabled',
                                                  text_color="white")
                logoBtn.place(x=140, y=12)

                LabelT = customtkinter.CTkLabel(new_root, text="Terms and Condition", font=("constantia", 24, 'bold'))
                LabelT.pack(padx=10, pady=20)

                with open("C:\\Users\\Velagasseth\\Desktop\\train test.txt", 'r') as file:
                    a = file.read()

                terms = customtkinter.CTkLabel(new_root, text=a, font=("constantia", 18, 'bold'))
                terms.pack(padx=10, pady=10)

                term_var = customtkinter.StringVar(value="off")
                terms_checkBox = customtkinter.CTkCheckBox(new_root, text="I agree with the terms and conditions!",
                                                           font=("Ink Free", 20, 'bold'),
                                                           fg_color="white",
                                                           hover_color="white", variable=term_var, onvalue="on",
                                                           command=my_terms)
                terms_checkBox.pack(padx=5, pady=10)

                submit = customtkinter.CTkButton(new_root, text="cancel", font=("constantia", 20, 'bold'), hover=False
                                                 , fg_color="transparent", cursor="hand2",
                                                 text_color="#2CB67D", width=50)
                submit.pack(padx=380, pady=20, anchor=tkinter.W)
                submit1 = customtkinter.CTkButton(new_root, text="next >", font=("constantia", 20, 'bold'), hover=False
                                                  , fg_color="transparent", cursor="hand2",
                                                  text_color="#2CB67D", width=50, )
                submit1.place(x=480, y=680)

                window.destroy()
                new_root.mainloop()




        else:
            check_error.configure(text="Login fail your a minor!!", text_color="red",
                                  font=("ink free", 20, 'bold'))
            entry1.configure(state="disabled")
            entry2.configure(state="disabled")
            submitBtn.configure(state="disabled")


submitBtn = customtkinter.CTkButton(frame, text="Sign in", font=("constantia", 20, 'bold'), width=250, command=push)
submitBtn.pack(padx=40, pady=10)

window.mainloop()
