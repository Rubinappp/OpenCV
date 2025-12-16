import cv2 as cv
import numpy as np
img=cv.imread('Photos\images.jpg') 
cv.imshow('Cat',img)

blank=np.zeros(img.shape[:2],dtype='uint8')# should be same size of the image else assertion error
cv.imshow("blank",blank)

Circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2+10),100,255,-1)
cv.imshow('Mask',Circle)
masked=cv.bitwise_and(img,img,mask=Circle)
cv.imshow("Masked image",masked)
#If mask pixel = 255 → keep img pixel
#If mask pixel = 0   → set result pixel to black

rectangle=cv.rectangle(blank.copy(),(0,0),(100,100),255,thickness=-1)
cv.imshow('Rectangle',rectangle)
masked1=cv.bitwise_and(img,img,mask=rectangle)
cv.imshow("masked1",masked1)

weird_shape=cv.bitwise_and(Circle,rectangle)
cv.imshow("masked1",weird_shape)
masked2=cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow("Weird shaped Masked image",masked2)




cv.waitKey(0)