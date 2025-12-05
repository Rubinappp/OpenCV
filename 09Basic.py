#Basic Functions

import cv2 as cv
img=cv.imread('Photos\images.jpg') # this is bgr image
cv.imshow('Cat',img)

#Converting bgr image to grayscale( color conversion function)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT) 
#ksize=the area of neighboring pixels used to compute the blur.
# Kernel size MUST be odd numbers 
#(3,3) → a 3×3 matrix light blur

# x x x    # 8 (x )neighbours that calculate blur (0)
# x O x
# x x x

# (5,5) → a 5×5 matrix
# (7,7) → a 7×7 matrix strong blur

#cv.BORDER_DEFAULT = reflection padding
# It creates imaginary pixels outside by reflecting the border:| 3 4 5 | 5 4 3
#This gives smooth blur near edges.


cv.imshow('Blur',blur)

cv.waitKey(0)


