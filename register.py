"""This are built-in modules, which are part of the 
Python Standard Library"""
import os
import hashlib
from tkinter import *


"""this are third-party modules that need to be 
installed separately using pip"""
import customtkinter
from PIL import Image


"""The are local modules that I have created myself 
and are part of the project."""
import database
from image_utils import get_ctk_image
from CTkMessagebox import CTkMessagebox


class UserSignup():
    """This class returns the register or registration 
    page whenever it is been called"""

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    def __init__(self):
        # self.register = customtkinter.CTk()
        self.register = customtkinter.CTkToplevel()
        self.register.title('Signup')
        self.register.resizable(0, 0)
        self.register.geometry('500x500+400+100')
        self.register.attributes('-topmost', True)
        self.register.withdraw()
        self.register.after(500, self.register.deiconify)

        self.register.columnconfigure(0, weight=1, uniform='a')
        self.register.rowconfigure(1, weight=0, uniform='a')


        self.frame = customtkinter.CTkFrame(master=self.register, width=320, 
                                            height=400, corner_radius=10, 
                                            border_color='gray50')
        self.frame.pack(pady=60, anchor='center')
        self.frame.grid_columnconfigure((0,1,2), weight=0)
        self.frame.grid_rowconfigure((0,1,2), weight=1)


        title_lable = customtkinter.CTkLabel(master=self.frame, text='Create new account',
                                             font=customtkinter.CTkFont('Sans', 20))
        title_lable.place(x=60, y=20)

        
        self.user_name = customtkinter.CTkEntry(master=self.frame, width=220, height=32,
                                                placeholder_text='Enter username',
                                                font=('Sans', 14))
        self.user_name.place(x=53, y=60)
        self.user_name.focus()


        self.user_password = customtkinter.CTkEntry(master=self.frame, width=220, height=32,
                                                    placeholder_text='Enter password',
                                                    show='....', font=('Sans', 14))
        self.user_password.place(x=53, y=118)


        self.comfirm_password = customtkinter.CTkEntry(master=self.frame, width=220, 
                                                       height=32,
                                                       placeholder_text='Comfirm password', show='....', font=('Sans', 14))
        self.comfirm_password.place(x=53, y=175)


        self.user_role = customtkinter.CTkComboBox(master=self.frame, width=218,
                                                   values=['Admin', 'User'],
                                                   corner_radius=7, border_width=2, border_color='gray50', height=30,button_color='gray50', fg_color='gray25',button_hover_color=('gray70', 'gray30'), dropdown_fg_color='gray35', justify='left')
        self.user_role.place(x=54, y=230)
        self.user_role.set('Select role')


        self.register_btn = customtkinter.CTkButton(master=self.frame,
                                                    text='register', width=220,
                                                    height=32,corner_radius=5,font=customtkinter.CTkFont('Sans', 13),hover_color=('#3CCF4E'),fg_color='transparent',border_color='gray40',border_width=0.6, command=self.create_new_user)
        self.register_btn.place(x=54, y=285)


        self.alternative_btn = customtkinter.CTkButton(master=self.frame,
                                                       width=220, border_width=0.6,
                                                       height=30,corner_radius=5, image=get_ctk_image(icon='Google', size=17), compound='left',font=customtkinter.CTkFont('Sans', 13),hover_color=('#3CCF4E'),
                                                       fg_color=('gray7', 'gray30'),text='Register using google',border_color='gray40',
                                                       command=self.google_login)
        self.alternative_btn.place(x=54, y=340)

        # self.register.mainloop()
    

    def create_new_user(self):
        username = self.user_name.get()
        password = self.user_password.get()
        comfirmp = self.comfirm_password.get()
        role = self.user_role.get()
        if (username and password and comfirmp != ""):
            if password == comfirmp:
                # Hash the password using SHA-256 algorithm
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                hashed_comfirm = hashlib.sha256(comfirmp.encode()).hexdigest()
                try:
                    database.create_new_user(username, hashed_password, hashed_comfirm, role)
                    CTkMessagebox(title='Successful', message='Account created successfully',
                                  icon='check', option_1='Ok')
                except:
                    CTkMessagebox(title='Error', message="Can't add data to the database",
                                  icon='cancel', option_1='Ok')
            else:
                CTkMessagebox(title='Error', message='Password does not match',
                              icon='cancel', option_1='Ok')
        else:
            CTkMessagebox(title='Warning', message="Empty field is not allowed!",
                          option_1='Try again', icon='warning' )
    

    def google_login(self):
        CTkMessagebox(title='Not Available', message='This option is not available yet', 
                      option_1='Ok', icon='info')



# if __name__ == "__main__":
#     app = UserSignup()
