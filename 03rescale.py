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

# When you resize an image, OpenCV must create new pixels or remove pixels.

# Interpolation = the method OpenCV uses to calculate or estimate those new pixel values.

# Different methods = different quality.

# INTER_AREA = “pixel area relation” interpolation =best method for shrinking
# when an image is scaled down many original pixels get combined into fewer pixels
# INTER_AREA calculates each new pixel value using the area covered by the old pixels by averaging which gives smooth result with no noise



# | Interpolation     | Best For                  | Notes                             |
# | ----------------- | ------------------------- | --------------------------------- |
# | **INTER_AREA**    | **Shrinking (downscale)** | Highest quality for reducing size |
# | **INTER_LINEAR**  | General use               | Default, good quality, fast       |
# | **INTER_CUBIC**   | Upscaling                 | slow but high quality             |
# | **INTER_NEAREST** | Very fast, blocky         | good for masks                    |
