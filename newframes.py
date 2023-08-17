"""This are built-in modules, which are part of the 
Python Standard Library"""
import os
import sys
import json
import sqlite3
import datetime
from tkinter import *


"""this are third-party modules that need to be installed 
separately using pip"""
import customtkinter
from PIL import Image
from tkinter import ttk
from CTkMessagebox import CTkMessagebox


"""The are local modules that I have created myself and 
are part of the project. """
import dashboard
from database import resource_path
from image_utils import get_ctk_image
from new_frame_entry import Userdata2
from result_table_stock import ResultTableF


class Newframe():
    """This class defines the Newframe page, that is use create the GUI"""

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    """Using context manager to open or load the a json file"""
    with open(file='config/settings.json', mode='r') as _rf:
        user_data = json.load(_rf)

    def __init__(self) -> None:
        # self.new_frame = customtkinter.CTk()
        self.new_frame = customtkinter.CTkToplevel()
        self.new_frame.minsize(1100, 595)
        self.new_frame.geometry('1000x600+155+50')
        self.new_frame.title('Welcome to DS Enterprise')
        self.new_frame.protocol("WM_DELETE_WINDOW", self.on_close)

        if sys.platform.startswith("win"):
            self.new_frame.after(1, lambda: self.new_frame.state("zoomed"))
        else:
            CTkMessagebox(title='Platform', message='Platform not supported for windows',
                      icon='warning')


        self.new_frame.columnconfigure((1,2), weight=1, uniform='a')
        self.new_frame.rowconfigure(0, weight=1, uniform='a')


        date = datetime.datetime.now().date()
        

        self.menu = Menu(self.new_frame)
        self.new_frame.config(menu = self.menu)
        self.filename = Menu(self.menu, tearoff=0, activebackground=self.user_data
                             ['menu_background_color'], activeforeground='white')
        self.menu.add_cascade(label='File', menu = self.filename)
        self.filename.add_command(label = 'Save', accelerator = 'Ctrl+S', command=None)
        self.filename.add_separator()


        self.option_menu = Menu(self.menu, tearoff=0, activebackground=self.user_data
                                ['menu_background_color'], activeforeground='white')
        self.menu.add_cascade(label = "Options", menu = self.option_menu)
        self.option_menu.add_command(label = 'Print', accelerator='Ctrl+P', command=None)
        self.option_menu.add_command(label = 'View All Data', 
                                     accelerator='Ctrl+I', command=self.view_data)


        left_frame = customtkinter.CTkFrame(master=self.new_frame, border_color='gray10',
                                            border_width=0.8, corner_radius=5,)
        left_frame.grid(row=0, column=0, ipadx=(10), pady=(0,0), sticky=NSEW)
        left_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)


        user_profile = customtkinter.CTkLabel(master=left_frame, 
                                              text='', text_color='gray12',
                                              image=get_ctk_image(icon='logo_12', size=90),
                                              font=customtkinter.CTkFont('Roboto', 18))
        user_profile.grid(row=0, column=0, padx=20, pady=1, sticky=NSEW)

        
        status_label = customtkinter.CTkLabel(master=left_frame, text='Welcome,\n[00121]',
                                              font=customtkinter.CTkFont('Roboto', 18),
                                              text_color='#16FF00')
        status_label.grid(row=1, column=0, padx=30, ipady=2, sticky=EW)     


        daily_sales_button = customtkinter.CTkButton(master=left_frame, text='Daily Sales',
                                                   text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"), 
                                                   height=25, width=30,fg_color='transparent',
                                                   corner_radius=5, border_width=1,
                                                   image=get_ctk_image(icon='logo_14', size=30), 
                                                   anchor='w', 
                                                   command=self.Dsales)
        daily_sales_button.grid(row=2, column=0, padx=10, pady=0, sticky=EW)


        self.switch_theme = customtkinter.CTkSwitch(master=left_frame,
                                                text="Change theme",
                                                command=self.change_mode)
        self.switch_theme.grid(row=5, padx=50, pady=(0, 30), sticky="s")


        """This column downwards defines top, middle and down frames"""
        self.menu_frame = customtkinter.CTkFrame(master=self.new_frame, border_width=0.6,
                                           border_color='gray25', #fg_color='gray28',
                                           corner_radius=2, width=1200, height=40)
        self.menu_frame.grid(row=0, column=1, columnspan=2, padx=(20,20), pady=(0, 12), sticky=N)
        self.menu_frame.grid_columnconfigure((0,1,2,3), weight=1)
        

        middle_frame = customtkinter.CTkFrame(master=self.new_frame, border_width=0.6,
                                           border_color='gray10', fg_color='gray28',
                                           corner_radius=5, width=1200, height=100)
        middle_frame.grid(row=0, column=1, columnspan=2, padx=(20,20), pady=(60, 60), sticky=NSEW)
        middle_frame.grid_columnconfigure((0,1,2,3,4), weight=1)
        middle_frame.grid_rowconfigure((1,2,3,4,5,6,7,8), weight=1)


        """----------------------Columns and Table-------------------------"""
        self.style = ttk.Style(master=self.new_frame)
        self.style.theme_use('clam')


        self.style.configure('Treeview', background="gray28",
                             foreground='white', rowheight=30,
                             fieldbackground="#292929")
        

        self.style.map('Treeview', background=[('selected', '#347083')])
        

        self.tree = ttk.Treeview(master=middle_frame, 
                                 columns=("col1", "col2", "col3"), 
                                 show='headings')
        

        self.tree['columns'] = ('new item', 'quantity', 'price', 'date')
        
        # self.tree.heading('id', text='Id')
        self.tree.heading('new item', text='Item Name')
        self.tree.heading('quantity', text='Quantity')
        self.tree.heading('price', text='Price')
        self.tree.heading('date', text='Date')

        # self.tree.column("id", width=200)
        self.tree.column("new item", width=200, anchor='center')
        self.tree.column("quantity", width=200, anchor='center')
        self.tree.column("price", width=200, anchor='center')
        self.tree.column("date", width=200, anchor='center')
        self.show_all_record2()


        self.vsb = customtkinter.CTkScrollbar(master=middle_frame,
                                              button_hover_color='#FF0303', 
                                              orientation='vertical', 
                                              command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        # self.vsb.pack(side='right', fill='y')
        # self.vsb.grid(row=1, column=4, sticky=N+S)

        self.hsb = customtkinter.CTkScrollbar(master=middle_frame,
                                              orientation='horizontal', 
                                              command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.hsb.set)
        self.hsb.grid(row=9, columnspan=6, column=0, sticky=E+W)
        # self.hsb.pack(side='bottom', fill='x')


        self.tree.grid(row=1, column=0, rowspan=8, columnspan=6, sticky='nsew')
        # self.tree.pack(expand=True, fill='both')
        # self.tree.grid(row=1, column=0, rowspan=7, columnspan=4, sticky='nsew')
        """----------------------Columns and Table-------------------------"""


        top_frame = customtkinter.CTkFrame(master=middle_frame, border_color='gray50', 
                                           border_width=1, width=400, height=40,
                                           fg_color='gray35', corner_radius=7)
        top_frame.grid(row=0, column=0, columnspan=6, padx=(2,2), pady=(0, 0), ipady=3, sticky='ew')
        top_frame.grid_columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)


        data_entry = customtkinter.CTkButton(master=top_frame, text='Enter Data',
                                              width=80, height=26, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.new_entry_data)
        data_entry.grid(row=0, column=0, padx=(0, 0), pady=(3, 0))
        

        quantity_ = customtkinter.CTkButton(master=top_frame, text='Refresh table',
                                              width=80, height=26, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=None)
        quantity_.grid(row=0, column=1, padx=(0, 0), pady=(3, 0))


        buttom_frame = customtkinter.CTkFrame(master=self.new_frame, border_width=0.6,
                                              border_color='gray25', #fg_color='gray24',
                                              corner_radius=4, width=1200, height=25)
        buttom_frame.grid(row=0, column=1, columnspan=5, pady=(0, 0), sticky=S)
        buttom_frame.grid_columnconfigure((0,1,2,3), weight=1)
        """End of the frames"""


        menu_frame_label = customtkinter.CTkLabel(master=self.menu_frame, 
                                                  text=self.user_data["Record"],
                                                  text_color='#16FF00', 
                                                  font=('Sans', 15))
        menu_frame_label.place(x=40, y=20, anchor='w')


        self.search_entry = customtkinter.CTkEntry(master=self.menu_frame, 
                                            placeholder_text='Item name....',
                                            width=220, corner_radius=9)
        self.search_entry.place(x=560, y=20, anchor='e')

        
        search_button = customtkinter.CTkButton(master=self.menu_frame, text='Search',
                                                width=30, height=27, corner_radius=8,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('gray70', 'gray30'),
                                                fg_color='gray15', 
                                                image=get_ctk_image(icon='logo_08', size=22),
                                                compound='left',border_color='gray40',
                                                border_width=1, command=self.data_search2)
        search_button.place(x=660, y=20, anchor='e')


        self.new_frame.bind('<Control-i>', self.view_data)
        self.new_frame.bind('<Control-I>', self.view_data)

        # self.new_frame.mainloop()

    
    def new_entry_data(self):
        Userdata2()
    

    def view_data(self, *args):
        ResultTableF()


    def fetch_data(self):
        pass
        # ResultTableF()
    

    def on_close(self):
        msg = CTkMessagebox(title='Exit', message='Are you sure you want to exit',
                            option_1='Yes', option_2='No')
        if msg.get() == 'Yes':
            sys.exit()
        else:
            return

    
    def show_all_record2(self) -> None:
        connection = sqlite3.connect(resource_path("data__/new_frame.db"))
        conn = connection.cursor()
        conn.execute(" SELECT * FROM ds_newframe")
        rows = conn.fetchall()
        if len(rows) != 0:
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert("", END, values=row)
                connection.commit()


    def data_search2(self):
        try:
            value = self.search_entry.get().lower()
            connection = sqlite3.connect(resource_path("data__/new_frame.db"))
            conn = connection.cursor()
            conn.execute("SELECT * FROM ds_newframe WHERE new_item LIKE ?",
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
             CTkMessagebox(title='Error', message='There was a problem with the\
                           Database!! Contact your system Admin',
                           icon='cancel', option_1='Try again')


    def change_mode(self):
        pass
        # if self.switch_theme.get() == False:
        #     customtkinter.set_appearance_mode('dark')
        # else:
        #     customtkinter.set_appearance_mode('light')


    def Dsales(self):
        msg = CTkMessagebox(title='Logout', 
                         message='Do you want to Switch to Daily Sales', 
                         icon='info', option_1='Yes', option_2='No')
        if msg.get() == 'Yes':
            dashboard.Dashboard()
            self.new_frame.destroy()
        else:
            self.new_frame = self.new_frame



# if __name__ == "__main__":
#     app = Newframe()
#     