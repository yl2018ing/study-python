import imghdr
import os
import cv2
from PIL import Image
import shutil

'''
    本代码实现了通过一张蒙版图去除图片水印(蒙版图需与要去除水印的图片一样大小）
    需要加水印则填入logo路径，否则不要填
    读取图片大小进行比较，如果大小一致则返回True，否则返回False
'''


# 读取图片大小，进行比较
def read_size(img, size):
    img_size = Image.open(img).size

    if img_size == size:
        return True
    else:
        return False


# 目录不存在就创建
def mulu(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
        print('成功创建一个目录：', dirs)


'''
     蒙版去水印
     完整图片路径
     相对图片路径
     蒙版图片路径
     蒙版图大小
     完成存放目录
     需要加水印
     则传入水印路径
'''


def qsy(img, img_path, mark_path,done_dirs, logo_path=None):
    img = cv2.imread(img)  # 读取图片
    mask = cv2.imread(mark_path, cv2.IMREAD_GRAYSCALE)  # 读取蒙版
    dst = cv2.inpaint(img, mask, 1, cv2.INPAINT_TELEA)  # 去除水印

    cv2.imwrite(done_dirs + img_path, dst)  # 保存图片
    if logo_path:
        jsy(done_dirs + img_path, logo_path)


'''
    加水印
    水印大小不能超过图片大小
    会覆盖原本的图片
    如无需覆盖，可自行更改保存路径
'''


def jsy(img, logo_path):
    img1 = Image.open(img).convert('RGBA')
    img2 = Image.open(logo_path).convert('RGBA')
    wid = Image.open(img).width
    hei = Image.open(img).height
    r, g, b, a = img2.split()

    img1.paste(img2, (int(wid/3), int(hei/4)), mask=a)  # logo 位置(X坐标，Y坐标）
    img1 = img1.convert('RGB')
    img1.save(img)


if __name__ == '__main__':
    total = 0  # 总数
    bad = 0  # 损坏数量
    move = 0  # 移动数量
    win = 0  # 成功数量

    img_dirs = 'img/'  # 需要处理的图片目录（图片所在的文件夹）
    mark_path = 'mark/1280.jpg'  # 蒙版图路径（需要一样大小)
    logo_path = 'logo/logo.png'  # LOGO路径
    done_dirs = 'done/'  # 完成后的存放目录
    other_dirs = 'other/'  # 其它的目录
    bad_dirs = 'bad/'  # 图片损坏存放目录

    mark_size = Image.open(mark_path).size  # 读取蒙版图的大小

    if not os.path.exists(img_dirs):
        print('错误！没有找到这个需要去水印的文件夹，程序终止！')
    else:
        # 其他的目录不存在，就创建
        mulu(done_dirs)
        mulu(other_dirs)
        mulu(bad_dirs)

        paths = os.listdir(img_dirs)
        total = len(paths)
        print('去水印开始了，共' + str(total) + '张图片！')


        # 开始遍历目录下的每一张图片
        for img_path in paths:
            img = img_dirs + img_path  # 拼接成完整的图片路径

            # 判断图片是否损坏,what用于返回图片类型
            if imghdr.what(img):

                # 如果两张图片大小一致，便开始去除水印，否则将不能处理的图片移动到其他的目录
                if read_size(img, mark_size):
                    qsy(img, img_path, mark_path, done_dirs, logo_path)
                    win += 1
                    total -= 1
                    print('处理成功！共%d张图片处理成功，还剩%d张图片未处理。' % (win, total))
                else:
                    shutil.move(img, other_dirs + img_path)
                    move += 1
                    total -= 1
                    print('图片大小不一致！共%d张图片大小不一致，还剩%d张图片未处理。' % (move, total))

            else:
                shutil.move(img, bad_dirs + img_path)
                bad += 1
                total -= 1
                print('图片损坏！共%d张图片损坏，还剩%d张图片未处理。' % (bad, total))
        print('--------------------------------')
        print('已完成所有处理！')
        print('剩余%d张图片'%total)
        print('完成%d张图片'%win)
        print('移动%d张图片'%move)
        print('损坏%d张图片'%bad)
