import cv2 as cv
img=cv.imread('Photos\images.jpg') # this is bgr image
cv.imshow('Cat',img)

#Edge Cascade
canny=cv.Canny(img,125,175)
cv.imshow('Edge',canny)

#For reducing edge we can pass blur image to canny
#Blur → remove noise → clean edges
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT) 
canny=cv.Canny(blur,125,175) # greater than thresold 2 keep it/ less than thresold 1 discard. im between keep if connected to thresold2
cv.imshow('BlurEdge',canny)
cv.waitKey(0)
#Edge is boundary (where pixel intensity changes sharply)