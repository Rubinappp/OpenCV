#Basic information Transformation
#translation,rotation,resizing,flipping,cropping

# 1.Translation
# Translation = moving every pixel in the image by some amount:(right/left,Up/down)

import cv2 as cv
import numpy as np
img=cv.imread('Photos/images.jpg')

cv.imshow("cat",img)
#Translation
def translate(img,tx,ty):
    transMat= np.float32([[1,0,tx],[0,1,ty]]) # 2D matrix converted into float since result might have decimal number
    dimension=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension)
translated=translate(img,-100,-100) # shifted left and down by 100 pixels
cv.imshow('trans_img',translated)
cv.waitKey(0)

#computer graphics
# (0,0) ─────────► x
#    │
#    │
#    ▼ y

# | Value    | Effect on image |
# | -------- | --------------- |
# | `tx > 0` | Move **right**  |
# | `tx < 0` | Move **left**   |
# | `ty > 0` | Move **down**   |
# | `ty < 0` | Move **up**     |



# computers transform images using a general formula called an affine transform:
#  |x′|  |x|
#  |y′​|=A|y|⋅ +b  
# Where:

# A = 2×2 matrix (rotation, scaling, shear)
# b = 2×1 vector (translation)

#For translation:

# A = identity matrix

# b = shift amounts (tₓ, tᵧ)
#  |x′| |1 0| |x|    |tx|
#  |y′​|=|0 1| |y| +  |ty|

#Simplification:x′=x+tx​,y′=y+ty​

# But
# OpenCV wants a single matrix combining A and b.

# So it merges them into a 2×3 matrix:
#  |x′| |1 0 tx|
#  |y′​|=|0 1 ty|

