from tkinter import *
import customtkinter
from customtkinter import*
from time import*



customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
root=customtkinter.CTk()
root.geometry('800x300')
root.title('Velagasseth')
root.resizable(False, False)

def submit():
    username=name.get()
    username1=username[0].upper()
    if (username[0].lower()):
        username = username.capitalize()


    pin=number.get()
    if(username ==''):
        name.configure(placeholder_text='*enter your name!',border_color='red',placeholder_text_color='red')
    elif(pin==''):
        number.configure(placeholder_text='*enter your pin!',border_color='red',placeholder_text_color='red')
    else:
        new_root=customtkinter.CTk()
        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme('blue')
        new_root = customtkinter.CTk()
        new_root.geometry('800x700')
        new_root.title('Velagasseth')
        root.resizable(False, False)

        welcomeL1 = customtkinter.CTkLabel(new_root,text='Welcome '+username+ ' 👋',font=('constantia', 30, 'bold'), )
        welcomeL1.place(x=120, y=20)
        logo=customtkinter.CTkButton(new_root,height=50,width=50,corner_radius=100,state='disabled',fg_color='green',
                                     font=('constantia', 30, 'bold'),)
        logo.place(x=25, y=10)
        logo.configure(text=f'{username1}')

        statusL=customtkinter.CTkLabel(new_root, text='Status:',font=('constantia',25))
        statusL.place(x=25, y=120)


        status=['Married','Single']

        def check_status(values):
            if (values=='Married'):
                label3.configure(text='tax exempted 👍!')

                rate_per_day = customtkinter.CTkEntry(new_root, font=('constantia', 20),
                                                      placeholder_text='rate_per_day', width=250,state=DISABLED)
                rate_per_day.place(x=25, y=280)
                rate_per_hour = customtkinter.CTkEntry(new_root, font=('constantia', 20),
                                                       placeholder_text='rate_per_hour', width=250,
                                                       state=DISABLED)
                rate_per_hour.place(x=25, y=320)
                no_of_hours = customtkinter.CTkEntry(new_root, font=('constantia', 20), placeholder_text='no_of_hours',
                                                     width=250,state=DISABLED)
                no_of_hours.place(x=25, y=360)

            elif(values=='Single'):
                label3.configure(text='*fill the inforamtion to proceed!')
                rate_per_day = customtkinter.CTkEntry(new_root, font=('constantia', 20),
                                                      placeholder_text='rate_per_day', width=250)
                rate_per_day.place(x=25, y=280)
                rate_per_hour = customtkinter.CTkEntry(new_root, font=('constantia', 20),
                                                       placeholder_text='rate_per_hour', width=250,
                                                       )
                rate_per_hour.place(x=25, y=320)
                no_of_hours = customtkinter.CTkEntry(new_root, font=('constantia', 20), placeholder_text='no_of_hours',
                                                     width=250)
                no_of_hours.place(x=25, y=360)
                display = customtkinter.CTkLabel(new_root, font=('constantia', 20), text='')
                display.place(x=25, y=350)

                submitBtn=customtkinter.CTkButton(new_root,text='Submit')
                submitBtn.place(x=25, y=450)



        my_combo=customtkinter.CTkComboBox(new_root, values=status,
                                           font=('constantia',20),dropdown_font=('constantia',20),
                                          dropdown_hover_color='blue',
                                          command=check_status)
        my_combo.place(x=25, y=180)
        label3 = customtkinter.CTkLabel(new_root, text='', font=('constantia', 25),width=300)
        label3.place(x=25, y=240)

        root.destroy()
        new_root.mainloop()



#root.iconbitmap('')
welcomeL=customtkinter.CTkLabel(root, text='Velagasseth',font=('Ink free',30, 'bold'),)
welcomeL.place(x=25, y=10)
name=customtkinter.CTkEntry(root,font=('constantia',20), placeholder_text='Employee Name' ,width=250)
name.place(x=25, y=65)
number=customtkinter.CTkEntry(root,font=('constantia',20), placeholder_text='Employee Number' ,width=250)
number.place(x=25, y=120)
submit=customtkinter.CTkButton(root,text='submit',font=('Ink free',20,'bold'),command=submit)
submit.place(x=25,y=180)


text=customtkinter.CTkLabel(root,font=('ink free',23,'bold'), text='Trustworthy plattform with' ,width=200,
                            text_color='green')
text.place(x=290, y=65)

text=customtkinter.CTkLabel(root,font=('Ink free',25 ,'bold'), text='desirable policy.' ,width=200,text_color='green')
text.place(x=300, y=110)

root.mainloop()









