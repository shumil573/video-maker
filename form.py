import cv2
import os
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import xlrd#还可能因为版本不兼容而安装pyexcel-xls

fps = 1#fps的倒数是每张图片出现的时间
size = (1280, 720)#定义图片大小，需要和视频大小一致

path = r'unform.txt'
sum=0
with open(path, 'r', encoding='utf-8') as file_to_read:#需要加, encoding='utf-8'，已解决无法split的问题
    for line in file_to_read:
        sum=sum+1
        lines = line.split(' ')  # 整行读取数据
        voc=''
        if(len(lines)==2):
            word=lines[0]
            meaning=lines[1]
        else :
            word = lines[0]
            voc=lines[1]
            meaning = lines[2]
        point = meaning.find('.')
        point = meaning.find('.', point + 1)
        while point != -1:
            gap = point - 1
            while meaning[gap].isalpha() == True:
                gap = gap - 1
            if meaning[gap] == ";":
                meaning = meaning[0:gap+1] + '\n' + meaning[gap + 1:]
            point = meaning.find('.', point + 1)
            # 把空格换成\n
        #####方法3失败 meaning.replace("\u3000", "\r\n", 4);#把空格换成\n，不超过4次
        means=meaning.split('\n')
        meanSize=40
        meanBegin=50
        count = (1280 - meanBegin) // meanSize
        count=count+5
        meaning=''
        for it in means:
            if len(it)>count:
                it=it[:count]+'\n'+it[count:]
                #print(it)
            meaning=meaning+it+'\n'
        bk_img = cv2.imread('back.jpg')
        font = ImageFont.truetype("msyh.ttc", 72)  # -------------------单词的字体大小
        img_pil = Image.fromarray(bk_img)
        draw = ImageDraw.Draw(img_pil)
        # 绘制文字信息
        draw.text((50, 50), word, font=font, fill=(0, 0, 0))  # -------------------单词的绘制位置和颜色
        font = ImageFont.truetype("msyh.ttc", 36)  # -------------------【音标】的字体大小
        draw.text((50, 130), voc, font=font, fill=(255,100,100))  # ------------------【音标】的绘制位置和颜色
        font = ImageFont.truetype("msyh.ttc", 40)  # -------------------释义的字体大小
        draw.text((50, 230), meaning, font=font, fill=(70,70,70))  # -------------------释义的绘制位置和颜色
        bk_img = np.array(img_pil)
        save_name = "./FormWord/" + lines[0] + ".jpg"
        if sum%20==0:
            print('NO.'+str(sum)+' '+save_name)
        cv2.imwrite(save_name, bk_img)
