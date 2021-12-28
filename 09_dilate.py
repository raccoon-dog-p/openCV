import cv2

image = cv2.imread('data/images/truth.png')

cv2.imshow('..',image)

# 이미지 확장

dilationSize = 6

element = cv2.getStructuringElement(cv2.MORPH_RECT,(2*dilationSize,2*dilationSize))

imageDilate= cv2.dilate(image,element)

cv2.imshow('qq',imageDilate)

cv2.waitKey(0)
cv2.destroyAllWindows