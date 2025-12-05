import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)

#Draw Circle
cv.circle(blank,(255,255),40,(0,0,255),thickness=-1) # center,radius,bgr
cv.imshow('Circle',blank)

cv.waitKey(0)
