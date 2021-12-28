import cv2
import numpy as np

image= cv2.imread('data/images/mark.jpg')

cv2.imshow('img',image)

# 선 그리기
image_line = image.copy()


cv2.line(image_line,(322,179),(400,183),(0,0,255),3,cv2.LINE_AA)

cv2.imshow('copy',image_line)

# 원 그리기

image_circle = image.copy()
cv2.circle(image_circle,(350,200),150,(255,0,0),3,cv2.LINE_AA)

cv2.imshow('circle!',image_circle)

# 타원 그리기
image_Ellipse = image.copy()
cv2.ellipse(image_Ellipse,(360,200),(100,170),45,0,360,(0,255,0),2)
cv2.ellipse(image_Ellipse,(360,200),(100,170),135,0,360,(0,0,255),2)


cv2.imshow('ellipse',image_Ellipse)

# 사각형 그리기
image_Rectangle = image.copy()
cv2.rectangle(image_Rectangle,(208,55),(450,355),(150,150,150),3)
cv2.imshow('rectangle',image_Rectangle)
# 글자 넣기
imageText = image.copy()
cv2.putText(imageText,"Loser~",(205,50),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,255,0),2)

cv2.imshow('text',imageText)

cv2.waitKey(0)
cv2.destroyAllWindows()