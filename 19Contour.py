# we will use threshold for finding edge instead of canny
# thresolding binarize the image either make pixel 0 or 255
import cv2 as cv
import numpy as np

img=cv.imread('Photos/images.jpg')
cv.imshow("cat",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
ret,thres=cv.threshold(gray,125,255,cv.THRESH_BINARY) # thresold ,max value(if>thresold),binarizing image
# If pixel value > 125 → set to 255 (white)
# If pixel value ≤ 125 → set to 0 (black)

# ret = threshold used
# thres = new binary image
cv.imshow('thresold',thres)

contours,heirarchy=cv.findContours(thres,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv.waitKey(0)