import fitz  

img_path = 'H:\download\图片助手(ImageAssistant)_批量图片下载器/18comic.vip\[まめおじたん]_Knospenmädchen_(中文無修)_H漫內頁瀏覽_Comics_-_禁漫天堂/'
doc = fitz.open()
# H:\download\图片助手(ImageAssistant)_批量图片下载器\18comic.vip\[まめおじたん]_Knospenmädchen_(中文無修)_H漫內頁瀏覽_Comics_-_禁漫天堂
# H:/download/图片助手(ImageAssistant)_批量图片下载器/18comic.vip/[まめおじたん]_Knospenmädchen_(中文無修)_H漫內頁瀏覽_Comics_-_禁漫天堂
# 循环path中的文件，可import os 然后用 for img in os.listdir(img_path)实现
# 这里为了让文件以1，2，3的形式进行拼接，就偷懒循环文件名中的数字。
for i in range(10001,10178):
	img = str(i) + '.jpg'
	img_file = img_path + img
	imgdoc = fitz.open(img_file)
	pdfbytes = imgdoc.convert_to_pdf()
	pdf_name = str(i) + '.pdf'
	imgpdf = fitz.open(pdf_name, pdfbytes)
	doc.insert_pdf(imgpdf)
doc.save('combined.pdf')
doc.close()
