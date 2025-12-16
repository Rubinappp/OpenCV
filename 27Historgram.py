import cv2 as cv
import matplotlib.pyplot as plt 
img=cv.imread("Photos\images.jpg")
cv.imshow("Cats",img)


gray=cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#GrayScale histogram
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256]) # channel here is index and we have only 1 gray so 0 index
#channel,mask,bins,intensity range

plt.figure ()
plt.title("Gray scale Histogram")
plt.xlabel('Bins')
plt.ylabel("No of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)