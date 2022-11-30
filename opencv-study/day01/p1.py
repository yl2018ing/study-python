import cv2 as cv
import sys

'''
    OpenCV 是一个图像处理库。它包含大量图像处理函数
    本代码功能：
        读取图像数据
        将图像读成灰度
        将图像制成黑色\白色
        保存图像
        显示图像
        等待图像窗口中的按键
        如果按键S，则将图片另存成一张PNG图片
'''

# 读取图像数据
img = cv.imread(cv.samples.findFile("img/pu.jpg"))
print('------------------------------------------------')
# 从文件加载图像
'''
    如果您读取一个 jpg 文件，默认情况下会创建一个 3 通道图像。
    灰度图像:cv.IMREAD_GRAYSCALE
'''
img2 = cv.imread('img/pu.jpg',cv.IMREAD_GRAYSCALE)

# 制作黑色图像,0黑 255白
img2[:] = 0

# 保存图像
cv.imwrite('img/pu-bai.jpg',img2)
# 如果图像加载正确
if img is None:
    sys.exit(" 无法阅读图像")



# 显示图像，第一个参数是窗口的标题，会结束很快
cv.imshow('显示窗',img)
# 设置为0表示永远等待，直到按下某个键
k = cv.waitKey(0)

# 如果按下的键是“s”键，图像将被写入文件
if k == ord("s"):
    cv.imwrite('img/pu.png',img)