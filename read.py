import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    #images, videos, live videos

    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_LINEAR)

#def changeRes(width,height):
    #live videos
    capture.set(3,width)
    capture.set(4,height)


#Reading Image
img = cv.imread("Images/cat.jpg")
cv.imshow("Cat", img)

frame = rescaleFrame(img, 4)
cv.imshow("Resized Cat", frame)
cv.waitKey(0)

#Reading Video
"""capture = cv.VideoCapture('Videos/video1.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,0.2)
    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
"""