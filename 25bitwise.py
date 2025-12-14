#AND,OR,XOR,NOT
import cv2 as cv
import numpy as np
blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)#this is a binary image so give only 1 color white
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow("rectangle",rectangle)
cv.imshow("circle",circle)

#bitwise AND -- intersection
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow("bitwiseAnd",bitwise_and)

#bitwise Or -- non intersecting+intersecting region
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow("bitwiseOR",bitwise_or)

#bitwise xor -- non intersecting regions
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow("bitwisexor",bitwise_xor)

#bitwise NOT -- 
bitwise_not=cv.bitwise_not(rectangle) # convert white to black and black to white
cv.imshow("RNOT",bitwise_not)

bitwise_not=cv.bitwise_not(circle) # convert white to black and black to white
cv.imshow("CNOT",bitwise_not)

cv.waitKey(0)

#blank.copy to work on different pages