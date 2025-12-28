#Thresolding = binarizing image 0=black 255=white

import cv2 as cv
img=cv.imread('Photos/images.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('gray',gray) # name ,pixel which is in img


#Simple Thresold
Thresold,thres=cv.threshold(gray,150,255,cv.THRESH_BINARY)#above 150 then set to 255
cv.imshow("Simple Thresold",thres)
# each pixel is compared with thresold
# pixel>Thresold =255
#pixel<Thresold =0
Thresold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)# inversing 
cv.imshow("inv thresold",thresh)
# we have to manuall specifiy thresold here in some case it might work and in some it wont.


#Adapative Thresolding= no manual thresold
adaptive_thres=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,5) 
#11 is block size to compute mean of thresold value
cv.imshow("Adaptive Thresold",adaptive_thres)

adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,5) 
cv.imshow("AdaptiveThresold",adaptive_thresh)

print(Thresold)

cv.waitKey(0)