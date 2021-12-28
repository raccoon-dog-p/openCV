import cv2

image = cv2.imread('data/images/truth.png')

cv2.imshow('..',image)

# 이미지 침식

erodeSize = 6

element = cv2.getStructuringElement(cv2.MORPH_RECT,(2*erodeSize,2*erodeSize))

imageErode= cv2.erode(image,element)

cv2.imshow('qq',imageErode)

cv2.waitKey(0)
cv2.destroyAllWindows