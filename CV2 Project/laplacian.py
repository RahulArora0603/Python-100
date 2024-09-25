import cv2 as cv 
import numpy as np
video = cv.VideoCapture(0)

while True:
    _,frame = video.read()

    laplasian = cv.Laplacian(frame,cv.CV_64F)
    laplasian = np.uint8(laplasian)
    cv.imshow('laplacian',laplasian)


    if cv.waitKey(5)==ord('x'):
        break

video.release()
cv.destroyAllWindows()