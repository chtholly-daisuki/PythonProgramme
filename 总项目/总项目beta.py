import fitz
import os  
from PIL import Image  

doc = fitz.open()
# os.listdir()方法获取文件夹名字，返回数组
#新建一个文件夹，把webp导入新建文件夹并删除
webp_name_list = os.listdir(os.getcwd())  
for webp_name in webp_name_list:
    print(webp_name)
    if webp_name.endswith('.webp'):  
        im = Image.open(webp_name)  
        if im.mode == "RGBA":  
            im.load()  # required for png.split()  
            background = Image.new("RGB", im.size, (255, 255, 255))  
            background.paste(im, mask=im.split()[3])  
        jpg_name = webp_name.replace('webp', 'jpg')
        pdf_name = webp_name.replace('webp', 'pdf')
        
        if not os.path.exists(jpg_name):  
            print("%s -> %s"%(webp_name,jpg_name))
            im.save('{}'.format(jpg_name), 'JPEG')
        
        imgdoc = fitz.open(jpg_name)
        pdfbytes = imgdoc.convert_to_pdf()
        
        imgpdf = fitz.open(pdf_name, pdfbytes)
        doc.insert_pdf(imgpdf)
            
            
string=input("整合的pdf文件该叫什么名字呢？")
doc_name=string + '.pdf'
doc.save(doc_name)
doc.close()
input("回车结束操作")
