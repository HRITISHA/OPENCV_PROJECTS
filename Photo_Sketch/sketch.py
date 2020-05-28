import cv2
import numpy as np
import matplotlib.pyplot as plt
def sobel (img):
	opImgx		= cv2.Sobel(img,cv2.CV_8U,0,1)	#detects horizontal edges
	opImgy		= cv2.Sobel(img,cv2.CV_8U,1,0)	#detects vertical edges
	#combine both edges
	return cv2.bitwise_or(opImgx,opImgy)
img=cv2.imread('girl.jpg',0)

gblur=cv2.GaussianBlur(img,(3,3),0)
inverted_img = 255-gblur
edgImg0		= sobel(gblur)
edgImg1		= sobel(inverted_img)
edgImg		= cv2.addWeighted(edgImg0,1,edgImg1,1,0)	#different weights can be tried too
	
	#Invert the image back
opImg				= 255-edgImg

titles=['image','Guassian blur','Sketch']

images=[img, gblur,opImg]
for i in range(3):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
