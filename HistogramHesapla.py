import cv2
import numpy as np
from matplotlib import pyplot as plt

normal = cv2.imread("manzara.jpg")
cv2.imshow("denemeiki",normal)

image_high = normal.shape[0]    #okunan değerin yükseklik ve genişligini bulduk (yani resmin x ve y kordinatları arasında kalan piksel sayısı)
image_width = normal.shape[1]

his=np.zeros([265])    #dizi boyutu olusturmak için kullandık

for i in range(0,image_high):
    for j in range(0,image_width):
        his[normal[i,j]]+=1

plt.plot(his)
plt.show()
