import cv2
import os
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import xlrd#还可能因为版本不兼容而安装pyexcel-xls

fps = 1#fps的倒数是每张图片出现的时间
size = (1280, 720)#定义图片大小，需要和视频大小一致

fileType='test'
path = r'test.txt'
sum=0
with open(path, 'r', encoding='utf-8') as file_to_read:#需要加, encoding='utf-8'，已解决无法split的问题
    for line in file_to_read:#加入有音标的txt文件后，编码出现问题，txt内显示正常，生成图片则失败
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
        point = meaning.find('.')#找到单词释义里的词性后的‘.’
        point = meaning.find('.', point + 1)#确认后面是否有第二个释义
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
        # bk_img = cv2.imread('back.jpg')
        # font = ImageFont.truetype("times.ttf", 110)  # -------------------单词的字体大小
        # img_pil = Image.fromarray(bk_img)
        # draw = ImageDraw.Draw(img_pil)
        # # 绘制文字信息
        # draw.text((50, 80), word, font=font, fill=(0, 0, 0))  # -------------------单词的绘制位置和颜色
        # font = ImageFont.truetype("times.ttf", 50)  # -------------------【音标】的字体大小,音标难以渲染，发现是字体不支持导致的
        # draw.text((50, 230), voc, font=font, fill=(255,100,100))  # ------------------【音标】的绘制位置和颜色
        # font = ImageFont.truetype("msyh.ttc", 50)  # -------------------释义的字体大小
        # draw.text((50, 350), meaning, font=font, fill=(70,70,70))  # -------------------释义的绘制位置和颜色
        # bk_img = np.array(img_pil)
        # save_name = "./test/" + str(sum) + ".jpg"
        # if sum%20==0:
        #     print('NO.'+str(sum)+' '+word)
        # cv2.imwrite(save_name, bk_img)
        
