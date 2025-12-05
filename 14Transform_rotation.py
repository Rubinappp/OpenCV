import cv2 as cv
import numpy as np
img=cv.imread('Photos/images.jpg')
cv.imshow("cat",img)
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0) 
    # center point,degree of rotation, scaling for zoom in or out . 1.0 is original size., > 1.0 → zoom in, < 1.0 → shrink
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,45)  # rotate anticlockwise
cv.imshow("rotated",rotated)


rotated_rotate=rotate(rotated,45) 
# final image doesn’t look like a perfect 90° rotation since previously there were black pixels introduced around which will distort the shape 
# so needs to rotate original pic by 90 if needed.
cv.imshow('rotated_rotate',rotated_rotate)

rotated1=rotate(img,90)
cv.imshow('rotate1',rotated1)


rotate_clockwise=rotate(img,-45)
cv.imshow("rotate_clockwise",rotate_clockwise)
cv.waitKey(0)