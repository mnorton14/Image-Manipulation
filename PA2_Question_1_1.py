import numpy as np
import cv2
 
#base = cv2.imread('disp1.png', 0)
base = cv2.imread('view1.png',0)
img1 = cv2.imread('disp1.png', 1)
img2 = cv2.imread('disp5.png', 1)
img3 = cv2.imread('view1.png', 0)
img4 = cv2.imread('view3.png', 1)
img5 = cv2.imread('view5.png', 0)

img3 = np.pad(img3,1, 'constant')
img5 = np.pad(img5,1, 'constant')

newImg1 = np.zeros_like(img1)
row, col = base.shape
anchor = []
window = []
print anchor        
print window

for i in range(100):  #row
    SAD = 0
    lowestSAD = 0
    for j in range(col):
        anchor = []
        anchor.append(img3[i-1,j-1])
        anchor.append(img3[i-1,j])
        anchor.append(img3[i-1,j+1])
        anchor.append(img3[i,j-1])
        anchor.append(img3[i,j])
        anchor.append(img3[i,j+1])
        anchor.append(img3[i+1,j-1])
        anchor.append(img3[i+1,j])
        anchor.append(img3[i+1,j+1])
        Asum = np.sum(anchor) 
        
        x,y = 0,0
        for k in range(col):
            window = []
            window.append(img5[i-1,j-1])
            window.append(img5[i-1,j])
            window.append(img5[i-1,j+1])
            window.append(img5[i,j-1])
            window.append(img5[i,j])
            window.append(img5[i,j+1])
            window.append(img5[i+1,j-1])
            window.append(img5[i+1,j])
            window.append(img5[i+1,j+1])
            Wsum = np.sum(window)
            SAD = np.abs(int(Asum) - int(Wsum))
            if(SAD < lowestSAD):
                lowestSAD = SAD
                x = i
                y = k
            SAD = 0
        newImg1[i,j] = img3[x,y]
        
cv2.imshow('disp', newImg1)
cv2.imshow('Disp 1', img1)
cv2.imshow('Disp 5', img2)

#Sets Key to Close Windows to '0'
cv2.waitKey(0)
cv2.destroyAllWindows()