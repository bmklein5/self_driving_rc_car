import cv2
import numpy as np

img = cv2.imread('bbc.png')
height, width, channels = img.shape
left = int(width * 0.35)
right = int(width * 0.65)

mask = np.zeros((height, width), dtype=np.uint8)
mask[:, left:right] = 255
mask_inv = cv2.bitwise_not(mask)
img_masked = cv2.bitwise_and(img, img, mask=mask_inv)
cv2.rectangle(img_masked, (left, 0), (right, height), (0, 0, 0), -1)

cv2.imshow('Final Image', img_masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
