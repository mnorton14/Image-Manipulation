import numpy as np
import cv2
 
base = cv2.imread('disp1.png', 0)
img1 = cv2.imread('disp1.png', 1)
img2 = cv2.imread('disp5.png', 1)
img3 = cv2.imread('view1.png', 1)
img4 = cv2.imread('view3.png', 1)
img5 = cv2.imread('view5.png', 1)

cv2.imshow('Disp 1', img1)
cv2.imshow('Disp 5', img2)
cv2.imshow('View 1', img3)
cv2.imshow('View 3', img4)
cv2.imshow('View 5', img5)

row, col = base.shape
newView = []
newView = np.zeros_like(img1)
for i in range(row):    #add row back in
    dist = 0
    for j in range(col-1): #col-1
        for k in range(col-1): #col-1
            d1p0 = img1[i,j-1]
            d1p1 = img1[i,j]
            d1p2 = img1[i,j + 1]            
            d2p0 = img2[i,k-1]
            d2p1 = img2[i,k]
            d2p2 = img2[i,k + 1]
            #Finds same edges in both images and produces the middle view of those edges    
            if(d1p1[1] != d1p2[1] and d2p1[1] != d2p2[1] and d1p1[1] == d2p1[1] and d1p2[1] == d2p2[1]):
                dist = (k-j)/2
                if(dist%2 != 0):
                    dist-=1
                newView[i,j+dist] = d1p1
                newView[i,j+dist+1] = d1p2     
       #if prev or next = 0 and current doesnt then make nexxt equal to current
                #go from left and from right sides
        #loop through new view and forget the other two
for i in range(row):
    for j in range(col-1):
        pixCheck = newView[i,j]
        d1p0 = newView[i,j+1]
        if(pixCheck[1] == 0 and d1p0[1] != 0):
            newView[i,j] = d1p0
                  
cv2.imshow('Disp 3', newView)        
cv2.imwrite('Disp3.png', newView)
#Sets Key to Close Windows to '0'
cv2.waitKey(0)
cv2.destroyAllWindows()