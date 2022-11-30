import cv2 as cv

flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print( flags )
img = cv.imread('img/work.png')

print(img.shape)


cv.imshow('test',img)
print(img)
cv.waitKey(0)