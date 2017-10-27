import numpy as np
import cv2
 
#base = cv2.imread('disp1.png', 0)
img1 = cv2.imread('disp1.png', 0)
img2 = cv2.imread('disp5.png', 0)

cv2.imshow('Disp 1', img1)
cv2.imshow('Disp 5', img2)

OcclusionCost = 20 

row, col = img1.shape 
o1 = np.zeros((row,col))
o2 = np.zeros((row,col))

costMatrix = np.zeros((col,col))
directionMatrix = np.zeros((col,col))

for z in range(0,row):
    for i in range (0,col):
        costMatrix[i,0] = i*OcclusionCost
        costMatrix[0,i] = i*OcclusionCost    
    for i in range(1,col):
        for j in range(1,col):
            min1 = costMatrix [i-1,j-1] + np.abs(img1[z,i] - img2[z,j])
            min2 = costMatrix [i-1,j] + OcclusionCost
            min3 = costMatrix [i,j-1] + OcclusionCost
            costMatrix [i,j] = cmin = min (min1,min2,min3)
            if (min1== cmin):
                directionMatrix [i,j] = 1
            if (min2== cmin):
                directionMatrix [i,j] = 2
            if (min3== cmin):
                directionMatrix [i,j] = 3 
    p = col-1
    q = col-1
    while (p != 0 and q != 0):
        if (directionMatrix[p,q]) == 1:
            o1[z,p] = np.abs(p-q)
            o2[z,q] = np.abs(p-q)
            p = p-1
            q = q-1
            
        elif (directionMatrix[p,q]) == 2:
            o1[z,p] = 0
            o1[z,q] = 0
            p = p-1
            
        elif (directionMatrix[p,q]) == 3:
            o1[z,p] = 0
            o1[z,q] = 0
            q = q-1

cv2.imshow('Disparity Estimation 1',o1/o1.max())
cv2.imshow('Disparity Estimation 2',o2/o2.max())

#Sets Key to Close Windows to '0'
cv2.waitKey(0)
cv2.destroyAllWindows()