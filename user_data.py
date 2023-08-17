"""This are built-in modules, which are part of the 
Python Standard Library"""
import json
import datetime
from tkinter import *


"""this are third-party modules that need to be installed 
separately using pip"""
import customtkinter
from CTkMessagebox import CTkMessagebox


"""This are local modules created by me and are 
part of my project"""
import database


class Userdata():
    """This class defines the data_editpage, that is use create the GUI"""

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    """Using context manager to open txt file for reading mode"""
    TEXT_FILE_PATH = "config/about.json"

    with open(file=TEXT_FILE_PATH, mode='r', encoding='utf-8') as rf:
        user_data = json.load(rf)

    def __init__(self) -> None:
        # self.data_edit = customtkinter.CTk()
        self.data_edit = customtkinter.CTkToplevel()
        self.data_edit.withdraw()
        self.data_edit.resizable(0, 0)
        self.data_edit.title('New Data')
        self.data_edit.minsize(900, 450)
        self.data_edit.geometry('720x450+265+130')
        self.data_edit.attributes('-topmost', True)
        self.data_edit.after(500, self.data_edit.deiconify)


        self.data_edit.columnconfigure(0, weight=1, uniform='a')
        self.data_edit.rowconfigure((1, 2), weight = 1, uniform='a')


        self.date = datetime.datetime.now().date()


        self.top_frame = customtkinter.CTkFrame(self.data_edit, border_width = 0.7,
                                                border_color ='gray20', 
                                                corner_radius=3,height=35)
        self.top_frame.grid(row = 0, column = 0, ipady=3, sticky = NSEW)
        self.top_frame.grid_columnconfigure((1, 2), weight = 1)


        top_frame_label = customtkinter.CTkLabel(master=self.top_frame, 
                                                text='Transaction ID =>', 
                                                font=('TImes', 22))
        top_frame_label.grid(row=0, column=0, padx=(18, 0), pady=(7, 0))


        self.data_idi = customtkinter.CTkEntry(master=self.top_frame, 
                                            placeholder_text=self.user_data
                                            ['entry_search'], state='disable',
                                            width=130, corner_radius=8)
        self.data_idi.grid(row=0, column=1, padx=(40, 0), pady=(6, 0))
        self.data_idi.focus()
        

        self.data_frame = customtkinter.CTkFrame(self.data_edit, width=400, 
                                                 height=500, corner_radius=5)
        self.data_frame.grid(row=1, column=0, padx=(10, 10), rowspan=4, pady=(10, 15), 
                        sticky=NSEW)
        self.data_frame.grid_columnconfigure((1, 2, 3, 4, 5, 6), weight=1, uniform='a')
        self.data_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform='a')


        self.item_sales = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                                 height=32, font=('Sans', 14),
                                                 placeholder_text='Item sold')
        self.item_sales.grid(row=0, column=1, padx=(10, 0), pady=(2, 2))


        self.quantity = customtkinter.CTkEntry(master=self.data_frame, width=320,
                                                height=32, font=('Sans', 14),
                                               placeholder_text='Quantity')
        self.quantity.grid(row=0, column=2, padx=(10, 0), pady=(2, 2))


        self.price = customtkinter.CTkEntry(master=self.data_frame,width=320,
                                            height=32, font=('Sans', 14),
                                            placeholder_text=' Price')
        self.price.grid(row=0, column=3, padx=(10, 0), pady=(2, 2))


        self.amount_paid = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                                  height=32, font=('Sans', 14),
                                                  placeholder_text='Amount paid')
        self.amount_paid.grid(row=0, column=4, padx=(10, 0), pady=(2, 2))


        self.balance_left = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                                   height=32, font=('Sans', 14),
                                                   placeholder_text='Balance',)
        self.balance_left.grid(row=1, column=1, padx=(10, 0), pady=(2, 2))


        self.served_by = customtkinter.CTkEntry(master=self.data_frame,width=320, 
                                                height=32, font=('Sans', 14),
                                                placeholder_text='Served By')
        self.served_by.grid(row=1, column=2, padx=(10, 0), pady=(2, 2))


        self.contact = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                              height=32, font=('Sans', 13),
                                              placeholder_text='Customer Contact')
        self.contact.grid(row=1, column=3, padx=(10, 0), pady=(2, 2))


        save_data_option = customtkinter.CTkFrame(master=self.data_frame, width=10, 
                                                  height=10, corner_radius=5)
        save_data_option.grid(row=0, column=6, padx=(1, 10), rowspan=3, 
                              columnspan=2, pady=(10, 15), sticky=NSEW)
        save_data_option.grid_columnconfigure((1), weight=1, uniform='a')
        save_data_option.grid_rowconfigure((0, 1, 2,), weight=1, uniform='a')
        

        data_save = customtkinter.CTkButton(master=save_data_option, text='Save Data',
                                              width=80, height=28, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.send_request)
        data_save.grid(row=0, column=1, padx=(0, 8), pady=(10, 0))


        data_cancel = customtkinter.CTkButton(master=save_data_option, text='Reset Entry',
                                              width=80, height=28, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.reset_entry)
        data_cancel.grid(row=1, column=1, padx=(0, 8), pady=(10, 0))


        data_cancel = customtkinter.CTkButton(master=save_data_option, text='Close',
                                              width=80, height=28, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.winclose)
        data_cancel.grid(row=2, column=1, padx=(0, 8), pady=(10, 0))


        # self.data_edit.mainloop()


    def reset_entry(self):
        """This function is use to reset the entry box"""
        self.item_sales.delete(0, 20)
        self.quantity.delete(0, 20)
        self.price.delete(0, 20)
        self.amount_paid.delete(0, 20)
        self.balance_left.delete(0, 20)
        self.served_by.delete(0, 20)
        self.contact.delete(0, 20)


    def send_request(self):
        """this method is get data from user entry"""
        try:
            its = str(self.item_sales.get()).upper()
            itq = int(self.quantity.get())
            itp = int(self.price.get())
            amt = int(self.amount_paid.get())
            bl = int(self.balance_left.get())
            svb = str(self.served_by.get()).upper()
            ct = int(self.contact.get())
            dt = str(self.date)
    
            if (its and itq and itp and amt and bl and svb and ct and dt != ""):
                try:
                    database.insert_daily_sales(its, itq, itp, amt, bl, svb, ct, dt)
                    CTkMessagebox(title='Successful',
                                    message='Data saved successfuly',
                                    icon='check', option_1='Ok')
                except:
                    CTkMessagebox(title='Error',
                                message="Can't add data to the database\
                                    Please contact system admin",
                                icon='cancel', option_1='Ok')
            else:
                CTkMessagebox(title='Warning',
                            message="Empty field is not allowed!",
                            option_1='Try again', icon='warning')
        except ValueError:
            CTkMessagebox(title='Error',
                          message="Please enter a valid number",
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
#     app = Userdata()