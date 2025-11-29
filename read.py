import cv2 as cv
img=cv.imread('Photos/images.jpg')
cv.imshow('Cat',img) # name ,pixel which is in img
cv.waitKey(0)