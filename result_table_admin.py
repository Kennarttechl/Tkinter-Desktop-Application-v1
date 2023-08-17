"""This are built-in modules, which are part of the 
Python Standard Library"""
import os
import sqlite3
from tkinter import NSEW
from tkinter import END, ttk
from tkinter import LEFT, Menu  # import tkinter's Image class as TkImage
from PIL import Image as PILImage  # import PIL's Image module as PILImage


"""this are third-party modules that need to be installed 
separately using pip"""
import customtkinter
from image_utils import get_ctk_image
from CTkMessagebox import CTkMessagebox


class ResultTableA():

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')
    
    def __init__(self) -> None:
        # self.master_window = customtkinter.CTk()
        self.master_window = customtkinter.CTkToplevel()
        self.master_window.withdraw()
        self.master_window.title('Admin Data Table')
        self.master_window.geometry('1070x410+260+160')
        self.master_window.attributes('-topmost', True)
        self.master_window.after(500, self.master_window.deiconify)


        self.master_window.columnconfigure(0, weight=1, uniform='a')
        self.master_window.rowconfigure(1, weight=1, uniform='a')


        self.menu = Menu(self.master_window)
        self.master_window.config(menu = self.menu)
        self.filename = Menu(self.menu, tearoff=0, 
                             activebackground='gray20', activeforeground='white')
        self.menu.add_cascade(label='File', menu=self.filename)
        self.filename.add_command(label='Save Data      ', accelerator='Ctrl+S', 
                                  command=None)
        self.filename.add_separator()
        self.filename.add_command(label='Print Data     ', image=None, compound=LEFT, 
                                  accelerator='Ctrl+P', command=self.print_data)


        self.top_frame = customtkinter.CTkFrame(master=self.master_window, 
                                                fg_color='#2C3333', height=45, 
                                                corner_radius=2, bg_color='#2C3333')
        self.top_frame.grid(row=0, column=0, pady=(0, 0), ipady=3, sticky='nsew')
        self.top_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')


        self.close_button = customtkinter.CTkButton(master=self.top_frame, 
                                                    text='Exit tabel',width=90, 
                                                    height=25, corner_radius=4,
                                                    hover_color=('gray70', 'gray30'),
                                                    command=self.sysexit)
        self.close_button.grid(row=0, column=1, padx=(0, 110), pady=(9, 0))


        self.search_box = customtkinter.CTkEntry(master=self.top_frame, 
                                            placeholder_text='Item name.....',
                                            width=220, corner_radius=9)
        self.search_box.grid(row=0, column=2, padx=(0, 10), pady=(9, 0))

        
        self.search_button = customtkinter.CTkButton(master=self.top_frame,
                                                     text='Search',width=60,
                                                     height=27, corner_radius=8,
                                                     font=('Sans', 13),
                                                     hover_color=('gray70', 'gray30'),fg_color='gray15', compound='left', border_color='gray40',border_width=1, image=get_ctk_image(icon="logo_08", size=22),
                                                     command=self.data_search)
        self.search_button.grid(row=0, column=3, padx=(90, 0), pady=(9, 0))


        self.middle_frame = customtkinter.CTkFrame(master=self.master_window, 
                                                   fg_color='#20262E',)
        self.middle_frame.grid(row=1, column=0, rowspan=4, pady=(1, 1), sticky=NSEW)
        

        self.style = ttk.Style(master=self.master_window)
        self.style.theme_use('clam')


        self.style.configure('Treeview', background="gray28", foreground='white', 
                             rowheight=30, fieldbackground="#292929")
        

        self.style.map('Treeview', background=[('selected', '#347083')])


        self.tree = ttk.Treeview(master=self.middle_frame, 
                                 columns=("col1", "col2", "col3"),show='headings')
        

        self.tree['columns'] = ('daily sales', 'daily expenses', 'item', 
                                'price.,', 'item._.', 'price._',
                                 'item..', 'price__', 'date')
        
        # self.tree.heading("id", text='Id')
        self.tree.heading("daily sales", text='Daily Sales')
        self.tree.heading("daily expenses", text='Daily Expenses')
        self.tree.heading('item', text='Item')
        self.tree.heading('price.,', text='Price')
        self.tree.heading('item._.', text='Item')
        self.tree.heading('price._', text='Price')
        self.tree.heading('item..', text='Item')
        self.tree.heading('price__', text='Price')
        self.tree.heading("date", text='Date')

        # self.tree.column("id", width=400)
        self.tree.column("daily sales", width=100, anchor='center')
        self.tree.column("daily expenses", width=100, anchor='center')
        self.tree.column("item", width=200, anchor='center')
        self.tree.column("price.,", width=100, anchor='center')
        self.tree.column("item._.", width=200, anchor='center')
        self.tree.column("price._", width=100, anchor='center')
        self.tree.column("item..", width=200, anchor='center')
        self.tree.column("price__", width=100, anchor='center')
        self.tree.column("date", width=100, anchor='center')
        self.show_all_records()

            
        self.vsb = customtkinter.CTkScrollbar(master=self.middle_frame,
                                            #   button_hover_color='#FF0303', 
                                              orientation='vertical', 
                                              command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side='right', fill='y')


        self.hsb = customtkinter.CTkScrollbar(master=self.middle_frame,
                                            #   button_hover_color='#FF0303', 
                                              orientation='horizontal', 
                                              command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.hsb.set)
        self.hsb.pack(side='bottom', fill='x')

        self.tree.pack(expand=True, fill='both')


        self.master_window.bind('<Control-P>', self.print_data)
        self.master_window.bind('<Control-p>', self.print_data)

        # self.master_window.mainloop()


    def print_data(self, *event)-> None:
        pass


    def data_search(self):
        try:
            value = self.search_box.get().lower()
            connection = sqlite3.connect("data__/ds_admin.db")
            conn = connection.cursor()
            conn.execute("SELECT * FROM adminsales WHERE item_bought1 LIKE ?",
                         ('%'+value+'%',))
            rows = conn.fetchall()
            if len(rows) != 0:
                CTkMessagebox(title='Found', message='Record found',
                              icon='check', option_1='Ok')
                self.tree.delete(*self.tree.get_children())
                for row in rows:
                    self.tree.insert('', END, values=row)
                    connection.commit()
            else:
                CTkMessagebox(title='No Record', message='Record not found',
                          icon='warning', option_1='try again')
        except:
            CTkMessagebox(title='Error',
                          message='There was a problem with the\
                            Database!! Contact your system Admin',
                            icon='cancel', option_1='Try again')
        finally:
            connection.close()

            
    def show_all_records(self):
        try:
            connection = sqlite3.connect("data__/ds_admin.db")
            conn = connection.cursor()
            conn.execute(" SELECT * FROM adminsales")
            rows = conn.fetchall()
            if len(rows) != 0:
                self.tree.delete(*self.tree.get_children())
                for row in rows:
                    self.tree.insert("", END, values=row)
                    connection.commit()
        except sqlite3.Error as a:
            CTkMessagebox(title='Error',
                          message=f'There is a problem displaying the data {a}',
                          option_1='Ok', icon='cancel')
                

    def sysexit(self):
        msg = CTkMessagebox(title='Close Data Tabel', message='Save your data',
                          icon='info', option_1='Yes', option_2='No')
        if msg.get() == 'Yes':
            self.master_window.destroy()
        else:
            return self.master_window



# if __name__ == "__main__":
#     app = ResultTableA()
