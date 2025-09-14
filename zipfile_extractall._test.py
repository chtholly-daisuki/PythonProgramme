import fitz
import os
import shutil
import zipfile
import string
from PIL import Image  

zip_name = '1z18479.zip'
zf = zipfile.ZipFile(zip_name)

path_out = os.getcwd() + '/' + zip_name

zf.extractall(path = path_out)
