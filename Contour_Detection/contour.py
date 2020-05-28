#CONTOURS are defined as curves joining all the continuous points along the boundary with same colours or intensity.
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('opencv.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img = cv2.resize(img, (400, 500))
# gray = cv2.resize(gray, (400, 500))

ret,thresh=cv2.threshold(gray,127,255,0)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Number of contours= "+str(len(contours)))


cv2.drawContours(img,contours,-1,(0,255,255),1)
cv2.imshow('Image',img)
cv2.imshow('Grayimage',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()