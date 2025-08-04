import cv2 as cv

img = cv.imread('Bible Page Data/proverbs_27.jpeg')
cv.imshow('Proverbs 27', img)

# Converting to greyscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Greyscale', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dialated Edges', dilated)

# Eroding an image
# eroding = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded Edges', eroding)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[0:250, 0:500]
cv.imshow('Cropped', cropped)
cv.waitKey(0)