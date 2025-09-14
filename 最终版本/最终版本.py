import fitz
import os
import shutil
import zipfile
from PIL import Image  

#zip下的webp或jpg图片转pdf

while(1):
    print("Ciallo～(∠・ω< )⌒☆很高兴和你见面，先让本小姐明确您的要求( • ̀ω•́ )✧\n1、webp原图要保留吗")
    webpstr='yes'#input("yes or no：")
    print("2、jpg图片要保存吗")
    jpgstr='yes'#input("yes or no：")
    print("解压对象的名字叫什么呢（如果已解压请输入'no'）")
    zip_name=input()#'420116'
    print("解压后的名字应该叫什么呢")
    #namestr=input()
    namestr=zip_name

    if(zip_name!='no'):
        zf = zipfile.ZipFile(zip_name+'.zip')
        ret=zf.extractall()
        zf.close()
    doc = fitz.open()
    # os.listdir()方法获取文件夹名字，返回数组
    #新建一个文件夹，把webp导入新建文件夹并删除
    name_list = os.listdir(os.getcwd())
    

    for webp_name in name_list:#webp转jpg
        if webp_name.endswith('.webp'):  
            im = Image.open(webp_name)
            print('处理webp：'+ webp_name+ '中......')
            if im.mode == "RGBA":
                im.load()  # required for png.split()  
                background = Image.new("RGB", im.size, (255, 255, 255))  
                background.paste(im, mask=im.split()[3])  
            jpg_name = webp_name.replace('webp', 'jpg')
            if not os.path.exists(jpg_name):  
                #print("%s -> %s"%(webp_name,jpg_name))
                im.save('{}'.format(jpg_name), 'JPEG')
                print(jpg_name+'转换完成')
                #im.save(jpg_name)
            #webp_name.close()
    name_list = os.listdir(os.getcwd())
    for jpg_name in name_list:#jpg转pdf
        if jpg_name.endswith('.jpg'):
            print('将jpg：'+ jpg_name+ '转换为pdf中......')
            pdf_name = jpg_name.replace('jpg', 'pdf')
            imgdoc = fitz.open(jpg_name)
            pdfbytes = imgdoc.convert_to_pdf()
        
            imgpdf = fitz.open(pdf_name, pdfbytes)
            doc.insert_pdf(imgpdf)
            #jpg_name.close()
    save_location = 'G:\书\社会历史\本'
    origin_location = os.path.dirname(__file__)
    if ~os.path.exists(save_location + '/' + namestr) : os.mkdir(save_location + '/' + namestr)

    #new一个文件夹，把文件移入，并删除原文件夹文件
    if webpstr == 'yes' and ~os.path.exists(save_location + '/' + namestr + '/webp版本') :
        os.mkdir(save_location + '/' + namestr + '/webp版本')
        print('nmslnmslnmsl\n/n/n')
    if jpgstr == 'yes' and ~os.path.exists(save_location + '/' + namestr + '/jpg版本') :
        os.mkdir(save_location + '/' + namestr + '/jpg版本')
        print('igsuqgwiqwqwd\n/n/n')

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

    old_zip_name = os.path.dirname(__file__) + '/' + zip_name + '.zip'
    new_zip_name = os.path.dirname(__file__) + '/' + zip_name + '已解压.zip'
    os.rename(old_zip_name,new_zip_name)
    
    isre=input("输入【st】结束，若要继续解压请输入【re】")
    if(isre=='st'):
        break
print("感谢您的使用")
