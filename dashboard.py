"""This are built-in modules, which are part of the 
Python Standard Library"""
import sys
import json
import sqlite3
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import Menu


"""this are third-party modules that need to be installed 
separately using pip"""
import customtkinter
from CTkMessagebox import CTkMessagebox


"""These are local modules that I have created myself and are 
part of the project. """
import newframes
from user_data import Userdata
from database import resource_path
from result_table import ResultTable
from image_utils import get_ctk_image


class Dashboard():

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    """Using context manager to open the a json file"""
    with open(file='config/settings.json', mode='r') as _rf:
        user_data = json.load(_rf)

    def __init__(self) -> None:
        # self.dash = customtkinter.CTk()
        self.dash = customtkinter.CTkToplevel()
        self.dash.minsize(1110, 600)
        self.dash.geometry('1000x600+135+30')
        self.dash.title('Welcome to DS Enterprise')
        self.dash.protocol("WM_DELETE_WINDOW", self.on_close)

        if sys.platform.startswith("win"):
            self.dash.after(1, lambda: self.dash.state("zoomed"))
        else:
            CTkMessagebox(title='Platform', 
                          message='Platform not supported for windows',
                          icon='warning')
  
  
        self.dash.columnconfigure((1,2), weight=1, uniform='a')
        self.dash.rowconfigure(0, weight=1, uniform='a')


        self.date = datetime.datetime.now().date()


        self.menu = Menu(self.dash)
        self.dash.config(menu = self.menu)
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
                                     accelerator='Ctrl+I', command=self.get_data)
        

        left_frame = customtkinter.CTkFrame(master=self.dash, border_color='gray25', 
                                            border_width=0.8, corner_radius=5)
                                            #fg_color='#06283D',
        left_frame.grid(row=0, column=0, ipadx=(10), pady=(0,0), sticky=NSEW)
        left_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)


        user_profile = customtkinter.CTkLabel(master=left_frame, text='', 
                                              image=get_ctk_image(icon='logo_12',size=90),
                                              text_color='gray12')
        user_profile.grid(row=0, column=0, padx=20, pady=1, sticky=NSEW)

        
        status_label = customtkinter.CTkLabel(master=left_frame, text='Welcome,\n[00121]',
                                              font=customtkinter.CTkFont('Roboto', 18),
                                              text_color='#16FF00')
        status_label.grid(row=1, column=0, padx=30, ipady=2, sticky=EW)     


        new_frame_button = customtkinter.CTkButton(master=left_frame, text='New Frames',
                                                   text_color=("gray10", "gray90"), fg_color='transparent',
                                                   hover_color=("gray70", "gray30"), 
                                                   height=25, width=30, anchor='w',
                                                   corner_radius=5, border_width=1,
                                                   image=get_ctk_image(icon='logo_10',size=30), 
                                                   command=self.new_frame_dashbord)
        new_frame_button.grid(row=2, column=0, padx=10, pady=2, sticky=EW)


        daily_sales_button = customtkinter.CTkButton(master=left_frame, text='Daily Sales',
                                                   text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"), 
                                                   height=25, width=30, border_width=1,fg_color='transparent',
                                                   corner_radius=5, anchor='w',
                                                   image=get_ctk_image(icon='logo_14', size=30), command=self.nothing)
        daily_sales_button.grid(row=3, column=0, padx=10, pady=0, sticky=EW)


        self.switch_theme = customtkinter.CTkSwitch(master=left_frame,
                                                text="Change theme",
                                                command=self.change_mode)
        self.switch_theme.grid(row=5, padx=50, pady=(0, 30), sticky="s")


        """This column downwards defines top, middle and down frames"""
        self.menu_frame = customtkinter.CTkFrame(master=self.dash, border_width=0.6,
                                           border_color='gray25', #fg_color='#06283D',
                                           corner_radius=5, width=1200, height=40)
        self.menu_frame.grid(row=0, column=1, columnspan=2, padx=(20,20), pady=(0, 12), sticky=N)
        self.menu_frame.grid_columnconfigure((0,1,2,3), weight=1)
        

        middle_frame = customtkinter.CTkFrame(master=self.dash, border_width=0.6,
                                           border_color='gray10', fg_color='#2C3333',
                                           corner_radius=5, width=1200, height=100)
        middle_frame.grid(row=0, column=1, columnspan=2, padx=(20,20), pady=(60, 60), sticky=NSEW)
        middle_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        middle_frame.grid_rowconfigure((1,2, 3, 4, 5, 6, 7, 8), weight=1)


        """----------------------Columns and Table-------------------------"""
        self.style = ttk.Style(master=self.dash)
        self.style.theme_use('clam')


        self.style.configure('Treeview', background="gray28", foreground='white', 
                             rowheight=30, fieldbackground="#292929")
        

        self.style.map('Treeview', background=[('selected', '#347083')])
        

        self.tree = ttk.Treeview(master=middle_frame,
                                 columns=("col1", "col2", "col3"), 
                                 show='headings')
        

        self.tree['columns'] = ('item sold', 'quantity', 'price', 'amount', 
                                'balance', 'served by', 'contact','date')
        
        # self.tree.heading('rowid', text='Rowid')
        self.tree.heading('item sold', text='Item Sold')
        self.tree.heading('quantity', text='Quantity')
        self.tree.heading('price', text='Price')
        self.tree.heading('amount', text='Amount')
        self.tree.heading('balance', text='Balance')
        self.tree.heading('served by', text='Served By')
        self.tree.heading('contact', text='Contact')
        self.tree.heading('date', text='Date')

        # self.tree.column("rowid", width=200)
        self.tree.column("item sold", width=100, anchor='center')
        self.tree.column("quantity", width=100, anchor='center')
        self.tree.column("price", width=100, anchor='center')
        self.tree.column("amount", width=100, anchor='center')
        self.tree.column("balance", width=100, anchor='center')
        self.tree.column("served by", width=100, anchor='center')
        self.tree.column("contact", width=100, anchor='center')
        self.tree.column("date", width=100, anchor='center')
        self.tree.bind("<ButtonRelease-1>", self.get_cursor)
        self.show_all_record()


        self.vsb = customtkinter.CTkScrollbar(master=middle_frame,
                                            #button_hover_color='#FF0303', 
                                            orientation='vertical',
                                            command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        # self.vsb.pack(side='right', fill='y')
        # self.vsb.grid(row=1, column=4, sticky=N+S)


        self.hsb = customtkinter.CTkScrollbar(master=middle_frame,
                                            #   button_hover_color='#FF0303', 
                                              orientation='horizontal', 
                                              command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.hsb.set)
        self.hsb.grid(row=9, columnspan=6, column=0, sticky=E+W)
        # self.hsb.pack(side='bottom', fill='x')


        self.tree.grid(row=1, column=0, rowspan=8, columnspan=6, sticky='nsew')
        # self.tree.pack(expand=True, fill='both')
        """----------------------Columns and Table-------------------------"""

        
        top_frame = customtkinter.CTkFrame(master=middle_frame, border_color='gray50', 
                                           border_width=1, width=400, height=40,
                                           corner_radius=3) #fg_color='gray28')
        top_frame.grid(row=0, column=0, columnspan=6, padx=(2,2), pady=(0, 0), 
                       ipady=3, sticky='ew')
        top_frame.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)


        data_entry = customtkinter.CTkButton(master=top_frame, text='Daily Sales',
                                              width=80, height=26, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.mydata)
        data_entry.grid(row=0, column=0, padx=(0, 0), pady=(3, 0))


        quantity_entry = customtkinter.CTkButton(master=top_frame, text='Refresh table',
                                                 width=80, height=26, corner_radius=4,
                                                 hover_color=('gray70', 'gray30'),
                                                 command=None)
        quantity_entry.grid(row=0, column=1, padx=(0, 0), pady=(3, 0))


        buttom_frame = customtkinter.CTkFrame(master=self.dash, border_width=0.6,
                                              border_color='gray25', #fg_color='#06283D',
                                              corner_radius=4, width=1200, height=25)
        buttom_frame.grid(row=0, column=1, columnspan=5, pady=(0, 0), sticky=S)
        buttom_frame.grid_columnconfigure((0,1,2,3), weight=1)
        """End of the frames"""


        menu_frame_label = customtkinter.CTkLabel(master=self.menu_frame, 
                                                  text='Daily Sales',
                                                  text_color='#16FF00', 
                                                  font=('Sans', 15),)
        menu_frame_label.place(x=40, y=20, anchor='w')


        self.search_box = customtkinter.CTkEntry(master=self.menu_frame, 
                                            placeholder_text='Item name....',
                                            width=220, corner_radius=9)
        self.search_box.place(x=560, y=20, anchor='e')

        
        self.search_button = customtkinter.CTkButton(master=self.menu_frame, text='Search',
                                                width=30, height=27, corner_radius=8,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('gray70', 'gray30'),
                                                fg_color='gray15', 
                                                image=get_ctk_image(icon='logo_08', size=22),
                                                compound='left', command=self.data_search,
                                                border_color='gray40',border_width=1,)
        self.search_button.place(x=660, y=20, anchor='e')


        self.dash.bind('<Control-i>', self.get_data)
        self.dash.bind('<Control-I>', self.get_data)

        # self.dash.mainloop()
        #Note value formating = "${0:.2f}".format(value)


    def mydata(self):
        Userdata()


    def get_data(self, *args):
        ResultTable()


    def on_close(self):
        msg = CTkMessagebox(title='Exit', message='Are you sure you want to exit',
                            option_1='Yes', option_2='No')
        if msg.get() == 'Yes':
            sys.exit()
        else:
            return


    def show_all_record(self) -> None:
        connection = sqlite3.connect(resource_path('data__/daily_database.db'))
        conn = connection.cursor()
        conn.execute("SELECT * FROM data_collection")
        rows = conn.fetchall()
        if len(rows) != 0:
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert('', END, values=row)
                connection.commit()
        connection.close()


    def data_search(self):
        try:
            value = self.search_box.get().lower()
            connection = sqlite3.connect(resource_path("data__/daily_database.db"))
            conn = connection.cursor()
            conn.execute("SELECT * FROM data_collection WHERE item_sales LIKE ?",
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
        finally:
            connection.close()


    def nothing(self):
        if CTkMessagebox(title='Dashboard', message='Option not available yet',
                         icon='info'):
            return self.dash


    def get_cursor(self, event):
        cursor_row = self.tree.focus()
        contents = self.tree.item(cursor_row)
        row = contents['values']


    def change_mode(self):
        pass
        # if self.switch_theme.get() == False:
        #     customtkinter.set_appearance_mode('dark')
        # else:
        #     customtkinter.set_appearance_mode('light')


    def new_frame_dashbord(self):
        msg = CTkMessagebox(title="Logout", 
                            message="Do you want to switch to New-Record?",
                            icon="info", option_1="Yes", option_2="No")
        response = msg.get()
        if response == 'Yes':
            newframes.Newframe()
            self.dash.destroy()
        else:
            self.dash = self.dash



# if __name__ == "__main__":
#     app = Dashboard()
    
    