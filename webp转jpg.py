# coding:utf-8  
import os  
from PIL import Image  
  
# os.listdir()方法获取文件夹名字，返回数组  
file_name_list = os.listdir(os.getcwd())  
for file_name in file_name_list:  
    if file_name.endswith('.webp'):  
        im = Image.open(file_name)  
        if im.mode == "RGBA":  
            im.load()  # required for png.split()  
            background = Image.new("RGB", im.size, (255, 255, 255))  
            background.paste(im, mask=im.split()[3])  
        save_name = file_name.replace('webp', 'jpg')  
        if not os.path.exists(save_name):  
            print("%s -> %s"%(file_name,save_name))  
            im.save('{}'.format(save_name), 'JPEG')  
input("回车结束操作")
