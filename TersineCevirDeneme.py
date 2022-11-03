import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
image = Image.open('resim.jpg')        #normal görüntüyü tersine çevirme
im_invert = ImageOps.invert(image)
im_invert.save('data/dst/lena_invert.jpg', quality=95)

"""

normal = cv2.imread("resim.jpg",0)                           #resim 400x400 oldugu için piksel oranı belirli
cv2.imshow("el",normal)

newM = [k[:] for k in normal]

dup = []
for k in newM:
    for i in k:
        dup.append(i)
#print (max(dup), min(dup))
a = max(dup)

#print(newM)

for i in range(400):
    for j in range(400):
        newM[i][j]= int(newM[i][j]) - a     #burada bir sıkıntı var int() yazmayınca hata alıyorum bu koda bak


plt.plot(newM)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()

