import cv2 as cv

img = cv.imread("OpenCV/Images/cat.jpg")
cv.imshow("Cat", img)

# 1. Convert to gray scale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("Gray", gray)

# 2. Blur
blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 3. edge cascade
canny = cv.Canny(blur, 125,175)
cv.imshow('canny edges', canny)

# 4. Dilating the image
dilated = cv.dilate(canny,(3,3), iterations=1)
cv.imshow("dilated", dilated)

# 5. Eroded
eroded = cv.eroded(dilated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

cv.waitKey(0)