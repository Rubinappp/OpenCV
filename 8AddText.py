import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)
#Write text on image
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_SCRIPT_COMPLEX,1.0,(0,255,0),2)# text,where to put,font,fonr-size,color,thickness
cv.imshow('Text',blank)

cv.waitKey(0)
