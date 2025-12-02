import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8') # width,height,channel np.zeros(...) → initializes all pixel values to 0
cv.imshow('blank',blank) # blank image 
print(blank.shape)
# 1.  paint blank image in certian color

blank[:]=0,255,0
cv.imshow('Green',blank)

blank[200:300, 300:400]=255,0,0
cv.imshow('blue',blank)

cv.waitKey(0) # pause wait for key to be pressed 


