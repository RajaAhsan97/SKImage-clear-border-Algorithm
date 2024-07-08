"""
    MATLAB imreconstruct method
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

LP = cv.imread('LP.jpg')
LP_gray = cv.threshold(cv.cvtColor(LP, cv.COLOR_BGR2GRAY), 240, 255, cv.THRESH_BINARY, cv.THRESH_OTSU)[1]
(h, w, c) = LP.shape


# creating marker at the borders of image
marker = np.zeros((h,w), dtype=np.uint8)
for j in range(h):
    for k in range(w):
        if j == h-1 or k == w-1 or j == 0 or k == 0:
            marker[j,k] = LP_gray[j,k]

# create morphological dilation operation kernel
kernel = np.ones((5,5), dtype=np.uint8)

iteration = 0
while True:
    # dilating marker
    expanded = cv.dilate(marker, kernel)
    # masking the dilated image using bitwise_and operation 
    cv.bitwise_and(expanded, LP_gray, expanded)

    if (marker == expanded).all():
        break
    marker = expanded
    iteration += 1

# differnce the dirated image with the original image to remove border
out = LP_gray - expanded

fig, ax = plt.subplots(nrows=1, ncols=4)

ax[0].imshow(LP_gray)
ax[1].imshow(marker)
ax[2].imshow(expanded)
ax[3].imshow(out)
plt.show()
