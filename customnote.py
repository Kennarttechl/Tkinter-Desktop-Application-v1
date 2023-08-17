"""This are built-in modules, which are part of the 
Python standard Library"""
from tkinter import * 


"""This are third-party modules that need to be installed 
separately using pip"""
import customtkinter
from CTkMessagebox import CTkMessagebox


"""This are modules created by me and are part of the code"""
import database


class BaseCustomNote(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        self.topframe = customtkinter.CTkFrame(self, width=600, height=40,
                                               corner_radius=15, border_width=4)
        self.topframe.grid(row=0, column=0)
        self.topframe.grid_columnconfigure((1), weight=1, uniform='a')
        self.topframe.grid_rowconfigure((1), weight=1, uniform='a')

        self.grid(row=0, column=0, pady=70, rowspan=2, columnspan=4)


class CustomNote(BaseCustomNote):
    def __init__(self, master):
        super().__init__(master)

        customtkinter.set_appearance_mode('dark')
        default = customtkinter.set_default_color_theme('green')

        self.noteid = customtkinter.CTkEntry(self.topframe, width=100, 
                                                height=35, font=(('Sans'), 16),
                                                placeholder_text='Note ID',
                                                corner_radius=10, state='disable')
        self.noteid.grid(row=0, column=0, padx=(0,320), pady=(5, 0))


        self.notetitle = customtkinter.CTkEntry(self.topframe, width=200, 
                                                height=35, font=(('Sans'), 16),
                                                placeholder_text='Note title',
                                                corner_radius=10)
        self.notetitle.grid(row=0, column=0, padx=(0,0), pady=(5, 0))
        self.notetitle.focus()


        self.notecontent = customtkinter.CTkTextbox(self.topframe, width=450, 
                                               height=320, corner_radius=10,
                                               border_width=1, font=(('Sans'), 17),
                                               scrollbar_button_hover_color='#FF0303')
        self.notecontent.grid(row=1, column=0, padx=(15, 22), pady=(20, 15))
        # self.notecontent.focus()


        self.close_btn = customtkinter.CTkButton(self.topframe, text='Save Data',
                                              fg_color=default, height=28,
                                              corner_radius=8, command=self.requestt)
        self.close_btn.grid(row=1, column=1, padx=(0, 15), pady=(0, 120))


        self.button = customtkinter.CTkButton(self.topframe, text='Close',
                                              fg_color=default, height=28,
                                              corner_radius=8, command=self.syclos)
        self.button.grid(row=1, column=1, padx=(0, 15), pady=(10, 10))


        self.entry_reset = customtkinter.CTkButton(self.topframe, text='Reset Entry',
                                              fg_color=default, height=28,
                                              corner_radius=8, command=self.entyreset)
        self.entry_reset.grid(row=1, column=1, padx=(0, 15), pady=(130, 10))


    def entyreset(self):
        # self.noteid.delete(0, 120)
        self.notetitle.delete(0, 30)
        self.notecontent.delete("0.0", "end")


    def requestt(self):
        try:
            # ntid = int(self.noteid.get())
            ntt = str(self.notetitle.get()).upper()
            ntc = str(self.notecontent.get("0.0", "end")).upper()
            if (ntt and ntc != ""):
                try:
                    database.admin_note(ntt, ntc)
                    CTkMessagebox(title='Successful', message='Data saved successfuly',
                                  icon='check', option_1='Ok')
                except:
                    CTkMessagebox(title='Error', message="Can't add data to the database\
                                    there is a problem",
                                    icon='cancel', option_1='Ok')
            else:
                CTkMessagebox(title='Warning', message="Empty field is not allowed!",
                            option_1='Try again', icon='warning' )
        except ValueError:
            CTkMessagebox(title='Error', message="Please enter a valid number",
                          icon='cancel', option_1='Ok')
            

    def syclos(self):
        msg = CTkMessagebox(title='Close Notebook', message='Do you want to exit\n'
                          'Remember to Save your data', icon='info', option_1='Yes', option_2='No')
        if msg.get() == 'Yes':
            self.destroy()
        else:
            return self.master
        








