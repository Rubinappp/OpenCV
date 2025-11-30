# resize and resize will prevent computational strength
# we will get rid of some info
# rescale means to change width and height to smaller value than original

import cv2 as cv

# img=cv.imread('Photos\images.jpg')

# cv.imshow('big',img)


def rescaleFrame(frame,scale=0.75):
    # works for Images,video,Live video 
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
# def changeRes(width,height)


# rescale_img=rescaleFrame(img)
# cv.imshow('resize',rescale_img)

capture=cv.VideoCapture('Videos\dog.mp4')

while True: 
    
    isTrue,frame=capture.read()
    scaled_frame=rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Scaled',scaled_frame)

    if cv.waitKey(20)& 0XFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows()