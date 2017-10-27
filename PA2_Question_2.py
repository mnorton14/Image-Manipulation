import numpy as np
import cv2

base = cv2.imread('Butterfly.jpg', 0)
img1 = cv2.imread('Butterfly.jpg', 1)
cv2.imshow('Butterfly', img1)

row,col = base.shape
height, width = row*col, 5
feature = [[0 for x in range(width)] for y in range(height)]
x = 0
y = 0
#Creates the feature vector matrix with x,y coordinates as the last two entries
for i in range(height):   
    if(y == col):
        y = 0
        x+=1  
    img = img1[x,y]
    feature[i][0] = img[0]
    feature[i][1] = img[1]
    feature[i][2] = img[2]
    feature[i][3] = x
    feature[i][4] = y
    y+=1   

#h and iter values   
h = 10
iter = 30
       
print feature

#Sets Key to Close Windows to '0'
cv2.waitKey(0)
cv2.destroyAllWindows()



#Sets Key to Close Windows to '0'
cv2.waitKey(0)
cv2.destroyAllWindows()