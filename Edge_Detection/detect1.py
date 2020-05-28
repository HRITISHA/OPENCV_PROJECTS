# In this IMAGE GRADIENT has been used.
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("messi.jpg", cv2.IMREAD_GRAYSCALE)
lap=cv2.Laplacian(img,cv2.CV_64F,)
lap=np.uint8(np.abs(lap))
img1=cv2.imread("sudoku.jpg", cv2.IMREAD_GRAYSCALE)
sobelx=cv2.Sobel(img1,cv2.CV_64F,1,0)
sobely=cv2.Sobel(img1,cv2.CV_64F,0,1)

sobelx=np.uint8(np.abs(sobelx))
sobely=np.uint8(np.abs(sobely))
sobelcomb=cv2.bitwise_or(sobelx,sobely)

titles=['image1','Laplacian','image2','sobelx','sobely','sobelcombined']

images=[img,lap,img1,sobelx,sobely,sobelcomb]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()