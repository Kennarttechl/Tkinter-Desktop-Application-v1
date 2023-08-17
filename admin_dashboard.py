"""This are built-in modules, which are part of the Python 
Standard Library"""
import sys
import json
import datetime
from tkinter import *
from tkinter import Menu


"""this are third-party modules that need to be installed 
separately using pip"""
import customtkinter
# from tktooltip import ToolTip
from CTkMessagebox import CTkMessagebox


"""This are local modules that I have created myself and are 
part of the project."""
import about
import newframes
import dashboard
import customnote
from register import UserSignup
from edit__data import EditData
from admin_entry import NewEntry
from image_utils import get_ctk_image
from note_table_admin import NoteTable
from result_table_admin import ResultTableA


class Adminsuper():
    """This class defines the Admin page, which is use create the GUI"""

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    """Using context manager to open the a json file"""
    with open(file='config/settings.json', mode='r') as _rf:
        user_data = json.load(_rf)

    def __init__(self) -> None:
        # self.admin__a = customtkinter.CTk()
        self.admin__a = customtkinter.CTkToplevel()
        self.admin__a.minsize(1100, 530)
        self.admin__a.geometry('1000x515+125+60')
        self.admin__a.title('Welcome to DS Enterprise')
        self.admin__a.protocol("WM_DELETE_WINDOW", self.on_close)

        if sys.platform.startswith("win"):
            self.admin__a.after(1, lambda: self.admin__a.state("zoomed"))
        else:
            CTkMessagebox(title='Platform', message='Platform not supported for windows',
                      icon='warning')


        self.admin__a.columnconfigure((1,2), weight=1, uniform='a')
        self.admin__a.rowconfigure(0, weight=1, uniform='a')


        self.date = datetime.datetime.now().date()


        self.menu = Menu(self.admin__a)
        self.admin__a.config(menu = self.menu)
        self.filename = Menu(self.menu, tearoff=0, 
                             activebackground='gray20', activeforeground='white')
        self.menu.add_cascade(label='File', menu=self.filename)
        self.filename.add_command(label='Save       ', accelerator='Ctrl+S', command=None)

        self.help = Menu(self.menu, tearoff=0, activebackground='gray20',
                         activeforeground='white', activeborderwidth=0)
        self.menu.add_cascade(label='Help', menu = self.help)
        self.help.add_command(label='About      ', accelerator='Ctrl+A', 
                              command=self.about)

        self.option_menu = Menu(self.menu, tearoff=0, activebackground='gray20', 
                                activeforeground='white')
        self.menu.add_cascade(label='Options', menu = self.option_menu)
        self.option_menu.add_command(label='Print       ', 
                                     accelerator='Ctrl+P', command=None)
        self.option_menu.add_command(label='View All Data', 
                                     accelerator='Ctrl+I', command=self.get_data)
        self.option_menu.add_command(label='View Note Data', 
                                     accelerator='Ctrl+N', command=self.get_note_data)


        self.left_frame = customtkinter.CTkFrame(master=self.admin__a, border_color='gray25', 
                                            border_width=0.8, corner_radius=8)
                                            # fg_color=self.user_data['admin_color2'], 
        self.left_frame.grid(row=0, column=0, padx=(10,0), ipadx=(10), 
                             pady=(10, 20), sticky=NSEW)
        self.left_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)


        self.user_profile = customtkinter.CTkLabel(master=self.left_frame, text='',
                                              image=get_ctk_image(icon='logo_05', size=130),
                                              font=customtkinter.CTkFont('Roboto', 18),
                                              text_color='gray12')
        self.user_profile.grid(row=0, column=0, padx=20, pady=1, sticky=NSEW)


        self.new_frame_button = customtkinter.CTkButton(master=self.left_frame,
                                                        text='New Frames',
                                                        text_color=("gray10", "gray90"), fg_color='transparent',
                                                        hover_color=("gray70", "gray30"), height=25, width=30, anchor='w',corner_radius=6, border_width=1,
                                                        image=get_ctk_image(icon='logo_10', size=30),
                                                        command=self.gotonewf)
        self.new_frame_button.grid(row=2, column=0, padx=10, pady=2, sticky=EW)


        self.daily_sales_button = customtkinter.CTkButton(master=self.left_frame, 
                                                          height=25,text='User dashboard',text_color=("gray10", "gray90"),hover_color=("gray70", "gray30"), border_width=1, width=30,
                                                          fg_color='transparent',corner_radius=6, anchor='w', 
                                                          image=get_ctk_image(icon='logo_14', size=30), 
                                                          command=self.usrnothing)
        self.daily_sales_button.grid(row=3, column=0, padx=10, pady=0, sticky=EW)


        self.create_new_user = customtkinter.CTkButton(master=self.left_frame, height=25,  
                                                    text='Create New User',
                                                   text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"), 
                                                   border_width=1,fg_color='transparent',
                                                   corner_radius=6, anchor='w', width=30,
                                                   image=get_ctk_image(icon='logo_11', size=30), 
                                                   command=self.new_user)
        self.create_new_user.grid(row=4, column=0, padx=10, pady=0, sticky=EW)


        self.switch_theme = customtkinter.CTkSwitch(master=self.left_frame,
                                                    text="Change theme",
                                                    command=self.change_mode)
        self.switch_theme.grid(row=6, padx=50, pady=(0, 30), sticky="s")


        """This column downwards defines top, middle and down frames"""
        self.menu_frame = customtkinter.CTkFrame(master=self.admin__a, border_width=0.6,
                                                 border_color='gray25',
                                                 #fg_color=self.user_data['admin_color2'],
                                                 corner_radius=5, width=1200, height=40)
        self.menu_frame.grid(row=0, column=1, columnspan=2, padx=(19,19), 
                             pady=(10, 12), sticky=N)
        self.menu_frame.grid_columnconfigure((0,1,2,3), weight=1)


        self.middle_frame = customtkinter.CTkFrame(master=self.admin__a, border_width=1,
                                                   border_color='gray40',
                                                    # fg_color=self.customtkinter,
                                                   corner_radius=5, width=1200, height=100)
        self.middle_frame.grid(row=0, column=1, columnspan=2, padx=(20,20), 
                          pady=(57, 60), sticky=NSEW)
        self.middle_frame.grid_columnconfigure((0,1,2,3), weight=1)
        self.middle_frame.grid_rowconfigure((1,2,3,4,5,6,7,8), weight=1)

        
        self.top_frame = customtkinter.CTkFrame(master=self.middle_frame, corner_radius=3, 
                                                border_width=0.6, width=400, height=40,border_color='gray50')
                                                #fg_color=self.user_data['admin_color3'], 
        self.top_frame.grid(row=0, column=0, columnspan=4, padx=(2, 2), pady=(0, 0), 
                       ipady=3, sticky='ew')
        self.top_frame.grid_columnconfigure((0,1,2,3,4,5,6,7,8,10,12), weight=1)


        self.data_modify = customtkinter.CTkButton(master=self.top_frame,
                                                   text='Daily Sales',
                                                   width=80, height=26, corner_radius=4,hover_color=('gray70', 'gray30'),command=self.dataentry)
        self.data_modify.grid(row=0, column=3, padx=(0, 0), pady=(5, 0))


        self.txt_note = customtkinter.CTkButton(master=self.top_frame, width=100, 
                                           text='New Note',
                                            hover_color=('gray70', 'gray30'),
                                            font=('Sans', 13), height=26,
                                            corner_radius=4, command=self.adminnote)
        self.txt_note.grid(row=0, column=3, padx=(230,0), pady=(4,0))


        self.data_modify = customtkinter.CTkButton(master=self.top_frame, 
                                                   text='Modify Data',
                                              width=80, height=26, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.modify_dt)
        self.data_modify.grid(row=0, column=4, padx=(0, 220), pady=(3, 0))
        # ToolTip(self.data_modify, msg='Edit saved data', fg='white', bg='gray15', delay=0)


        self.print_data = customtkinter.CTkButton(master=self.middle_frame, 
                                                  text='Print Data',
                                                   text_color=("white"), 
                                                   fg_color=self.user_data['theme3'],
                                                   hover_color=("gray70", "gray30"), 
                                                   height=30, width=106, anchor='S',
                                                   corner_radius=4, border_width=1,
                                                   font=('Roboto', 16),command=None)
        self.print_data.grid(row=8, column=3, padx=(0, 130), pady=(0, 0), sticky='e')


        self.submit_button = customtkinter.CTkButton(master=self.middle_frame, 
                                                     text='Save Record',
                                                   text_color=("white"), 
                                                   fg_color=self.user_data['theme2'],
                                                   hover_color=("gray70", "gray30"), 
                                                   height=30, width=106, anchor='S',
                                                   corner_radius=4, border_width=1,
                                                   font=('Roboto', 16),command=self.datasave)
        self.submit_button.grid(row=8, column=3, padx=(30, 10), pady=(0, 0), sticky='e')


        self.buttom_frame = customtkinter.CTkFrame(master=self.admin__a, 
                                              border_width=0.6,
                                              border_color='gray10', 
                                              #fg_color=self.user_data['admin_color2'],
                                              corner_radius=4, width=1200, 
                                              height=30)
        self.buttom_frame.grid(row=0, column=1, columnspan=5, padx=(19, 19), pady=(0, 20), sticky=S)
        self.buttom_frame.grid_columnconfigure((0,1,2,3), weight=1)
        """End of the frames"""


        self.display_records = customtkinter.CTkLabel(master=self.buttom_frame, 
                                                 text="Today's date " + str(self.date), 
                                                 font=('Sans', 12),)
        self.display_records.place_configure(x=350, y=1)
        # self.display_records.grid(row=5, column=2, padx=(5, 0), pady=(2, 2))


        self.menu_frame_label = customtkinter.CTkLabel(master=self.menu_frame, 
                                                  text=self.user_data['master'],
                                                  text_color=self.user_data['admin_color'], 
                                                  font=('Sans', 15),)
        self.menu_frame_label.place(x=40, y=20, anchor='w')


        """This code takes tuple from a user as in 'Shortcut' to perform task"""
        self.admin__a.bind('<Control-a>', self.about)
        self.admin__a.bind('<Control-A>', self.about)
        self.admin__a.bind('<Control-i>', self.get_data)
        self.admin__a.bind('<Control-I>', self.get_data)
        self.admin__a.bind('<Control-N>', self.get_note_data)
        self.admin__a.bind('<Control-n>', self.get_note_data)


        # self.admin__a.mainloop()

    def get_note_data(self, *event):
        NoteTable()


    def dataentry(self):
        NewEntry()

    def datasave(self):
        pass
    
    def new_user(self):
        UserSignup()


    def get_data(self, *args):
        ResultTableA()

    
    def modify_dt(self):
        EditData()


    def about(self, *args):
        about.Aboutpage()


    def adminnote(self):
        customnote.CustomNote(self.admin__a)

    
    def change_mode(self):
        pass
        # if self.switch_theme.get() == False:
        #     customtkinter.set_appearance_mode('dark')
        # else:
        #     customtkinter.set_appearance_mode('light')

    def on_close(self):
        msg = CTkMessagebox(title='Exit Window', message='Are you sure you want to exit',
                            option_1='Yes', option_2='No')
        if msg.get() == 'Yes':
            sys.exit()
        else:
            return


    def gotonewf(self):
        msg = CTkMessagebox(title='New frame', message='Switch to New Frame\n'
                            'Do you want to proceed', option_1='Yes',
                            option_2='No', icon='info')
        if msg.get() == 'Yes':
            newframes.Newframe()
            self.admin__a.destroy()
        else:
            self.admin__a = self.admin__a


    def usrnothing(self):
        msg = CTkMessagebox(title='User Record', message='Switch to User dashboard\n'
                            'Remember to save your work', option_1='Yes', 
                            option_2='No', icon='info')
        if msg.get() == 'Yes':
            dashboard.Dashboard()
            self.admin__a.destroy()
        else:
            self.admin__a = self.admin__a



# if __name__ == "__main__":
#     app = Adminsuper()

