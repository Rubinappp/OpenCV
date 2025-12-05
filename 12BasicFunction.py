import cv2 as cv
img=cv.imread('Photos\images.jpg') # this is bgr image
cv.imshow('Cat',img)

#resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resize',resized)
#cubic is much slower but resultant image is of higher quality
#INTER_Linear/cubic use for inlarging image ,INTER_Area for shrinking image 
#Cropping
cropped=img[50:200,10:400] # row=height,columns=width
cv.imshow('Cropped',cropped)

cv.waitKey(0)