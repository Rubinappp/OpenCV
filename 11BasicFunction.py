import cv2 as cv
img=cv.imread('Photos\images.jpg') # this is bgr image
cv.imshow('Cat',img)

blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT) 
canny=cv.Canny(blur,125,175) # greater than thresold 2 keep it/ less than thresold 1 discard. im between keep if connected to thresold2
cv.imshow('CannyEdge',canny)

#Dilatng the  image
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilation',dilated)


# Dilation expands the white pixels outward.(Thicken the edge)
#Each white pixel grows outward once according to the kernel size.
#iterations multiply the effect of the kernel size.
# To connect broken edges in larger gaps.
# Let’s say kernel is (7,7) and iterations=1 → edges expand roughly 3 pixels outward (half of kernel size)

# iterations=2 → expand roughly 6 pixels outward

# iterations=3 → ~9 pixels outward

# Erosion 
# shrinks the white areas in a binary image (Thinning the edge)
eroded= cv.erode(dilated,(3,3),iterations=2)
cv.imshow('Erode',eroded)



cv.waitKey(0)