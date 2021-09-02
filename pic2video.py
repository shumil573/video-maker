import cv2
import os
import pygame
from PIL import Image, ImageFont, ImageDraw
import io
import numpy as np
import xlrd#还可能因为版本不兼容而安装pyexcel-xls
fps = 1#fps的倒数是每张图片出现的时间
size = (1280, 720)


#videowriter = cv2.VideoWriter("test.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)
videowriter = cv2.VideoWriter("cet6edit.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)
#path = r'./Word/'
path = r'./FormWord/'
for i in os.listdir(path):
    img = cv2.imread(path + i)
    img=cv2.resize(img,(1280, 720))#VideoWriter只能处理和画面一样大的图片，所以需要转换
    videowriter.write(img)
videowriter.release()
cv2.destroyAllWindows()