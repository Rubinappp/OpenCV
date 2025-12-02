import cv2 as cv
img=cv.imread('Photos/images_large.jpg')


cv.imshow('Cat',img) # name ,pixel which is in img

print(img.shape)
print(img) # gives numpy array of pixel value in each row
print(f"First row img : {img[0]}") 
print(f"First pixel(first row,column):{img[0,0]}") # first row,first column



cv.waitKey(0) # pause image until key is pressed


# open cv doesnt have anything to deal with images far greater than computer screen
# large image will go offsquare


# For a color image (RGB/BGR):
#print(img.shape)
# Example output: (2404, 1600, 3)

# 2404 → height (number of rows)

# 1600 → width (number of columns)

# 3 → number of color channels (B, G, R in OpenCV) -> total_pixels = 480 * 640 = 307200 pixels


# For a grayscale image:Only height and width — no color channels.


#img
# [[[197 194 186]
#   [197 194 186]
#   [197 194 186]
#   ...
#   [196 193 185]
#   [196 193 185]
#   [196 193 185]]  <- first row of pixels
#  [[197 194 186]
#   [197 194 186]
#   [197 194 186]
#   ...
#   [196 193 185]
#   [196 193 185]
#   [196 193 185]]  <- second row of pixels
#  [[197 194 186]
#   [197 194 186]
#   [197 194 186]
#   ...



