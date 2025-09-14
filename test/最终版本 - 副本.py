import fitz
import os
import shutil
import zipfile
import string
from PIL import Image  

#zip下的webp或jpg图片转pdf
is_out = False
while(1):
    
    print("Ciallo～(∠・ω< )⌒☆很高兴和你见面，先让本小姐明确您的要求( • ̀ω•́ )✧\n1、webp原图要保留吗")
    webpstr='yes'#input("yes or no：")
    print("2、jpg图片要保存吗")
    jpgstr='yes'#input("yes or no：")
    print("解压对象的名字叫什么呢（如果已解压请输入'no'）")
    #zip_name=input()#'420116'
    print("解压后的名字应该叫什么呢")
    #namestr=input()
    is_exist = False
    zip_name= 0
    for i_name in os.listdir(os.getcwd()):
        if i_name.endswith('.zip'):
            cut = i_name[0:-4]
            if len(cut) == 6 and int(cut) <= 1000000:
                
                zip_name = cut
                is_exist = True
                print('--------------------------------' + zip_name)
                break
    namestr=zip_name
    print('--------------------------------' + zip_name)

    if(zip_name!='no'):
        zf = zipfile.ZipFile(zip_name + '.zip')
        ret=zf.extractall()
        zf.close()
    doc = fitz.open()
    # os.listdir()方法获取文件夹名字，返回数组
    #新建一个文件夹，把webp导入新建文件夹并删除
    oriway = os.getcwd()
    name_list = os.listdir(os.getcwd())
    print(name_list)
    
    iswebp = 0 
    for webp_name in name_list:#webp转jpg
        if webp_name.endswith('.webp'):  
            im = Image.open(webp_name)
            print('处理webp：'+ webp_name+ '中......')
            if im.mode == "RGBA":
                im.load()  # required for png.split()  
                background = Image.new("RGB", im.size, (255, 255, 255))  
                background.paste(im, mask=im.split()[3])
                iswebp = 1
                print(iswebp)
            jpg_name = webp_name.replace('webp', 'jpg')
            if not os.path.exists(jpg_name):  
                #print("%s -> %s"%(webp_name,jpg_name))
                im.save('{}'.format(jpg_name), 'JPEG')
                print(jpg_name+'转换完成')
                #im.save(jpg_name)
            #webp_name.close()

    if iswebp == 0:
        vname = os.getcwd()# + '/1'
        for jpg_name in os.listdir(vname):
            src = vname + '/' + jpg_name
            dst = oriway# + ' /' + jpg_name
            print('源文件：' + src + '35483252447895897423563489534987594382547857454387547')
            print('目标文件：' + dst + '35483252447895897423563489534987594382547857454387547')
            shutil.copy2(src, dst)
            
    name_list = os.listdir(os.getcwd())
    for jpg_name in name_list:#jpg转pdf
        #print(jpg_name)
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
    
    #isre=input("输入【st】结束，若要继续解压请输入【re】")
    #if(isre=='st'):
    #    break
    if(is_exist == False):
        break
print("感谢您的使用")
