import cv2
import os
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import xlrd#还可能因为版本不兼容而安装pyexcel-xls

fps = 1#fps的倒数是每张图片出现的时间
size = (1280, 720)#定义图片大小，需要和视频大小一致


xlsx = xlrd.open_workbook(r"word.xlsx")
sheet1 = xlsx.sheets()[0]  # 获得第1张sheet

for i in range(0, 20):#索引从第0行开始
#for i in range(0, sheet1.nrows):
    word=str(sheet1.row(i)[0].value)
    meaning=str(sheet1.row(i)[1].value)
    #1如果找到，并且后面不是& /，坐标不是0，就在前面加一个换行
    #2找. 如果找到且坐标不是哦0，前面有空格，把空格换成\n
    #3直接把空格换成\n
    point=meaning.find('.')
    point = meaning.find('.', point+1)
    while point!=-1:
        gap=point-1
        while meaning[gap].isalpha() ==True: gap=gap-1
        if meaning[gap]==" ":#replace不行，但是判断可以判断是否为空格
            meaning=meaning[0:gap]+'\n'+meaning[gap+1:]
        point = meaning.find('.', point+1)
            #把空格换成\n
    #####方法3失败 meaning.replace("\u3000", "\r\n", 4);#把空格换成\n，不超过4次
    bk_img = cv2.imread('back.jpg')
    font = ImageFont.truetype("msyh.ttc", 60)#-------------------单词的字体大小
    img_pil = Image.fromarray(bk_img)
    draw = ImageDraw.Draw(img_pil)
    # 绘制文字信息
    draw.text((50, 50), word, font=font, fill=(0, 0, 0))#-------------------单词的绘制位置和颜色
    font = ImageFont.truetype("msyh.ttc", 40)#-------------------释义的字体大小
    draw.text((50, 230), meaning, font=font, fill=(0, 51, 26))#-------------------释义的绘制位置和颜色
    bk_img = np.array(img_pil)
    save_name="./Word/"+word+".jpg"
    print(save_name)
    cv2.imwrite(save_name, bk_img)