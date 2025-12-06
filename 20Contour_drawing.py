#Draw contour to look what its like

# recommended canny before contour not thresold 

import cv2 as cv
import numpy as np
img=cv.imread('Photos\images.jpg')
cv.imshow("image",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

canny=cv.Canny(gray,125,175)
cv.imshow("Canny",canny)

contours,heirarchy=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

#Drawing contour on blank image
Blank=np.zeros((img.shape),dtype='uint8')
cv.imshow("blank",Blank)

cv.drawContours(Blank,contours,-1,(255,0,0),thickness=1) # contour_index=-1 represent we want all contours
cv.imshow('Contour',Blank)

cv.waitKey(0)