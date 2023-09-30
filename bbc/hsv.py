import cv2
import numpy as np

hue = 14
saturation = 250

width = 640
height = 480
channels = 3
img = np.zeros((height, width, channels), dtype=np.uint8)

img[:] = cv2.cvtColor(np.array([hue, saturation, saturation], dtype=np.uint8).reshape(1, 1, 3), cv2.COLOR_HSV2BGR)[0, 0]

cv2.imshow('Orange Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
