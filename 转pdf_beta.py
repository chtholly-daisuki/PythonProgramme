import os
from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(0)         # 自动分页设为False

path = r"H:\download\图片助手(ImageAssistant)_批量图片下载器\18comic.vip\[まめおじたん]_Knospenmädchen_(中文無修)_H漫內頁瀏覽_Comics_-_禁漫天堂"
imagelist = [i for i in os.listdir(path)]


for image in sorted(imagelist):
    pdf.add_page()
    pdf.image(os.path.join(path, image))      # 指定宽高

pdf.output(os.path.join(path, "佩奇.pdf"), "F")
