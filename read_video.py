# A video is just a sequence of images (frames) shown quickly.

# Each pixel is like a tiny square in your image grid.

# Inside that pixel, OpenCV stores intensity values for each channel.



import cv2 as cv
capture=cv.VideoCapture('Videos/dog.mp4') # it will take int or '' 0 for web cam, 1 for 1st camera connected to computer 2 reference to second camera
# capture is just an instance 

while True:
    isTrue,frame= capture.read() 
    cv.imshow('Video',frame) #(name of window,display current frame)
    # will read video frame by frame
    # frame is the actual image as a NumPy array which has has pixels, height, width, and color channels (RGB/BGR).
    
    if cv.waitKey(20)& 0xFF == ord('q'):#Waits 20 milliseconds between frames,stop the video if you press q
        break

capture.release()
cv.destroyAllWindows()



#After video is finished open cv cannot find any more frame and break out of loop raising assertion error 





