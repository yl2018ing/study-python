import os
import shutil

"""
    需求：在经历imgSizeMove程序后，想要将文件夹内的数个文件夹里的第一张图片移动到一起
    本代码实现将数个文件夹中的第一张图片移动到一起
    复制：shutil.copy()
"""
def main():
    img_dirs = r'E:\test/'  # 需要遍历的图片文件夹
    done_dirs = r'E:\img/'  # 保存的文件夹
    path = os.listdir(img_dirs)
    total = len(path)
    print('共%d张图片！' % total)
    for i in path:
        sizeDir = os.listdir(img_dirs + i)
        # 遍历子文件夹
        for j in sizeDir:
            print(img_dirs + i + '/' + j)
            # 移动第一张图片
            shutil.move(img_dirs + str(i) + '/' + j, done_dirs + str(i) + '.' + j.split('.')[1])
            break


if __name__ == '__main__':
    main()

    print('已完成')