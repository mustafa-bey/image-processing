import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
normal = cv2.imread("manzara.jpg")
cv2.imshow("denemeiki",normal)


gri = cv2.imread("manzara.jpg",0)
cv2.imshow("deneme",gri)
hist_gray = cv2.calcHist([gri],[0],None,[256],[0,256])

plt.figure(2)
plt.plot(hist_gray)
plt.show()

CM = (np.max(gri) - np.min(gri)/ np.max(gri) + np.min(gri))
new_image = CM*gri

plt.imshow(new_image,cmap='gray')
plt.show()


"""

deneme =[2,3,4,5],[5,6,89,9],[1,1,2,4],[65,234,45,77]
normal = cv2.imread(deneme)
cv2.imshow("deneme_matrıs",normal)
