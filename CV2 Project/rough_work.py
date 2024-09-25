import cv2
import numpy as np
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter('output.mp4', fourcc, 23.976, (640, 480), isColor=False)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        edges = cv2.Canny(frame, 50, 100)
        edges = cv2.resize(edges, (640, 480))
        out.write(edges)
        cv2.imshow('frame', edges)
        if cv2.waitKey(5)==ord('x'): #closes when 'x' is pressed on keyboard
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()