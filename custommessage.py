"""This are built-in modules, which are part of the Python 
Standard Library"""
import sys
import json
from tkinter import *


"""this are third-party modules that need to be installed 
separately using pip"""
import customtkinter 


class Message(customtkinter.CTkFrame):
    """This class defines the Popupmessage, that is use create the GUI"""

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    """Using contex manager to load json file"""
    with open(file='config/settings.json', mode='r', encoding='utf-8') as rf:
        user_message = json.load(rf)

    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master


        self.message = customtkinter.CTkFrame(self, border_width=2, bg_color='gray25',
                                              border_color='gray40', corner_radius=15)
        self.message.grid(row=0, columnspan=4)
        self.message.grid_columnconfigure(2)


        self.yes_button = customtkinter.CTkButton(self.message, text='Yes', 
                                                  width=100, command=self.close)
        self.yes_button.grid(row=1, column=1, pady=10, padx=20)


        self.no_button = customtkinter.CTkButton(self.message, text='No', 
                                                 width=100, command=self.destroy)
        self.no_button.grid(row=1, column=0, pady=10, padx=20)

        self.grid(row=0, column=0, rowspan=3, columnspan=3)


    def close(self):
        self.destroy()
        self.master.destroy()
        sys.exit()


class CKTMessagebox(Message):
    """This class inherit from Message class (base class), which is use to msg popup"""

    def __init__(self, master) -> str:
        super().__init__(master)

        self.main_label = customtkinter.CTkLabel(self.message, width=200,
                                                 text=self.user_message['usermessage'],
                                                 text_color=self.user_message['message_text_color'],
                                                 compound='left', font=('Sans', 15))
        self.main_label.grid(row=0, column=0, columnspan=2, padx=(20, 20), pady=20)





