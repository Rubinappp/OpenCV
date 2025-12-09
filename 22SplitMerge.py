import cv2 as cv
import numpy as np
#open cv allows us to split the colorcode like bgr into different channel b,g,r
img=cv.imread('Photos\images.jpg')
cv.imshow("image",img)

b,g,r= cv.split(img)
cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)

print(img.shape)
print(b.shape) # it won't show color channel which is one. since grayscale has 1 color channel so img is displayed in grayscale
print(g.shape)
print(r.shape)

# images are displayed in grayscale which shows distribution of pixel intensity
# lighter region shows more concentratipn of that pixel values
#Darker region shows less or no pixel in that region 

merged=cv.merge([b,g,r])
cv.imshow("merge",merged)
cv.waitKey(0)