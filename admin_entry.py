"""This are built-in modules, which are part of the Python 
Standard Library"""
import json
import datetime
from tkinter import *


"""this are third-party modules that need to be installed 
separately using pip"""
import customtkinter
from CTkMessagebox import CTkMessagebox


"""This are local modules created by me and are part of my project"""
import database


class NewEntry():
    """This class defines the data_editpage, that is use create the GUI"""

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    """Using context manager to open txt file for reading mode"""
    TEXT_FILE_PATH = "config/about.json"

    with open(file=TEXT_FILE_PATH, mode='r', encoding='utf-8') as rf:
        user_data = json.load(rf)

    def __init__(self, master=None) -> None:
        # self.data_edit = customtkinter.CTk()
        self.data_edit = customtkinter.CTkToplevel()
        self.data_edit.withdraw()
        self.data_edit.title('New Data')
        self.data_edit.minsize(800, 300)
        self.data_edit.resizable(0, 0)
        self.data_edit.geometry('720x450+285+170')
        self.data_edit.attributes('-topmost', True)
        self.data_edit.after(500, self.data_edit.deiconify)


        self.data_edit.columnconfigure(0, weight=1, uniform='a')
        self.data_edit.rowconfigure((1, 2), weight = 1, uniform='a')


        self.date = datetime.datetime.now().date()


        self.top_frame = customtkinter.CTkFrame(self.data_edit, 
                                            border_width = 0.7, 
                                            border_color ='gray20',
                                            corner_radius = 3, height=35)
        self.top_frame.grid(row = 0, column = 0, ipady=3, sticky = NSEW)
        self.top_frame.grid_columnconfigure((1, 2), weight = 1)


        self.data_frame = customtkinter.CTkFrame(self.data_edit, width=400, 
                                                 height=500, corner_radius=5)
        self.data_frame.grid(row=1, column=0, padx=(10, 10), rowspan=4, pady=(10, 15), 
                        sticky=NSEW)
        self.data_frame.grid_columnconfigure((1, 2, 3, 4, 5, 6), weight=1, uniform='a')
        self.data_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform='a')


        self.daily_sls = customtkinter.CTkEntry(master=self.data_frame, width=360,
                                                height=32, placeholder_text='Sales',
                                                font=('Sans', 14))
        self.daily_sls.grid(row=0, column=1, padx=(10, 0), pady=(2, 2))


        self.daily_exp = customtkinter.CTkEntry(master=self.data_frame, width=320,
                                                height=32, placeholder_text='Expenses',
                                                font=('Sans', 14))
        self.daily_exp.grid(row=0, column=2, padx=(10, 0), pady=(2, 2))


        self.option1 = customtkinter.CTkEntry(master=self.data_frame,
                                              width=320, height=32,
                                              placeholder_text='Item',
                                              font=('Sans', 14))
        self.option1.grid(row=1, column=1, padx=(10, 0), pady=(2, 2))


        self.option2 = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                              height=32, placeholder_text='Price',
                                              font=('Sans', 14))
        self.option2.grid(row=1, column=2, padx=(10, 0), pady=(2, 2))


        self.option3 = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                              height=32, placeholder_text='Item',
                                              font=('Sans', 14))
        self.option3.grid(row=2, column=1, padx=(10, 0), pady=(2, 2))


        self.option4 = customtkinter.CTkEntry(master=self.data_frame, width=320,
                                              height=32, placeholder_text='Price',
                                              font=('Sans', 14))
        self.option4.grid(row=2, column=2, padx=(10, 0), pady=(2, 2))


        self.option5 = customtkinter.CTkEntry(master=self.data_frame, width=320,
                                              height=32, placeholder_text='Item',
                                              font=('Sans', 14))
        self.option5.grid(row=3, column=1, padx=(10, 0), pady=(2, 2))


        self.option6 = customtkinter.CTkEntry(master=self.data_frame, width=320,
                                              height=32, placeholder_text='Price',
                                              font=('Sans', 14))
        self.option6.grid(row=3, column=2, padx=(10, 0), pady=(2, 2))


        self.option7 = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                              height=32, placeholder_text='Item',
                                              font=('Sans', 13))
        self.option7.grid(row=4, column=1, padx=(10, 0), pady=(2, 2))


        self.option8 = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                              height=32, placeholder_text='Price',
                                              font=('Sans', 14))
        self.option8.grid(row=4, column=2, padx=(10, 0), pady=(2, 2))


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
        self.daily_sls.delete(0, 20)
        self.daily_exp.delete(0, 20)
        self.option1.delete(0, 20)
        self.option2.delete(0, 20)
        self.option3.delete(0, 20)
        self.option4.delete(0, 20)
        self.option5.delete(0, 20)
        self.option6.delete(0, 20)
        self.option7.delete(0, 20)
        self.option8.delete(0, 20)


    def send_request(self):
        try:
            dails = int(self.daily_sls.get())
            dailyex = int(self.daily_exp.get())
            opt1 = str(self.option1.get()).upper()
            opt2 = int(self.option2.get())
            opt3 = str(self.option3.get()).upper()
            opt4 = int(self.option4.get())
            opt5 = str(self.option5.get()).upper()
            opt6 = int(self.option6.get())
            dt = str(self.date)

            if (dails and dailyex and opt1 and opt2 and opt3 and opt4 
                and opt5 and opt6 and dt != ""):
                try:
                    database.get_data_admin(dails, dailyex, opt1, opt2, opt3, opt4, 
                                                opt5, opt6, dt)
                    CTkMessagebox(title='Successful', message='Data saved successfuly',
                                  icon='check', option_1='Ok')
                except:
                    CTkMessagebox(title='Error', message="Can't add data to the database\
                                  there is a problem",
                                  icon='cancel', option_1='Ok')
            else:
                CTkMessagebox(title='Warning', message="Empty field is not allowed!",
                              option_1='Try again', icon='warning')
        except ValueError as e:
            CTkMessagebox(title='Error', message=f"Please enter a valid number {str(e)}",
                          icon='cancel', option_1='Ok')


    """This method exit the data_edit window when the button is press"""
    def winclose(self) -> None:
        msg = CTkMessagebox(title='Close window', message='Do you want to exit?\
                            Remember to save your data', 
                            option_1='Yes', option_2='No')
        if msg.get() == 'Yes':
            self.data_edit.destroy()
        else:
            return self.data_edit



# if __name__ == "__main__":
#     app = NewEntry()