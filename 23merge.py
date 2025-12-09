import cv2 as cv
import numpy as np
img=cv.imread('Photos\images.jpg')
blank=np.zeros((img.shape[:2]),dtype='uint8')# blank is 2D not a colored image so give (height,width)only
print(blank)
b,g,r= cv.split(img)

blue=cv.merge([b,blank,blank]) 
# we combine 3 single channel here. 
# all three arrays must have exactly same shape and same no of color channel to get merged
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

merged=cv.merge([b,g,r])
cv.imshow("merge",merged)
cv.waitKey(0)

# Suppose Channel,Value in original image (BGR order)
# Blue,20   (very little blue)
# Green,50   (some green)
# Red,230  (very strong red)
# So actual pixel in memory after cv2.imread(): [20, 50, 230]

# After this .blue_image = cv2.merge([b, blank, blank])
# That same pixel in blue_image becomes: [20, 0, 0]










