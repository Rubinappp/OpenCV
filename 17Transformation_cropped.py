import cv2 as cv
import numpy as np
img=cv.imread('Photos/images.jpg')
cv.imshow("cat",img)
#cropped
crop=img[:60,:100]
cv.imshow("cat",crop)
cv.waitKey(0)