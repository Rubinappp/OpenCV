import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np
img=cv.imread("Photos\images.jpg")
cv.imshow("Cats",img)

colors=("b","g","r")
# for i,col in enumerate(colors): # enumerate adds iteration(col)
#     hist=cv.calcHist([img],[i],None,[256],[0,256]) 
#     plt.title("Color Histogram")
#     plt.xlabel('Bins')
#     plt.ylabel("No of pixels")
#     plt.plot(hist)
#     plt.xlim([0,256])

# plt.show()

# we can also try this for masked image 

blank=np.zeros((img.shape[:2]),dtype='uint8')
rect=cv.rectangle(blank,(0,0),(150,150),255,-1)
mask=cv.bitwise_and(img,img,mask=rect)
cv.imshow("masked",mask)
for i,col in enumerate(colors): # enumerate adds iteration(col)
    hist=cv.calcHist([img],[i],None,[256],[0,256]) 
    plt.title("Color Histogram")
    plt.xlabel('Bins')
    plt.ylabel("No of pixels")
    plt.plot(hist)
    plt.xlim([0,256])

plt.show()
