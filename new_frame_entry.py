"""This are built-in modules, which are part of the 
Python Standard Library"""
import json
import datetime
from tkinter import *


"""this are third-party modules that need to be 
installed separately using pip"""
import database
import customtkinter
from CTkMessagebox import CTkMessagebox


class Userdata2():
    """This class defines the data_editpage, that is use create the GUI"""

    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme('green')

    """Using context manager to open txt file for reading mode using json"""
    TEXT_FILE_PATH = "config/about.json"

    with open(file=TEXT_FILE_PATH, mode='r', encoding='utf-8') as rf:
        user_data = json.load(rf)

    def __init__(self) -> None:
        # self.data_edit = customtkinter.CTk()
        self.data_edit = customtkinter.CTkToplevel()
        self.data_edit.withdraw()
        self.data_edit.title('New Stock')
        self.data_edit.minsize(900, 450)
        self.data_edit.resizable(0, 0)
        self.data_edit.geometry('720x450+265+130')
        self.data_edit.attributes('-topmost', True)
        self.data_edit.after(500, self.data_edit.deiconify)


        self.data_edit.columnconfigure(0, weight=1, uniform='a')
        self.data_edit.rowconfigure((1, 2), weight = 1, uniform='a')


        self.date = datetime.datetime.now().date()


        self.top_frame = customtkinter.CTkFrame(master=self.data_edit, 
                                            border_width = 0.7, 
                                            border_color ='gray20',
                                            corner_radius = 3,
                                            height=35)
        self.top_frame.grid(row = 0, column = 0, ipady=3, sticky = NSEW)
        self.top_frame.grid_columnconfigure((1, 2), weight = 1)


        self.top_frame_label = customtkinter.CTkLabel(master=self.top_frame, 
                                                text='Transaction ID =>', 
                                                font=('TImes', 22))
        self.top_frame_label.grid(row=0, column=0, padx=(18, 0), pady=(7, 0))


        self.dataID = customtkinter.CTkEntry(master=self.top_frame, 
                                            placeholder_text=self.user_data
                                            ['entry_search'], state='disable',
                                            width=230, corner_radius=10)
        self.dataID.grid(row=0, column=1, padx=(40, 0), pady=(6, 0))
        self.dataID.focus()


        self.data_frame = customtkinter.CTkFrame(self.data_edit, width=400, height=500,
                                            corner_radius=5)
        self.data_frame.grid(row=1, column=0, padx=(10, 10), rowspan=4, pady=(10, 15), 
                        sticky=NSEW)
        self.data_frame.grid_columnconfigure((1, 2, 3, 4, 5, 6), weight=1, uniform='a')
        self.data_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform='a')


        self.newgoods = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                            placeholder_text='New stock',
                                            font=('Sans', 14), height=32,)
        self.newgoods.grid(row=0, column=1, padx=(10, 0), pady=(2, 2))


        self.quantity = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                          placeholder_text='Item quantity',
                                          font=('Sans', 14), height=32,)
        self.quantity.grid(row=0, column=2, padx=(10, 0), pady=(2, 2))


        self.price = customtkinter.CTkEntry(master=self.data_frame, width=320,
                                       placeholder_text='Price',
                                       font=('Sans', 14), height=32,)
        self.price.grid(row=0, column=3, padx=(10, 0), pady=(2, 2))


        self.save_data_option = customtkinter.CTkFrame(master=self.data_frame, 
                                                       width=10, 
                                                  height=10, corner_radius=5)
        self.save_data_option.grid(row=0, column=6, padx=(1, 10), rowspan=3, 
                              columnspan=2, pady=(10, 15), sticky=NSEW)
        self.save_data_option.grid_columnconfigure((1), weight=1, uniform='a')
        self.save_data_option.grid_rowconfigure((0, 1, 2,), weight=1, uniform='a')
        

        self.data_save = customtkinter.CTkButton(master=self.save_data_option, 
                                                 text='Save Data',
                                            width=80, height=28, corner_radius=4,
                                            hover_color=('gray70', 'gray30'),
                                            command=self.newstockk)
        self.data_save.grid(row=0, column=1, padx=(0, 8), pady=(10, 0))


        self.data_cancel = customtkinter.CTkButton(master=self.save_data_option, 
                                              width=80, height=28, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.entryreset, text='Reset Entry',)
        self.data_cancel.grid(row=1, column=1, padx=(0, 8), pady=(10, 0))


        self.data_cancel = customtkinter.CTkButton(master=self.save_data_option, 
                                                   text='Close',
                                              width=80, height=28, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.winclose)
        self.data_cancel.grid(row=2, column=1, padx=(0, 8), pady=(10, 0))


        # self.data_edit.mainloop()

    def entryreset(self):
        # self.dataID.delete(0, 20)
        self.newgoods.delete(0, 20)
        self.quantity.delete(0, 20)
        self.price.delete(0, 20)
        self.sysdate.delete(0, 20)


    def newstockk(self) -> None:
        try:
            # did = int(self.dataID.get())
            ngd = str(self.newgoods.get()).upper()
            qt = int(self.quantity.get())
            pr = int(self.price.get())
            syd = str(self.date)
            if (ngd and qt and pr and syd != ""):
                try:
                    database.new_stock(ngd, qt, pr, syd)
                    CTkMessagebox(title='Successful', message='Data saved successfuly',
                                    icon='check', option_1='Ok')
                except:
                    CTkMessagebox(title='Error', message="Can't add data to the database\
                                    ID already exist check the ID",
                                icon='cancel', option_1='Ok')
            else:
                CTkMessagebox(title='Warning', message="Empty field is not allowed!",
                            option_1='Try again', icon='warning' )
        except ValueError:
            CTkMessagebox(title='Error', message="Please enter a valid number",
                          icon='cancel', option_1='Ok')
        
    
    def winclose(self) -> None:
        """This method exit the data_edit window when the button is press"""
        msg = CTkMessagebox(title='Close window', message='Do you want to exit?\
                                Remember to save your data', 
                                option_1='Yes', option_2='No')
        if msg.get() == 'Yes':
            self.data_edit.destroy()
        else:
            return self.data_edit




# if __name__ == "__main__":
#     app = Userdata2()