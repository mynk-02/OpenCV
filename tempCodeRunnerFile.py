capture = cv.VideoCapture('Videos/video1.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,0.2)
    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
