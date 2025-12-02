import cv2 as cv
img=cv.imread('Photos\images.jpg') # this is bgr image
cv.imshow('Cat',img)

#resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resize',resized)


#Cropping
cropped=img[50:200,10:400] # row=height,columns=width
cv.imshow('Cropped',cropped)
#cubic is much slower but resultant image is of higher quality
cv.waitKey(0)