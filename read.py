import cv2 as cv

# img = cv.imread('Bible Page Data/proverbs_12.jpeg')
# cv.imshow('Proverbs 12', img)

# Reading Videos
capture = cv.VideoCapture('Videos/acadia_walking.mov')

if not capture.isOpened():
    print("Cannot open camera")
    exit()

while True:
    isTrue, frame = capture.read()
    cv.imshow('Walking', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()