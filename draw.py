import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')
# cv.imshow('Blank Image', blank)

img = cv.imread('Photos/isaac.jpeg')
# cv.imshow('Isaac', img)

# Paint the image a certain color
# blank[200:300, 300:400] = 39,242,223
# blank_rgb = cv.cvtColor(blank, cv.COLOR_BGR2RGB)

# Draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=2)
# cv.imshow('Rect', blank)

# # Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255,0,0), thickness=-1)
# cv.imshow('Cirlce', blank)

# # Draw a line
# cv.line(blank, (100,250), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)ß

# Write text
cv.putText(blank, 'Hello, world', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 0.75, (0,255,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)