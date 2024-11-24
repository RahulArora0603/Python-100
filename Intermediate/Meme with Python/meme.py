import cv2

img = cv2.imread('Meme with Python/download.png')
print(img.shape[:2])
color=(255,255,255)
fontScale = 1
font= cv2.FONT_HERSHEY_SIMPLEX
thickness=2
lineType=cv2.LINE_AA

img = cv2.putText(img, "Why did the programmer", (80,170),font, fontScale,color, thickness,lineType)
img = cv2.putText(img, 'quit his job?', (80,200), font, fontScale,color, thickness,lineType)
img = cv2.putText(img, 'Why?', (60,340), font, fontScale,color, thickness,lineType)
img = cv2.putText(img, 'Because he didnt', (200,330), font, fontScale,color, thickness,lineType)
img = cv2.putText(img, 'get arrays', (200,360), font, fontScale,color, thickness,lineType)
img = cv2.putText(img, '[.....]', (200,590), font, fontScale,color, thickness,lineType)

cv2.imwrite('meme.png', img)


