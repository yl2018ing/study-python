from __future__ import print_function
import numpy as np
import cv2 as cv
import sys

'''
    OpenCV 是一个图像处理库。它包含大量图像处理函数
    本代码功能：
        这个没有学懂
'''

def help(filename):
    print(
        '''
        {0} 展示了OpenCV序列化功能的用法。. \n\n
        usage:\n
            python3 {0} outputfile.yml.gz\n\n
        The output file may be either in XML, YAML or JSON. You can even compress it\n
        by specifying this in its extension like xml.gz yaml.gz etc... With\n
        FileStorage you can serialize objects in OpenCV.\n\n
        For example: - create a class and have it serialized\n
                     - use it to read and write matrices.\n
        '''.format(filename)
    )


class MyData:
    A = 97
    X = np.pi
    name = 'mydata1234'

    def __repr__(self):
        s = '{ name = ' + self.name + ', X = ' + str(self.X)
        s = s + ', A = ' + str(self.A) + '}'
        return s

    def write(self, fs, name):
        fs.startWriteStruct(name, cv.FileNode_MAP | cv.FileNode_FLOW)
        fs.write('A', self.A)
        fs.write('X', self.X)
        fs.write('name', self.name)
        fs.endWriteStruct()

    def read(self, node):
        if (not node.empty()):
            self.A = int(node.getNode('A').real())
            self.X = node.getNode('X').real()
            self.name = node.getNode('name').string()
        else:
            self.A = self.X = 0
            self.name = ''


def main(argv):
    if len(argv) != 2:
        help(argv[0])
        exit(1)
    # write

    R = np.eye(3, 3)
    T = np.zeros((3, 1))

    m = MyData()

    filename = argv[1]

    # XML / YAML文件打开和关闭
    s = cv.FileStorage(filename, cv.FileStorage_WRITE)
    # or:
    # s = cv.FileStorage()
    # s.open(filename, cv.FileStorage_WRITE)

    s.write('iterationNr', 100)

    s.startWriteStruct('strings', cv.FileNode_SEQ)
    for elem in ['img/pu.jpg', 'Awesomeness', 'img/pu.jpg']:
        s.write('', elem)
    s.endWriteStruct()

    s.startWriteStruct('Mapping', cv.FileNode_MAP)
    s.write('One', 1)
    s.write('Two', 2)
    s.endWriteStruct()

    s.write('R_MAT', R)
    s.write('T_MAT', T)

    m.write(s, 'MyData')

    s.release()

    print('Write Done.')
    # read
    print('\nReading: ')
    s = cv.FileStorage()
    s.open(filename, cv.FileStorage_READ)

    n = s.getNode('iterationNr')
    itNr = int(n.real())

    print(itNr)
    if (not s.isOpened()):
        print('Failed to open ', filename, file=sys.stderr)
        help(argv[0])
        exit(1)

    n = s.getNode('strings')
    if (not n.isSeq()):
        print('strings is not a sequence! FAIL', file=sys.stderr)
        exit(1)
    for i in range(n.size()):
        print(n.at(i).string())

    n = s.getNode('Mapping')
    print('Two', int(n.getNode('Two').real()), '; ')
    print('One', int(n.getNode('One').real()), '\n')

    R = s.getNode('R_MAT').mat()
    T = s.getNode('T_MAT').mat()

    m.read(s.getNode('MyData'))

    print('\nR =', R)
    print('T =', T, '\n')
    print('MyData =', '\n', m, '\n')

    print('Attempt to read NonExisting (should initialize the data structure',
          'with its default).')
    m.read(s.getNode('NonExisting'))
    print('\nNonExisting =', '\n', m)

    print('\nTip: Open up', filename, 'with a text editor to see the serialized data.')


if __name__ == '__main__':
    main(sys.argv)