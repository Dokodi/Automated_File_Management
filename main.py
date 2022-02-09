from tkinter import *
from tkinter import font
from tkinter import Tk, filedialog
import glob, os
import numpy as np
from PIL import Image


root = Tk()
#display message
myLabel = Label(root, text = "Delete, Move and Copy Files Based on File Types",font=("Helvetica", 20))
myLabel.pack()

#Selecting Folder from dialogue box

def fetchSourceFolder():

    root.withdraw() #Hides small tkinter window.
    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

source_folder = filedialog.askdirectory() #storing folder path in variable.

def fetchDestinationFolder():

    root.withdraw() #Hides small tkinter window.
    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

dest_folder = filedialog.askdirectory() #storing folder path in variable.

#fetching files with various photo extensions

def fetchImages():

        images_jpg = glob.glob(os.path.join(file_name, '*.txt'))
        images_png = glob.glob(os.path.join(file_name, '*.png'))
        images_cr2 = glob.glob(os.path.join(file_name, '*.cr2'))

#Function to move Photos

def moveFiles():
    for j in images_jpg:
        shutil.move(j, os.path.join(source_folder, dest_folder, copy_function = copy2 ))

    for p in images_png:
        shutil.move(p, os.path.join(source_folder, dest_folder, copy_function = copy2 ))

    for c in images_cr2:
        shutil.move(c, os.path.join(source_folder, dest_folder, copy_function = copy2  ))

#Function to copy Photos

def copyPhotos():
    for j in images_jpg:
        shutil.move(j, os.path.join(source_folder, dest_folder, copy_function = copy2 ))

    for p in images_png:
        shutil.move(p, os.path.join(source_folder, dest_folder, copy_function = copy2 ))

    for c in images_cr2:
        shutil.move(c, os.path.join(source_folder, dest_folder, copy_function = copy2  ))


#Function to Delete Photos

def deletePhotos():
    for j in images_jpg:
        os.remove(j)

    for p in images_png:
        os.remove(p)

    for c in images_cr2:
        os.remove(c)



root.mainloop()