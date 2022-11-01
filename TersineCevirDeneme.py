import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
image = Image.open('resim.jpg')        #normal görüntüyü tersine çevirme
im_invert = ImageOps.invert(image)
im_invert.save('data/dst/lena_invert.jpg', quality=95)

"""

normal = cv2.imread("resim.jpg")                           #resim 400x400 oldugu için piksel oranı belirli
cv2.imshow("el",normal)

print(normal)


matris = [],[]
for i in range(400):                                      # görüntü tüm elemanlarını bir dizide tutmak için kullan
    for j in range(400):
        matris[i][j]=normal


a = max(matris)                                           #matrisin en büyük degerini bir değiskene atar

for i in range(400):                                      # burada göruntuyu tersine çevirme işleminı gerçekleştirdik
    for j in range(400):
        matris[i][j]=matris[i][j] - a


invert = matris                                           #burada matrisi resim olarak okumaya calıstık
cv2.imshow("ters_gorontu",invert)


#gray = cv2.imread("resim.jpg",0)                         #burası gereksiz kullanmasan da olur
#cv2.imshow("gri_el",gray)


deneme =[2,3,4,5],[5,6,89,9],[1,1,2,4],[65,234,45,77]
cv2.imshow("deneme",deneme)


cv2.waitKey(0)
cv2.destroyAllWindows()
