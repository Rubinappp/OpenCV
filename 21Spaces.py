#color space ->representing an array of pixel of colors. rgb,grayscale,hsv
#python -m pip install matplotlib tp install matplotlib 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('Photos\images.jpg')
cv.imshow("image",img)
# Default open cv read image in bgr format

#If we try to display this bgr image using matplotlib it will display in rgb format
plt.imshow(img)
plt.show() # we see inversion of color

#BGR TO GrayScale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#BGR to HSV
hSV=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hSV)

#BGR to l*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)

#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)

#we can also convert other color hsv,lab,gray to bgr..
# But we cannot convert hsv to lab or lab to hsv and so on.we need to convert first into bgr .

#HSV to BGR 
hsv_bgr=cv.cvtColor(hSV,cv.COLOR_HSV2BGR)
cv.imshow("bgr",hsv_bgr)


cv.waitKey(0)