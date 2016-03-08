import cv2
import numpy as np



wat = cv2.imread('123.jpg',1)
x = wat[20:400,30:400]

cv2.imshow('im',x)
cv2.waitKey(0)
cv2.destroyAllWindows()

