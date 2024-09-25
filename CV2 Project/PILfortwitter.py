import cv2
cv2.namedWindow('Normal Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('GrayScale Image', cv2.WINDOW_NORMAL)

img = cv2.imread('CV2 Project/lake-7316684_1280.jpg')
cv2.imshow('Normal Image',img)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('GrayScale Image', gray_image)
cv2.waitKey(0)

cv2.destroyAllWindows()

