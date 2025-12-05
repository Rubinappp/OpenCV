import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8') # width,height,channel np.zeros(...) → initializes all pixel values to 0
cv.imshow('blank',blank) # blank image 

# 2. Draw a rectangle

cv.rectangle(blank,(0,0),(250,250),(255,0,0),thickness=2)
cv.imshow('Rectangle',blank)


cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED) # cv.filled / -1 automatically fill that  rectangle by bgr value
cv.imshow('Rect',blank)

#Alternative instead of using fix width 
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)
cv.imshow('rect1',blank)
# // = floor division produces integer values 
# cannot draw a rectangle at floating positions

cv.waitKey(0) # pause wait for key to be pressed 

