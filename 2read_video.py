# A video is just a sequence of images (frames) shown quickly.
# frame is the actual image as a NumPy array which has has pixels, height, width, and color channels (RGB/BGR).
    
# Each pixel is like a tiny square in your image grid.

# Inside that pixel, OpenCV stores intensity values for each channel.



import cv2 as cv
capture=cv.VideoCapture('Videos/dog.mp4') # it will take int or '' 0 for web cam, 1 for 1st camera connected to computer 2 reference to second camera
# capture is just an instance 

while True:
    isTrue,frame= capture.read() # # read the next frame
    cv.imshow('Video',frame) #(name of window,display that frame)
    
   
    if cv.waitKey(50)& 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows() # closes the OpenCV window


# waitKey(20) → pauses the program for 20 ms and checks if a key is pressed→ returns its ASCII code. 
# 0xFF == ord('q') If key is q → loop breaks → video stops 
#If key is not pressed → loop continues → next frame is read and displayed

#After video is finished open cv cannot find any more frame and break out of loop raising assertion error 





