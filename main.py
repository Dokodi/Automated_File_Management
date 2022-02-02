
import glob, os
import numpy as np
from PIL import Image
import shutil


images_jpg = glob.glob(r"C:\Users\Kelvin\Desktop\File_Management\pract\*.jpg")
images_png = glob.glob(r"C:\Users\Kelvin\Desktop\File_Management\pract\*.png")
images_cr2 = glob.glob(r"C:\Users\Kelvin\Desktop\File_Management\pract\*.cr2")

root_dir = r"C:\Users\Kelvin\Desktop\File_Management"
dest_dir = os.path.join(root_dir, "dest")
file_dir = os.path.join(root_dir, "files")

"""
print(images_jpg)
print(images_png)
"""

for i in images_jpg:
    shutil.move(i, os.path.join(dest_dir, "jpg_files"))

for j in images_png:
    shutil.move(j, os.path.join(dest_dir, "png_files"))

