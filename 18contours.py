
import cv2 as cv
import numpy as np

img=cv.imread('Photos/images.jpg')
cv.imshow("cat",img)

img1=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("img1",img1)

blur=cv.GaussianBlur(img1,(7,7),cv.BORDER_DEFAULT) # just by bluring no of contour is reduced 
cv.imshow("bLUR",blur)

edge=cv.Canny(blur,150,250)
cv.imshow('Edge',edge)

contours,heirarchy=cv.findContours(edge,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv.waitKey(0)

#cv.RETR_LIST =Find ALL contours (outer + inner + everything) no heirarchy will treat every shape equally
#cv.CHAIN_APPROX_SIMPLE=Compress contour → keeps the essential points instead of every single pixel along the edge in memory
# (mainly for memory efficiency)


# cv.CHAIN_APPROX_NONE =store every pixel along the edge,