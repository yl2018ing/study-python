import cv2 as cv
import numpy as np

'''
    OpenCV 是一个图像处理库。它包含大量图像处理函数
    本代码功能：
        读取图像数据
        将图像从彩色转换到黑色
        找到最小和最大强度
        生成一张类似泥巴一样的图片
        
        姑且将此代码叫做，生成泥巴图片代码
'''

img = cv.imread('img/shan.jpg')

# 将图像从彩色转换到黑色
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sobelx = cv.Sobel(grey, cv.CV_32F, 1, 0)

# 找到最小和最大强度
minVal = np.amin(sobelx)
maxVal = np.amax(sobelx)
draw = cv.convertScaleAbs(sobelx, alpha=255.0 / (maxVal - minVal), beta=-minVal * 255.0 / (maxVal - minVal))

cv.imshow('image',draw)
cv.imwrite('img/shan-ni.jpg',draw)
cv.waitKey()