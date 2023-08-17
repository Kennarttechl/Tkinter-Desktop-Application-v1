"""This are built-in modules, which are part of the 
Python Standard Library"""
import sqlite3
import hashlib
from tkinter import *


"""this are third-party modules that need to be installed 
separately using pip"""
import customtkinter
from CTkMessagebox import CTkMessagebox


"""The are local modules that I have created myself and 
are part of the project. """
from database import resource_path
from image_utils import get_ctk_image


class Passwordreset():
    """This class is responsible for password reset"""

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    def __init__(self):
        # self.password_reset = customtkinter.CTk()
        self.password_reset = customtkinter.CTkToplevel()
        self.password_reset.title('Password Reset')
        self.password_reset.resizable(0, 0)
        self.password_reset.iconbitmap('icons/logo.ico')
        self.password_reset.geometry('420x460+460+140')
        self.password_reset.attributes('-topmost', True)
        self.password_reset.withdraw()
        self.password_reset.after(500, self.password_reset.deiconify)


        self.password_reset.columnconfigure(0, weight=1, uniform='a')
        self.password_reset.rowconfigure(1, weight=0, uniform='a')


        frame = customtkinter.CTkFrame(self.password_reset, width=350, 
                                       height=500, corner_radius=10,
                                       border_color='gray50')
        frame.pack(pady=60, anchor='center')
        frame.grid_columnconfigure((0,1,2), weight=0)
        frame.grid_rowconfigure((0,1,2), weight=1)


        title_lable = customtkinter.CTkLabel(frame, text='Reset password',
                                            font=customtkinter.CTkFont('Sans', 20))
        title_lable.place(x=100, y=10)


        self.user_name = customtkinter.CTkEntry(frame, width=220, height=32,
                                            placeholder_text='Enter username',
                                            font=('Sans', 14))
        self.user_name.place(x=58, y=60)
        self.user_name.focus()

        
        self.new_pass = customtkinter.CTkEntry(frame, width=220, height=32,
                                            placeholder_text='Enter new password',
                                            show='....', font=('Sans', 14))
        self.new_pass.place(x=58, y=120)


        self.comfirm_pass = customtkinter.CTkEntry(frame, width=220, height=32,
                                            placeholder_text='Comfirm_password',
                                            show='....', font=('Sans', 14))
        self.comfirm_pass.place(x=58, y=180)


        login_btn = customtkinter.CTkButton(frame, text='Reset password', width=220, 
                                                height=32,corner_radius=5,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('#3CCF4E'),
                                                fg_color='transparent',
                                                border_color='gray40', border_width=0.6,
                                                command=self.generate_new_password)
        login_btn.place(x=58, y=240)


        alternative_btn = customtkinter.CTkButton(frame, text='Reset password using Google', 
                                                  width=220, height=32,corner_radius=5,image=get_ctk_image(icon='Google', 
                                                  size=17), border_width=0.6,
                                                  font=customtkinter.CTkFont('Sans', 12),
                                                  hover_color=('#3CCF4E'), compound='left',
                                                  fg_color=('gray7', 'gray30'),
                                                  border_color='gray40',
                                                  command=self.google_login)
        alternative_btn.place(x=58, y=298)

        # self.password_reset.mainloop()


    def google_login(self):
        CTkMessagebox(title='Unavailable', 
                      message='Sorry this option is not available yet', 
                      icon='info', option_1='Close')


    def generate_new_password(self):
        username = self.user_name.get()
        new_password = self.new_pass.get()
        confirm_password = self.comfirm_pass.get()

        if not username or not new_password or not confirm_password:
            CTkMessagebox(title='Error', message='Empty field is not allowed',
                        icon='warning', option_1='Ok')
            return

        connection = sqlite3.connect(resource_path('data__/register.db'))
        conn = connection.cursor()
        conn.execute("SELECT * FROM ds_register WHERE username=?", (username,))
        result = conn.fetchone()

        if result is None:
            CTkMessagebox(title='Error', message='Username not found!!',
                        icon='cancel', option_1='Ok')
            return

        if new_password != confirm_password:
            CTkMessagebox(title='Error', message="New password and confirm\
                            password don't match", icon='cancel', option_1='Ok')
            return

        new_hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
        conn.execute("UPDATE ds_register SET password=? WHERE username=?", 
                    (new_hashed_password, username))
        connection.commit()
        connection.close()
        CTkMessagebox(title='Success', message='Password reset successfully',
                    icon='check', option_1='Ok')



# if __name__ == "__main__":
#     app = Passwordreset()
