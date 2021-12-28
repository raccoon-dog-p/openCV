import cv2
import numpy as np

source = cv2.imread('data/images/sample.jpg',1)

scalingFactor = 1/255.0

# 0~255로 되어있는 이미지를 0~1사이의 실수로 정규화

source = source * scalingFactor
print(source)

# 반대로 0~255 로 정수화

# source = source * 255
# print(source)

# 위의 코드는 실수 이므로 이미지가 아니다
# 따라서 다시 이미지 배열로 만드려면, 데이터 타입을 변경해주어야 한다

#1. np.uint8(source)
# print(np.uint8(source))

#2. source.astype('uint8')
souerce = source.astype('uint8')