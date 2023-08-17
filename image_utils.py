import os
import sys
import customtkinter
from PIL import Image as PILImage


# set resources path for cx_Freeze
try:
    if hasattr(sys, '_MEIPASS'):
        """If the script is running in a cx_freeze bundle (i.e. a compiled executable)"""
        RESOURCES_PATH = os.path.join(sys._MEIPASS)
    else:
        """Otherwise, use the current working directory (i.e. the project directory)"""
        RESOURCES_PATH = os.path.join(os.path.abspath("."))
except Exception as e:
    print("Error occurred while setting resources path: ", e)



def get_ctk_image(icon=None, image_path=None, size=32):
    try:
        if icon:
            """if icon is given, use the corresponding icon image from the resources folder"""
            image_path = os.path.join(RESOURCES_PATH, 'icons', f'{icon}.png')
        return customtkinter.CTkImage(PILImage.open(image_path), size=(size, size))
        """create a CTkImage object from the image located at the given path and 
        resize it to the specified size"""
    except FileNotFoundError as e:
        print('File not found:', e)
    except Exception as e:
        print('Error occurred while getting CTkImage:', e)

