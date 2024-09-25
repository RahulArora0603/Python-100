import cv2 as cv 
import numpy as np
video = cv.VideoCapture(0) #openCv video capture object

while True:
    _,frame = video.read() #read the frames captured by camera

    
    laplasian = cv.Laplacian(frame,cv.CV_64F) #highlight regions of intensity change 
    laplasian = np.uint8(laplasian) 

    edges = cv.Canny(frame,50,100) #edge detection algorithm of opencv
    cv.imshow('Canny',edges)
    print(edges.shape)
    if cv.waitKey(5)==ord('x'): #closes when 'x' is pressed on keyboard
        break

video.release() #stops capturing video
cv.destroyAllWindows() #closes all windows

