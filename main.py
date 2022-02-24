from fileinput import filename
from tkinter import *
from tkinter import font
from tkinter import Tk
import glob, os, shutil
import numpy as np
from PIL import Image
from tkinter import filedialog



root = Tk()
#display message
myLabel = Label(root, text = "Delete, Move and Copy Files Based on File Types",font=("Helvetica", 20))
myLabel.grid(row=0)





dest_folder = "" #declaring variable to hool the path for the destination folder
source_folder = "" #declaring variable to hool the path for the source folder


#function to get the path for the source folder

def fetchSourceFolder():
    source_folder = filedialog.askdirectory() #storing folder path in variable.


#button to open file explorer for the selection of a folder
sourceButton = Button(root, text = "Choose Source Folder", padx = 50, pady = 10, command = fetchSourceFolder)
sourceButton.grid(row = 10, column = 0)


#function to get the path for the destination folder
def fetchDestinationFolder():
    dest_folder = filedialog.askdirectory() #storing folder path in variable.


#button to open file explorer for the selection of a folder
destButton = Button(root, text = "Choose Destination Folder", padx = 50, pady = 10, command = fetchDestinationFolder)

destButton.grid(row = 15, column = 0)

"""

images =     glob.glob(R'C:\Users\Kelvin\Desktop\pract.jpg')

print(images)
"""

#fetching files based on file types
images_jpg = glob.glob(os.path.join(source_folder, '*.jpg'))
images_png = glob.glob(os.path.join(source_folder, '*.png'))
images_cr2 = glob.glob(os.path.join(source_folder, '*.cr2'))


#functions to move, delete, and copy the files.
"""
def moveFiles():
    for j in images_jpg:
        shutil.move(j, dest_folder )

    for p in images_png:
        shutil.move(p, dest_folder )

    for c in images_cr2:
        shutil.move(c, dest_folder )

"""
"""
def moveFiles():
    for j in images_jpg:
        shutil.move(j, os.path.join(source_folder, dest_folder ))

    for p in images_png:
        shutil.move(p, os.path.join(source_folder, dest_folder ))

    for c in images_cr2:
        shutil.move(c, os.path.join(source_folder, dest_folder ))

#Function to copy Photos

moveButton = Button(root, text = "Move Picture Files", padx = 50, pady = 10, command = moveFiles)

moveButton.grid(row = 20, column = 0)


def copyPhotos():
    for j in images_jpg:
        shutil.move(j, os.path.join(source_folder, dest_folder ))

    for p in images_png:
        shutil.move(p, os.path.join(source_folder, dest_folder ))

    for c in images_cr2:
        shutil.move(c, os.path.join(source_folder, dest_folder  ))


#Function to Delete Photos

def deletePhotos():
    for j in images_jpg:
        os.remove(j)

    for p in images_png:
        os.remove(p)

    for c in images_cr2:
        os.remove(c)


"""
root.mainloop()