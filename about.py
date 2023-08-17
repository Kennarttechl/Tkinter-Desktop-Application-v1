"""This are built-in modules, which are part of the 
Python Standard Library"""
import json
from tkinter import *


"""this are third-party modules that need to be installed 
separately using pip"""
import customtkinter


class Aboutpage():
    """This class defines the aboutpage, that is use create the GUI"""
    customtkinter.set_appearance_mode('dark')


    """Using contex manager to open txt file for reading mode"""
    with open(file="config/about.json", mode='r', encoding='utf-8') as rf:
        app_about = json.load(rf)


    def __init__(self) -> None:
        # self.about = customtkinter.CTk()
        self.about = customtkinter.CTkToplevel()
        self.about.withdraw()
        self.about.title('About Page')
        self.about.geometry('620x450+360+120')
        self.about.iconbitmap('icons/logo.ico')
        self.about.attributes('-topmost', True)
        self.about.after(500, self.about.deiconify)
      

        self.about.columnconfigure(0, weight = 1, uniform='a')
        self.about.columnconfigure(1, weight = 0)
        self.about.rowconfigure(1, weight = 1)


        default_textbox = customtkinter.CTkTextbox(self.about, width=200, font=('Times', 20),
                                                    text_color=('gray80'), corner_radius=10,
                                                    scrollbar_button_hover_color=('#16FF00'))
        default_textbox.grid(row=1, column=0, padx=(30, 30), pady=(30, 25), sticky="nsew")
        default_textbox.insert(0.0, 'About the application\n*---------------------*'+ '\n\n' + 
                               self.app_about['app_description']['appname'])
        default_textbox.configure(state='disable')


        footer_frame = customtkinter.CTkFrame(self.about, border_width = 0.6, 
                                            border_color ='gray10',fg_color='gray25', 
                                            corner_radius = 3,)
        footer_frame.grid(row = 2, column = 0, ipady=1, sticky=EW)
        footer_frame.grid_columnconfigure((0,1,2), weight = 1)


        footer_text = customtkinter.CTkLabel(footer_frame,text=self.app_about
                                             ['statusbar']['KT'], font=customtkinter
                                             .CTkFont('Sans', 12))
        footer_text.grid(row=0, column=1, pady=2)


        # self.about.mainloop()


# if __name__ == "__main__":
#     app = Aboutpage()