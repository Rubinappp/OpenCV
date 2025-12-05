#flip = reflection
import cv2 as cv
import numpy as np
img=cv.imread('Photos/images.jpg')
cv.imshow("cat",img)
flip=cv.flip(img,0)# flipcode: 0= flip vertically /1=flip horozontally/-1 = flip both
cv.imshow("flip",flip) 



cv.waitKey(0)