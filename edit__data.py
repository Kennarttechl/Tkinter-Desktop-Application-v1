"""This are built-in modules, which are part of the 
Python Standard Library"""
import os
import json
import sqlite3
from tkinter import *


"""this are third-party modules that need to be installed 
separately using pip"""
import customtkinter
from CTkMessagebox import CTkMessagebox


"""this are modules i create my self which are part of the project"""
import database
from database import resource_path
from image_utils import get_ctk_image


class EditData():
    """This class defines the data_editpage that is use create the GUI"""

    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme('green')

    """Using contex manager to open txt file for reading mode"""
    TEXT_FILE_PATH = "config/about.json"

    with open(file=TEXT_FILE_PATH, mode='r', encoding='utf-8') as rf:
        user_data = json.load(rf)

    def __init__(self) -> None:
        super().__init__()
        # self.data_edit = customtkinter.CTk()
        self.data_edit = customtkinter.CTkToplevel()
        self.data_edit.withdraw()
        self.data_edit.title('Modify Data')
        self.data_edit.resizable(0, 0)
        self.data_edit.geometry('720x450+365+130')
        self.data_edit.attributes('-topmost', True)
        
        self.data_edit.after(800, self.data_edit.deiconify)


        self.data_edit.columnconfigure(0, weight=1, uniform='a')
        self.data_edit.rowconfigure((1, 2), weight = 1, uniform='a')


        top_frame = customtkinter.CTkFrame(self.data_edit, 
                                            border_width = 0.7, 
                                            border_color ='gray20',
                                            corner_radius = 3,
                                            height=35)
        top_frame.grid(row = 0, column = 0, ipady=3, sticky = NSEW)
        top_frame.grid_columnconfigure((1, 2, 3), weight = 1)


        top_frame_label = customtkinter.CTkLabel(master=top_frame, 
                                                text='Enter row ID =>', 
                                                font=('TImes', 22))
        top_frame_label.grid(row=0, column=0, padx=(18, 0), pady=(7, 0))


        self.search_box = customtkinter.CTkEntry(master=top_frame, 
                                            placeholder_text=self.user_data
                                            ['entry_search'],
                                            width=100, corner_radius=8)
        self.search_box.grid(row=0, column=1, padx=(100, 0), pady=(6, 0))
        self.search_box.focus()

        
        search_button = customtkinter.CTkButton(master=top_frame, text='Search',
                                                width=30, height=27, corner_radius=8,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('gray70', 'gray30'),
                                                fg_color='gray15', 
                                                image=get_ctk_image(icon='logo_08', size=22),
                                                compound='left', command=self.search_item_id,
                                                border_color='gray40',border_width=1,)
        search_button.grid(row=0, column=2, padx=(0, 200), pady=(6, 0))


        # tabview = customtkinter.CTkTabview(master=top_frame, width=220, height=10,
        #                                    corner_radius=8, fg_color=('gray20'))
        # tabview.grid(row=0, column=2, padx=(60, 0), pady=(6, 0))
        # tabview.add('tab1')
        # tabview.add('tab2')
        # tabview.set('tab1')


        self.data_frame = customtkinter.CTkFrame(self.data_edit, width=400, 
                                                 height=500, corner_radius=5)
        self.data_frame.grid(row=1, column=0, padx=(10, 10), rowspan=4, pady=(10, 15),
                             sticky=NSEW)
        self.data_frame.grid_columnconfigure((1, 2, 3, 4, 5, 6), weight=1, uniform='a')
        self.data_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform='a')


        self.itm = customtkinter.StringVar()
        self.item_sales = customtkinter.CTkEntry(master=self.data_frame, width=320,
                                                 height=32, textvariable=self.itm,placeholder_text='Item sold',
                                                 font=('Sans', 14))
        self.item_sales.grid(row=0, column=1, padx=(10, 0), pady=(2, 2))


        self.qtn = customtkinter.StringVar()
        self.quantity = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                               height=32, textvariable=self.qtn,
                                               placeholder_text='Quantity',
                                               font=('Sans', 14))
        self.quantity.grid(row=0, column=2, padx=(10, 0), pady=(2, 2))


        self.pri = customtkinter.StringVar()
        self.price = customtkinter.CTkEntry(master=self.data_frame, width=320,
                                            height=32, textvariable=self.pri, 
                                            placeholder_text=' Price',
                                            font=('Sans', 14))
        self.price.grid(row=0, column=3, padx=(10, 0), pady=(2, 2))


        self.amt = customtkinter.StringVar()
        self.amount_paid = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                                  height=32, textvariable=self.amt,
                                                  placeholder_text='Amount paid',
                                                  font=('Sans', 14))
        self.amount_paid.grid(row=0, column=4, padx=(10, 0), pady=(2, 2))


        self.blc = customtkinter.StringVar()
        self.balance_left = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                                   height=32, textvariable=self.blc,
                                                   placeholder_text='Balance',
                                                   font=('Sans', 14))
        self.balance_left.grid(row=1, column=1, padx=(10, 0), pady=(2, 2))


        self.srv = customtkinter.StringVar()
        self.served_by = customtkinter.CTkEntry(master=self.data_frame, width=320,
                                                height=32, textvariable=self.srv,
                                                placeholder_text='Served By',
                                                font=('Sans', 14))
        self.served_by.grid(row=1, column=2, padx=(10, 0), pady=(2, 2))


        self.cut = customtkinter.StringVar()
        self.contact = customtkinter.CTkEntry(master=self.data_frame, width=320, 
                                              height=32, textvariable=self.cut,
                                              placeholder_text='Customer Contact',
                                              font=('Sans', 13))
        self.contact.grid(row=1, column=3, padx=(10, 0), pady=(2, 2))


        self.data_modify = customtkinter.CTkButton(master=self.data_frame, width=90,
                                                   text='Close/Exit',
                                                   height=30, corner_radius=4,
                                                   hover_color=('gray70', 'gray30'),
                                                   command=self.close_win)
        self.data_modify.grid(row=6, column=5, padx=(0, 5), pady=(0, 0))


        self.data_modify = customtkinter.CTkButton(master=self.data_frame, text='Update',
                                                   width=90, height=30, corner_radius=4,
                                                   hover_color=('gray70', 'gray30'),
                                                   command=self.new_update)
        self.data_modify.grid(row=6, column=6, padx=(0, 20), pady=(0, 0))


        # self.data_edit.mainloop()


    def close_win(self):
        msg = CTkMessagebox(title='Exit', message='Do you want exit?\
                            Remember to save your update',
                            option_1='Yes', option_2='No')
        if msg.get() == 'Yes':
            self.data_edit.destroy()
        else:
            return


    def search_item_id(self):
        itemid = self.search_box.get().lower()
        item = database.fetch_data_populate(itemid)
        try:
            self.itm.set(item[0][0])
            self.qtn.set(item[0][1])
            self.pri.set(item[0][2])
            self.amt.set(item[0][3])
            self.blc.set(item[0][4])
            self.srv.set(item[0][5])
            self.cut.set(item[0][6])
        except IndexError as e:
            CTkMessagebox(title='Not found', 
                          message=f'Record ID not found please try again!  {str(e)}',
                          option_1='Ok', icon='warning')


    def new_update(self):
        connection = sqlite3.connect(resource_path('data__/daily_database.db'))
        conn = connection.cursor()
        itemid = self.search_box.get()
        try:
            conn.execute("""UPDATE data_collection SET item_sales = ?, 
                            quantity = ?, price = ?, amount = ?, balance = ?, 
                            served_by = ?, contact = ? WHERE oid = ?""",
                            (self.itm.get(), self.qtn.get(), self.pri.get(), 
                             self.amt.get(), self.blc.get(), self.srv.get(),
                             self.cut.get(), itemid ))
            connection.commit()
            CTkMessagebox(title='Saved', message='Data updated successfully', 
                          option_1='OK', icon='check')
        except sqlite3.Error as e:
            connection.rollback()
            CTkMessagebox(title='Error', message=f'Data update failed!:  {str(e)}', 
                          option_1='OK', icon='cancel')
        finally:
            connection.close()



# if __name__ == "__main__":
#     app = EditData()