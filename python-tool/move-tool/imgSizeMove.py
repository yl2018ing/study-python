import os
from PIL import Image
import shutil
import imghdr

'''
    功能：
        本代码实现将相同大小的图片移动到一起，文件夹以图片的大小命名
        损坏的图片移动到损坏的文件夹
'''


def moveImg(dirs, dirImg, doneDir, badDir):
    # 拼接完整图片路径
    img = dirs + dirImg
    # 判断图片是否损坏
    if imghdr.what(img):
        # 读取图片的大小
        img_size = Image.open(img).size
        # 目录不存在,创建目录
        if not os.path.exists(doneDir + str(img_size)):
            print('目录不存在', img_size)
            os.makedirs(doneDir + str(img_size))
        # 移动图片
        shutil.move(img, doneDir + str(img_size) + '/' + dirImg)
    else:
        # 异常图片
        shutil.move(img, badDir + dirImg)
        print(img, '图片异常')


if __name__ == '__main__':
    total = 0  # 总数
    bad = 0  # 损坏数量
    img_dirs = ''  # 图片所在的文件夹
    done_dirs = ''  # 完成后存放的文件夹
    bad_dirs = ''  # 损坏图片存放的文件夹
    # 遍历图片路径：图片路径
    path = os.listdir(img_dirs)
    total = len(path)
    print('共%d张图片！' % total)
    for img_path in path:
        # 调用移动图片方法
        moveImg(img_dirs, img_path, done_dirs, bad_dirs)
