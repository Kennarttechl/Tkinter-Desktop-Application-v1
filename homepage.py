"""This are built-in modules, which are part of the Python 
Standard Library"""
import sys
import json
import sqlite3
import hashlib
from tkinter import *


"""this are third-party modules that need to be installed 
separately using pip"""
import customtkinter
from CTkMessagebox import CTkMessagebox


"""This are local modules that I have created myself and are 
part of the project."""
import about
from database import resource_path
from dashboard import Dashboard
from image_utils import get_ctk_image
from admin_dashboard import Adminsuper 
from forget_password import Passwordreset


class Homepage(customtkinter.CTk):
    """This class defines the homepage, that is use create the GUI"""

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme("green")

    """Using contex manager to load json file that is use the home page"""
    Text = 'config/settings.json'

    with open(file=Text, mode='r', encoding='utf-8') as rf:
        text = json.load(rf)
    

    def __init__(self, master) -> None:
        self.master = master
        self.master.columnconfigure(0, weight = 1, uniform='a')
        self.master.rowconfigure((1,2), weight = 1, uniform='a')
  

        top_frame = customtkinter.CTkFrame(self.master, border_width = 0.6,
                                           border_color ='gray10', height = 60,
                                           fg_color='#06283D', corner_radius = 3)
        top_frame.grid(row = 0, column = 0, ipady=(4), sticky = NSEW)
        top_frame.grid_columnconfigure((0,1,2,3,4), weight = 1)


        self.home_button1 = customtkinter.CTkButton(top_frame, text='Home', height=28, 
                                                font=('Roboto', 13), width=80, 
                                                hover_color=("gray70", "gray30"),
                                                corner_radius=5, 
                                                image=get_ctk_image(icon='logo_07', size=17), 
                                                fg_color="transparent", compound='left',
                                                text_color=("gray10", "gray90"),
                                                border_color='gray40',border_width=1)
        self.home_button1.grid(row=0, column=0, padx=(20, 10), pady=(8, 0), sticky=W)


        daily_record_button = customtkinter.CTkButton(top_frame, text='About', 
                                                font=('Roboto', 13), width=80, 
                                                height=28, hover_color=("gray70", "gray30"),
                                                corner_radius=5,fg_color="transparent", 
                                                text_color=("gray10", "gray90"),
                                                border_color='gray40',border_width=1,
                                                command=self.about_page)
        daily_record_button.grid(row=0, column=2, padx=(0, 35), pady=(8, 0), sticky=N)


        login_button = customtkinter.CTkButton(top_frame, text='Check for update', 
                                            font=customtkinter.CTkFont('Ubuntu-Medium', 13), 
                                            corner_radius=5,
                                            width=80, hover_color=("gray70", "gray30"),
                                            fg_color="transparent", height=28, 
                                            text_color=("gray10", "gray90"),
                                            border_color='gray40',border_width=1,
                                            hover=True, command=self.appupdate)
        login_button.grid(row=0, column=4, padx=(0, 22), pady=(8, 0), sticky=E)


        self.middle_frame = customtkinter.CTkFrame(self.master, border_width=0.6,
                                              border_color='gray10', corner_radius=8)
        self.middle_frame.grid(row=1, rowspan=2, columnspan=1, padx=(40, 40), 
                               pady=(20, 0), sticky='nsew')
        self.middle_frame.grid_columnconfigure((0,1,2), weight=1)
        self.middle_frame.grid_rowconfigure((1,2,3,4,5), weight=1)

        
        lock_image = customtkinter.CTkLabel(master=self.middle_frame, text="", 
                                            image=get_ctk_image(icon='user', size=75))
        lock_image.grid(row=0, column=1, padx=(0, 0), pady=(20, 0), sticky='s')


        title_lable = customtkinter.CTkLabel(master=self.middle_frame,
                                             text='Login into your account',
                                             font=customtkinter.CTkFont('Sans', 18))
        title_lable.grid(row=1, column=1, padx=(0, 0), pady=(0, 320), sticky=S)


        self.user_name = customtkinter.CTkEntry(master=self.middle_frame, width=220,
                                                height=32, font=('Sans', 14),
                                                placeholder_text='Enter your username')
        self.user_name.grid(row=1, column=1, padx=(0, 0), pady=(0, 260), sticky=S)
        self.user_name.focus()


        self.user_pass = customtkinter.CTkEntry(master=self.middle_frame, width=220, 
                                                height=32, show='****', font=('Sans', 14),
                                                placeholder_text='Enter your password')
        self.user_pass.grid(row=1, column=1, padx=(0, 0), pady=(0, 195), sticky=S)


        forgot_password = customtkinter.CTkButton(master=self.middle_frame, 
                                                  text='Forgot password', width=83,
                                                  height=20,corner_radius=5,
                                                  font=customtkinter.CTkFont('Sans', 15),
                                                  hover_color=('gray70', 'gray30'),
                                                  fg_color='transparent',
                                                  border_color='gray40',
                                                  command=self.resetpassword)
        forgot_password.grid(row=1, column=1, padx=(0, 0), pady=(0, 30), sticky=S)


        login_btn = customtkinter.CTkButton(master=self.middle_frame, text='Login', 
                                            width=220, height=32,corner_radius=5,
                                            font=customtkinter.CTkFont('Sans', 13),
                                            hover_color=('#3CCF4E'),fg_color='transparent',
                                            border_color='gray40', border_width=0.6,
                                            command=self.masterlog)
        login_btn.grid(row=1, column=1, padx=(0, 0), pady=(0, 135), sticky=S)


        alternative_btn = customtkinter.CTkButton(master=self.middle_frame, 
                                                  text='Login With Google Mail', 
                                                  width=220, height=32,corner_radius=5, 
                                                  image=get_ctk_image(icon='Google', size=17),
                                                  font=customtkinter.CTkFont('Sans', 13),
                                                  hover_color=('#3CCF4E'), 
                                                  compound='left', border_width=0.6, 
                                                  fg_color=('gray7', 'gray30'),
                                                  border_color='gray40',
                                                  command=self.notavailable)
        alternative_btn.grid(row=1, column=1, padx=(0, 0), pady=(0, 75), sticky=S)


        buttom_frame = customtkinter.CTkFrame(self.master, border_width=0.6,
                                              border_color='gray10', fg_color='#06283D', 
                                              corner_radius=5, height=10)
        buttom_frame.grid(row=4, column=0, padx=(0, 0), pady=(15,0), sticky='nsew')
        buttom_frame.grid_columnconfigure((0,1,2), weight=1)


        welcome_label = customtkinter.CTkLabel(master=buttom_frame,
                                               text=self.text['footer'],
                                               font=('Sans', 15),)
        welcome_label.grid(row=0, column=1, padx=5, pady=5)
        

    def resetpassword(self):
        Passwordreset()


    def masterlog(self):
        username = self.user_name.get()
        password = self.user_pass.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if username == '' or password == '':
            CTkMessagebox(title='Error', 
                        message='Empty field is not allowed', 
                        icon='warning', option_1='Ok')  
            return

        connection = sqlite3.connect(resource_path('data__/register.db'))
        conn = connection.cursor()
        conn.execute("SELECT * FROM ds_register WHERE username=? AND password=?", 
                    (username, hashed_password))
        result = conn.fetchone()

        # Check if the logged in user is an admin
        conn.execute("SELECT * FROM ds_register WHERE username=? AND user_role=?", 
                    (username, 'Admin'))
        is_admin = conn.fetchone() is not None
        connection.close()

        if result is not None:
            if is_admin:
                Adminsuper()
                self.master.withdraw()
                CTkMessagebox(title='Success', 
                              message=f'Welcome.. {username}',
                            icon='check', option_1='Ok')
            else:
                Dashboard()
                self.master.withdraw()
                CTkMessagebox(title='Success', 
                              message=f'Welcome.. {username}', 
                              icon='check', option_1='Ok')
        else:
            CTkMessagebox(title='Error', message='Invalid username or password', 
                        icon='cancel', option_1='Ok')


    def notavailable(self):
        CTkMessagebox(title='Unavailable', 
                      message='Sorry this option is not available yet',
                      icon='info', option_1='Close')


    def appupdate(self)-> None:
        CTkMessagebox(title='Unavailable', message='Sorry your app is up to date\n'
                      'No update is available yet',
                      icon='info', option_1='Close')

        
    def about_page(self)-> None:
        about.Aboutpage()


def main():
    """this function define the attribute of the GUI and also create the the GUI"""
    home = customtkinter.CTk()
    Homepage(home)
    home.title('Home Page')
    home.minsize(600, 600)
    home.geometry('500x500')
    home.iconbitmap('icons/logo.ico')
    if sys.platform.startswith("win"):
        home.after(1, lambda: home.state("zoomed"))
    else:
        CTkMessagebox(title='Platform', 
                      message='Platform not supported!! for windows',
                      icon='warning')
    home.mainloop()



if __name__ == "__main__":
    app = main()
    # print(Homepage.__doc__)

