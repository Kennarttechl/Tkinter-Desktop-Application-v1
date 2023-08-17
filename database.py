import os
import sys
import sqlite3


"""https://www.sqlite.or/datatype3.html"""

"""https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file"""


global _MEIPASS

def resource_path(relative_path):
    try: # If the script is running in a cx_freeze bundle (i.e. a compiled executable)
        base_path = sys, _MEIPASS
    except Exception:
        """Otherwise, use the current working directory (i.e. the project directory)"""
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
    """Join the base path with the relative path to get the absolute path to the resource"""


data_folder = resource_path('data__')
"""Define a variable to hold the path to the 'data__' folder"""
if not os.path.exists(data_folder): #Check if the 'data__' folder exists if not then create it
    os.makedirs(data_folder)
print(os.path.abspath(os.path.join(sys.executable, '.', 'data__')))
"""Print the absolute path to the 'data__' folder"""


try:
    try:
        """Signup database"""
        connection = sqlite3.connect(os.path.join(resource_path('data__'),'register.db'))
        conn = connection.cursor()
        conn.execute(""" CREATE TABLE IF NOT EXISTS ds_register(
            username TEXT,
            password TEXT,
            comfirm_password,
            user_role TEXT
            )""")
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print("Error creating 'register.db':", e)


    try:
        """Admin note database"""
        connection = sqlite3.connect(os.path.join(resource_path('data__'), 'ds_note.db'))
        conn = connection.cursor()
        conn.execute(""" CREATE TABLE IF NOT EXISTS admin_note(
            note_title TEXT not null,
            note_content TEXT not null
            )""")
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print("Error creating 'ds_note.db':", e)


    try:
        """Admin daily sales database"""
        connection = sqlite3.connect(os.path.join(resource_path('data__'), 'ds_admin.db'))
        conn = connection.cursor()
        conn.execute(""" CREATE TABLE IF NOT EXISTS adminsales(
            daily_sales INTEGER not null,
            daily_expenses INTEGER not null,
            item_bought1 TEXT not null,
            price2 INTEGER not null,
            item_bought TEXT not null,
            price4 INTEGER not null,
            item_bought5 TEXT not null,
            price6 INTEGER not null,
            date INTEGER not null
            )""")
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print("Error creating 'ds_admin.db':", e)


    try:
        """Daily sales database"""
        connection = sqlite3.connect(os.path.join(resource_path('data__'), 'daily_database.db'))
        conn = connection.cursor()
        conn.execute("""CREATE TABLE IF NOT EXISTS data_collection(
            item_sales TEXT not null,
            quantity INTEGER not null,
            price INTEGER not null,
            amount INTEGER not null,
            balance INTEGER not null,
            served_by TEXT not null,
            contact TEXT not null,
            date INTEGER not null
            )""")
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print("Error creating 'daily_database.db':", e)


    try:
        """New stock database"""
        connection = sqlite3.connect(os.path.join(resource_path('data__'), 'new_frame.db'))
        conn = connection.cursor()
        conn.execute("""CREATE TABLE IF NOT EXISTS ds_newframe(
            new_item TEXT not null,
            quantity INTEGER not null,
            price INTEGER not null,
            date INTEGER not null
            )""")
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print(f"Error creating 'new_frame.db': {str(e)}")

except Exception as e:
    print(f"Error connecting to database: {str(e)}")
else:
    print('Database created successfully!!')
# ------------------------End of Database creation--------------------------------


def create_new_user(username, password, comfirm_password, user_role):
    """This function add data into the register database"""
    connection = sqlite3.connect('data__/register.db')
    conn = connection.cursor()
    conn.execute("INSERT INTO 'ds_register' VALUES (?,?,?,?)",
                 (username, password, comfirm_password, user_role))
    connection.commit()
    connection.close()


def admin_note(note_title, note_content):
    """This function add admin note into the database"""
    connection = sqlite3.connect("data__/ds_note.db")
    conn = connection.cursor()
    conn.execute(" INSERT INTO 'admin_note' VALUES (?,?)",
                 (note_title, note_content))
    connection.commit()
    connection.close()


def get_data_admin(daily_sales, daily_expenses, item_bought1, price2,
                   item_bought3, price4, item_bought5, price6, date):
    """This function add admin_daily sales into the database"""
    connection = sqlite3.connect("data__/ds_admin.db")
    conn = connection.cursor()
    conn.execute(" INSERT INTO 'adminsales' VALUES (?,?,?,?,?,?,?,?,?)",
                 (daily_sales, daily_expenses, item_bought1, price2,
                  item_bought3, price4, item_bought5, price6, date))
    connection.commit()
    connection.close()


