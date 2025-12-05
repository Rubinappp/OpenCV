import cv2 as cv
img=cv.imread('Photos\images.jpg') # this is bgr image
cv.imshow('Cat',img)

#Edge Cascade
canny=cv.Canny(img,125,175)
cv.imshow('Edge',canny)

#For reducing edge we can pass blur image to canny
#Blur → remove noise → clean edges
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT) 
canny=cv.Canny(blur,125,175) # greater than thresold 2 keep it/ less than thresold 1 discard. im between keep if connected to thresold2
cv.imshow('BlurEdge',canny)
cv.waitKey(0)
#Edge is boundary (where pixel intensity changes sharply)
cv.Canny(img,)

#In images, gradient = how quickly brightness changes from one pixel to the next.
#10, 12, 13, 15, 80, 82, 85
# Between 15 → 80:
# The change is HUGE → gradient is high → edge.
# Between 10 → 12:
# Small change → gradient is low → smooth region.


#how canny works 
# If gradient < threshold1 → ignore

# Too small → probably noise.

# If gradient > threshold2 → strong edge

# Definitely an edge.

# If between threshold1 and threshold2 → weak edge

# Only kept if connected to a strong edge.

#General rule
# Upper threshold ≈ 2–3 × lower threshold