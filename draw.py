import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow("Blank", blank)

#1. Paint the image a certain number
#blank[:] = 0,255,0 #green
#blank[:] = 0,0,255 #red
#blank[:] = 255,0,0 #blue

#blank[200:300, 300:400] = 0,0,255
#cv.imshow("Bg Colour", blank)

#2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2),(0,255,0), thickness=-1)
cv.imshow("Rectangle", blank)

#3. Draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40,(0,0,255), thickness=-1)
cv.imshow("Circle", blank)

#4. Draw a Line
cv.line(blank, (100,100), (blank.shape[1]//2,blank.shape[0]//2), (255,0,0),  thickness=2)
cv.imshow("Line", blank)

#5. Write text
cv.putText(blank, 'Hello my name is Mayank', (100,400),cv.FONT_HERSHEY_COMPLEX, 0.75, (0,255,0), 2)
cv.imshow("Text", blank)


cv.waitKey(0)