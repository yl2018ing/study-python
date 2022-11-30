from __future__ import print_function
from builtins import input
from math import gamma

import cv2 as cv
import numpy as np
import argparse
# Read image given by user

'''
    OpenCV 是一个图像处理库。它包含大量图像处理函数
    本代码功能：
        用于更改图片对比度和亮度，牵扯到循环，速度过于慢
        y是行，x是列，c是 B、G 或 R（0、1 或2)
        若非必要不建议使用
'''

parser = argparse.ArgumentParser(description='将更改图片的对比度和亮度')
parser.add_argument('--input', help='默认使用珊的图片', default='img/shan.jpg')
args = parser.parse_args()
image = cv.imread(cv.samples.findFile(args.input))
if image is None:
    print('无法读取图像，重新输入: ', args.input)
    exit(0)
print(image.shape)
print(image.dtype)
new_image = np.zeros(image.shape, image.dtype)
alpha = 1.0 # Simple contrast control
beta = 0    # Simple brightness control
# Initialize values
print(' Basic Linear Transforms ')
print('-------------------------')
try:
    alpha = float(input('* 请输入透明值 [1.0-3.0]: '))
    beta = int(input('* 请输入beta值 [0-100]: '))
except ValueError:
    print('错误！ 请输入数字')
# Do the operation new_image(i,j) = alpha*image(i,j) + beta
# Instead of these 'for' loops we could have used simply:
# new_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
# but we wanted to show you how to access the pixels :)


for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for c in range(image.shape[2]):
            new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
            print(new_image)


cv.imshow('New Image', new_image)
cv.imwrite('shan-beta.jpg', new_image)

# Wait until user press some key
cv.waitKey()

