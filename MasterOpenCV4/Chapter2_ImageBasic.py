
import cv2
import numpy as np
from matplotlib import pyplot as plt


## read image
img = cv2.imread('/Users/lucyliu/Documents/GitHub/LearnComputerVision/image/lucyface.png')

## get dimension of the image
dimensions = img.shape # height x width x channels
total_number_of_elements = img.size
image_dtype = img.dtype

## show image
cv2.imshow('original image', img)
cv2.waitKey(1)
plt.imshow(img[:, :, ::-1])
plt.xticks([]), plt.yticks([])
plt.show()

## get a pixel value
(b, g, r) = img[6, 40]
## get a region of the image
top_left_corner = img[0:50, 0:50]
plt.imshow(top_left_corner[:, :, [2, 1, 0]])
plt.show()

## set a pixel value to red
img[6, 40] = (0, 0, 255)

## read image in grey scale
gray_img = cv2.imread('/Users/lucyliu/Documents/GitHub/LearnComputerVision/image/lucyface.png', cv2.IMREAD_GRAYSCALE)
i = gray_img[6, 40]
plt.imshow(gray_img, cmap='gray', vmin=0, vmax=255)
plt.show()

## split and merge channels
b, g, r = cv2.split(img)
img_rgb = cv2.merge([r, g, b])
plt.imshow(img_rgb)

## show b g r and r g b image
plt.subplot(121)
plt.imshow(img)

plt.subplot(122)
plt.imshow(img_rgb)
plt.show()

## concatenate two picture horizontally
img_concats = np.concatenate((img, img_rgb), axis=1)
plt.imshow(img_concats)
plt.show()