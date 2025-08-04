import cv2 as cv

img = cv.imread('Bible Page Data/proverbs_27.jpeg')
cv.imshow('Proverbs 27', img)

# Converting to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Greyscale', gray)

cv.waitKey(0)