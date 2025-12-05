
import cv2 as cv

#  for live video
def changeRes(frame,width,height):
    capture.set(3,width)
    capture.set(4,height)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture=cv.VideoCapture(0)


while True: 
    
    isTrue,frame=capture.read()
    scaled_frame=changeRes(frame,640, 480)
   
    cv.imshow('Video',frame)
    cv.imshow('Video Scaled',scaled_frame)

    if cv.waitKey(20)& 0XFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows()