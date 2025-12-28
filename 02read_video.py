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

# 1. cv.waitKey() returns a 32-bit integer (or sometimes 16-bit depending on platform).

# 2. The actual key pressed is stored in the last 8 bits.

# 3. 0xFF is 11111111 in binary, so doing cv.waitKey() & 0xFF keeps only the last 8 bits.

#Suppose 

# Raw cv.waitkey: 33185 → binary: 1000 0000 1100 0001 (16 bits)

# Mask: 0xFF → binary: 0000 0000 1111 1111

#   1000 0000 1100 0001
# & 0000 0000 1111 1111
# ----------------------
#   0000 0000 1100 0001

# 4. we compare it with ord('q') (or any character) to detect if that key was pressed.
#cv.waitKey(50)&0xFF == ord('q') If key is q → loop breaks → video stops 
# If key is not pressed → loop continues → next frame is read and displayed
#After video is finished open cv cannot find any more frame and break out of loop raising assertion error 

