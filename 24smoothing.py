import cv2 as cv
img=cv.imread("Photos\images.jpg")
cv.imshow("image",img)

#blur=average of neighbouring  pixel
blur=cv.blur(img,(3,3))
cv.imshow("blur",blur)

#gaussian blur=average of weight assigned to neighbouring pxel
#Gives less blurring than blur method .But looks more natural than blur method
gblur=cv.GaussianBlur(img,(3,3),0) #sigma x =standard deviation
cv.imshow("gblur",gblur)

#Median blur= instead of average find median
# more effective in reducing noise than averaging and gaussian blur 
mblur=cv.medianBlur(img,3)
cv.imshow("medianBlur",mblur)

#Bilateral blur= most effective 
# used in a lot of advanced computer vision projects
# blur by retainingedges of image

bilateral=cv.bilateralFilter(img,10,35,25) # diameter(Neighborhood size),sigma color,sigma space
cv.imshow("bilateral",bilateral)
# diameter= its like kernel fix size to calculate center
#sigma color=how much intensity difference is allowed
#If two pixels differ by less than ~35 in brightness/color, they are considered “similar” so will get high weight and will be smoothed together.
# if greater than that intensity difference will get less weight and edge will preserved.

#sigmaspace= distance radius how far to look at
cv.waitKey(0)