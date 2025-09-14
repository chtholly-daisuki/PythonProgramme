import fitz
import os
import shutil
from PIL import Image  

doc = fitz.open()
# os.listdir()方法获取文件夹名字，返回数组
#新建一个文件夹，把webp导入新建文件夹并删除
name_list = os.listdir(os.getcwd())

print("Ciallo～(∠・ω< )⌒☆很高兴和你见面，先让本小姐明确您的要求( • ̀ω•́ )✧\n1、webp原图要保留吗")
webpstr=input("yes or no：")
print("2、jpg图片要保存吗")
jpgstr=input("yes or no：")
print("名字叫什么")
namestr=input()

for webp_name in name_list:#webp转jpg
    if webp_name.endswith('.webp'):  
        im = Image.open(webp_name)  
        if im.mode == "RGBA":
            print('处理webp：'+ webp_name+ '中......')
            im.load()  # required for png.split()  
            background = Image.new("RGB", im.size, (255, 255, 255))  
            background.paste(im, mask=im.split()[3])  
        jpg_name = webp_name.replace('webp', 'jpg')
        if not os.path.exists(jpg_name):  
            #print("%s -> %s"%(webp_name,jpg_name))
            im.save('{}'.format(jpg_name), 'JPEG')
for jpg_name in name_list:
    if jpg_name.endswith('.jpg'):
        pdf_name = jpg_name.replace('jpg', 'pdf')
        imgdoc = fitz.open(jpg_name)
        pdfbytes = imgdoc.convert_to_pdf()
        print('处理jpg：'+ jpg_name+ '中......')
        
        imgpdf = fitz.open(pdf_name, pdfbytes)
        doc.insert_pdf(imgpdf)
save_location = 'G:\书\社会历史\本'
origin_location = os.path.dirname(__file__)
if ~os.path.exists(save_location + '/' + namestr) : os.mkdir(save_location + '/' + namestr)

#new一个文件夹，把文件移入，并删除原文件夹文件
if webpstr == 'yes' and ~os.path.exists(save_location + '/' + namestr + '/webp版本') :
    os.mkdir(save_location + '/' + namestr + '/webp版本')
    print('nmslnmslnmsl/n/n/n')
if jpgstr == 'yes' and ~os.path.exists(save_location + '/' + namestr + '/jpg版本') :
    os.mkdir(save_location + '/' + namestr + '/jpg版本')
    print('igsuqgwiqwqwd/n/n/n')

for i in os.listdir(os.getcwd()):
    if i.endswith('.webp'):
        srcwebp = origin_location
        dstwebp = save_location + '/' + namestr + '/webp版本'
        if webpstr=='yes':
            print(os.path.abspath(i))
            shutil.copy2(os.path.abspath(i), dstwebp)#复制
            os.remove(os.path.abspath(i))#删除
        else :
            os.remove(os.path.abspath(i))#删除
    if i.endswith('.jpg'):
        srcjpg = origin_location
        dstjpg = save_location + '/' + namestr + '/jpg版本'
        if jpgstr=='yes':
            print(os.path.abspath(i))
            shutil.copy2(os.path.abspath(i), dstjpg)#复制
            os.remove(os.path.abspath(i))#删除
        else :
            os.remove(os.path.abspath(i))#删除
doc_name= namestr + '.pdf'
doc.save(doc_name)
doc.close()

srcpdf = origin_location
dstpdf = save_location + '/' + namestr+'/pdf版'+'.pdf'

shutil.copy2(doc_name, dstpdf)#复制
os.remove(doc_name)#删除

with open(save_location + '/' + namestr+ '/名字.txt','w') as f:
    f.write (namestr)

input("回车结束操作")
