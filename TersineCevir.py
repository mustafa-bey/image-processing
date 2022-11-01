import cv2
import numpy as np
from matplotlib import pyplot as plt

normal = cv2.imread("manzara.jpg",0)
cv2.imshow("denemeiki",normal)

image_high = normal.shape[0]
image_width = normal.shape[1]

for i in range(0,image_high):
    for j in range(0,image_width):
        normal[i][j]= 255-normal[i][j]

cv2.imshow("tersineCevir",normal)

cv2.waitKey(0)

cv2.destroyAllWindows()
