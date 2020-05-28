#This method uses inbuilt method known as CANNY EDGE DETECTION
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('messi.jpg',0)
canny=cv2.Canny(img,200,400)
titles=['image','canny']
images=[img,canny]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
