import cv2 as cv
img=cv.imread('Photos/images_large.jpg')
cv.imshow('Cat',img) # name ,pixel which is in img
cv.waitKey(0)

# For a color image (RGB/BGR):
#print(img.shape)
# Example output: (480, 640, 3)

# 480 → height (number of rows)

# 640 → width (number of columns)

# 3 → number of color channels (B, G, R in OpenCV) -> total_pixels = 480 * 640 = 307200 pixels
# For a grayscale image:Only height and width — no color channels.


# open cv doesnt have anything to deal with images far greater than computer screen
# large image will go offsquare