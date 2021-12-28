import cv2
import numpy as np

img_file='data/images/sample.jpg'

# open cv로 이미지 열기 - 칼라이미지(BGR)
image = cv2.imread(img_file,cv2.IMREAD_COLOR) # => 안 써도 디폴트 파라미터는 칼라로 가져옴

# 이미지가 정상인지 체크하는 코드
if image is None:
    print('이미지 파일을 열 수 없습니다.')
else:
    print(image.shape) 

# 이미지를 그레이 스케일로 바꾸기
gray_img= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('color',gray_img)

# 위의 imshow 함수는 화면에 표시하는 함수인데
# 실행되었다가 바로 종료

# 따라서 우리눈으로 확인하기 위해서는 cpu의 코드실행을 잠시 멈춘다.
cv2.waitKey(0)
cv2.destroyAllWindows()