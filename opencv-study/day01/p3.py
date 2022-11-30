
from __future__ import print_function
import cv2 as cv

'''
    OpenCV 是一个图像处理库。它包含大量图像处理函数
    本代码功能：
        加载两个图像，因为要添加，所以二者的高度和宽度必须相同
        等待用户输入透明度范围在0和1之间，如果在这个范围内就用这个输入的，否则默认用0.5透明度
       这个透明度是第一张图片的透明度，0为全透明，1为不透明
       功能类似于 PS两个图层 修改透明度 第一张图片在上，第二张图片在下
       可以用于两张一样大小的图片加水印，但是一般水印都比较小，不建议用此方法
'''

alpha = 0.5
raw_input = input

print(''' Simple Linear Blender
-----------------------
* Enter alpha [0.0-1.0]: ''')

input_alpha = float(raw_input().strip())
if 0 <= alpha <= 1:
    alpha = input_alpha

print('透明度为',alpha)
print('请稍等............')
# [load]
src1 = cv.imread(cv.samples.findFile('img/add1.jpg'))
src2 = cv.imread(cv.samples.findFile('img/add2.jpg'))
# [load]
if src1 is None:
    print("Error loading src1")
    exit(-1)
elif src2 is None:
    print("Error loading src2")
    exit(-1)
# [blend_images]


beta = (1.0 - alpha)
dst = cv.addWeighted(src1, alpha, src2, beta, 0.0)
# [blend_images]
# [display]
cv.imwrite('img/add-done.jpg', dst)
print('-------准备为您展示------')
cv.imshow('dst', dst)
cv.waitKey(0)
# [display]
cv.destroyAllWindows()