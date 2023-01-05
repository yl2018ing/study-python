# 该功能用来批量修改图片的尺寸
from PIL import Image
import os

'''
    本功能实现批量修改文件夹内图片的尺寸
    更改图片的高度和宽度
    在此之前，可以使用移动或者复制图片程序
    将相同尺寸移动到一个文件夹
    再使用此功能
'''


def main():

    while (1):
        file_path = input(r'请输入图像所在文件夹路径：')
        if os.path.exists(file_path):
            break
        else:
            print('提示——没有这个文件夹，请重新输入')
    save_path = input(r'请输入图片修改大小后的存储路径，没有会新建')
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    width = inputSize('请输入修改后的图片宽度')
    height = inputSize('请输入修改后的图片高度')

    raw_files = os.walk(file_path)  # 遍历文件夹内所有图像
    for root, dirs, files in raw_files:
        for file in files:  # 展现各文件
            picture_path = os.path.join(root, file)  # 得到图像的绝对路径
            pic_org = Image.open(picture_path)  # 打开图像

            pic_new = pic_org.resize((width, height), Image.ANTIALIAS)  # 图像尺寸修改
            _, sub_folder = os.path.split(root)  # 得到子文件夹名字
            pic_new_path = os.path.join(save_path, sub_folder)
            if not os.path.exists(pic_new_path):
                os.makedirs(pic_new_path)  # 建立子文件夹
            pic_new_path = os.path.join(pic_new_path, file)  # 新图像存储绝对路径
            pic_new.save(pic_new_path)  # 存储文件
            print(pic_new_path)


def inputSize(name):
    while (1):
        size = input(name)
        if size.isdigit():
            return int(size)
        else:
            print('提示——输入不是数字，请重新输入：')


if __name__ == '__main__':
    main()