def insert_daily_sales(item_sales, quantity, price, amount, 
                        balance, served_by, contact, date):
    """This function add daily sales into the database"""
    connection = sqlite3.connect('data__/daily_database.db')
    conn = connection.cursor()
    conn.execute(" INSERT INTO 'data_collection' VALUES (?,?,?,?,?,?,?,?)",
                 (item_sales, quantity, price, amount, 
                  balance, served_by, contact, date))
    connection.commit()
    connection.close()


def new_stock(newitem, quantity, price, date):
    """This function also add new stock into the database"""
    connection = sqlite3.connect("data__/new_frame.db")
    conn = connection.cursor()
    conn.execute(" INSERT INTO 'ds_newframe' VALUES (?,?,?,?)",
                 (newitem, quantity, price, date))
    connection.commit()
    connection.close()


def fetch_data_populate(rowid):
    """This function is use to fetch, and populate data into update table"""
    connection = sqlite3.connect('data__/daily_database.db')
    conn = connection.cursor()
    conn.execute("SELECT * FROM 'data_collection' WHERE rowid=?", 
                 (rowid,))
    return conn.fetchall()


#================Requesting or fetching data from the database================
# try:
#     connection = sqlite3.connect('daily_database.db')
#     conn = connection.cursor()
#     conn.execute("""CREATE TABLE IF NOT EXISTS data_collection(
#         id INTEGER PRIMARY KEY,
#         item_sales TEXT not null,
#         quantity INTEGER not null,
#         price INTEGER not null,
#         amount INTEGER not null,
#         balance INTEGER not null,
#         served_by TEXT not null,
#         contact TEXT not null,
#         date INTEGER not null,
#         new_frame_id INTEGER,
#         FOREIGN KEY (new_frame_id) REFERENCES ds_newframe(id)
#         )""")
#     connection.commit()
#     connection.close()

#     # Create new stock database
#     connection = sqlite3.connect('new_frame.db')
#     conn = connection.cursor()
#     conn.execute("""CREATE TABLE IF NOT EXISTS ds_newframe(
#         id INTEGER PRIMARY KEY,
#         new_item TEXT not null,
#         quantity INTEGER not null,
#         price INTEGER not null,
#         date INTEGER not null
#         )""")
#     connection.commit()
#     connection.close()

#     # Insert a new stock item and link it to a daily sale
#     connection = sqlite3.connect('daily_database.db')
#     conn = connection.cursor()
#     conn.execute("INSERT INTO 'data_collection' VALUES (?,?,?,?,?,?,?,?,?,?)",
#                 (1, 'item 1', 2, 10, 20, 0, 'user1', '12345', 1647904000, 1))
#     connection.commit()
#     connection.close()

#     connection = sqlite3.connect('new_frame.db')
#     conn = connection.cursor()
#     conn.execute("INSERT INTO 'ds_newframe' VALUES (?,?,?,?,?)",
#                 (1, 'new item 1', 5, 15, 1647904000))
#     connection.commit()
#     connection.close()
# except ValueError:
#     pass



"""this code is use to update the database"""
# def new_update(self):
#     connection = sqlite3.connect('daily_database.db')
#     conn = connection.cursor()
#     itemid = self.search_box.get()
#     try:
#         conn.execute(""" UPDATE data_collection SET 
#                         item_sales = :item_sales,
#                         quantity = :quantity,
#                         price = :price,
#                         amount = :amount,
#                         balance = :balance,
#                         served_by = :served_by,
#                         contactf = :contact
#                         WHERE oid = :oid""",
#                         {'item_sales': self.itm.get(),
#                          'quantity': self.qtn.get(),
#                          "price": self.pri.get(),
#                          "amount": self.amt.get(),
#                          "balance": self.blc.get(),
#                          "served_by": self.srv.get(),
#                          "contact": self.cut.get(),
#                          "oid": itemid
#                         })
#         connection.commit()
#         CTkMessagebox(title='Saved', message='Data updated successfully', 
#                       option_1='OK', icon='check')
#     except sqlite3.Error as e:
#         connection.rollback()
#         CTkMessagebox(title='Error', 
#           message=f'Data update failed: {str(e)}', 
#           option_1='OK', icon='error')
#     finally:
#         connection.close()

