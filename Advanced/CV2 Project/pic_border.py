import cv2 as cv

img = cv.imread('CV2 Project\Mypic.png')
height, width = img.shape[:2]
print(height, width)

cv.line(img, (2,0),(2,355),(0, 0,120),4)
cv.line(img, (2,0),(266,0),(0, 0,120),4)
cv.line(img, (0,355),(266,355),(0, 0, 120),4)
cv.line(img, (266,0),(266,355),(0, 0,120),4)


cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()