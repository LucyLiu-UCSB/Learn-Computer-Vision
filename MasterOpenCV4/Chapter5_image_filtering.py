# Import required packages:
import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(3, 3, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')

## read image
image = cv2.imread('/Users/lucyliu/Documents/GitHub/LearnComputerVision/image/lucyface.png')

# Create a figure() object with appropriate size and title
plt.figure(figsize=(12, 6))
plt.suptitle("Smoothing techniques", fontsize=14, fontweight='bold')

## create the average kernel
kernel_averaging_5_5 = np.ones((5, 5), np.float32)/25
kernel_averaging_10_10 = np.ones((10, 10), np.float32) / 100

print("kernel: {}".format(kernel_averaging_5_5))
# The function cv2.filter2D() applies an arbitrary linear filter to the provided image:
smooth_image_f2D_5_5 = cv2.filter2D(image, -1, kernel_averaging_5_5)
smooth_image_f2D_10_10 = cv2.filter2D(image, -1, kernel_averaging_10_10)

smooth_image_b = cv2.blur(image, (10, 10))

# When the parameter normalize (by default True) of cv2.boxFilter() is equals to True,
# cv2.filter2D() and cv2.boxFilter() perform the same operation:
smooth_image_bfi = cv2.boxFilter(image, -1, (10, 10), normalize=True)

# The function cv2.GaussianBlur() convolves the source image with the specified Gaussian kernel
# This kernel can be controlled using the parameters ksize (kernel size),
# sigmaX(standard deviation in the x direction of the gaussian kernel) and
# sigmaY (standard deviation in the y direction of the gaussian kernel)
smooth_image_gb = cv2.GaussianBlur(image, (9, 9), 0)

# The function cv2.medianBlur(), which blurs the image with a median kernel:
smooth_image_mb = cv2.medianBlur(image, 9)

# The function cv2.bilateralFilter() can be applied to the input image in order to apply a bilateral filter:
smooth_image_bf = cv2.bilateralFilter(image, 5, 10, 10)
smooth_image_bf_2 = cv2.bilateralFilter(image, 9, 200, 200)

# Plot the images:
show_with_matplotlib(image, "original", 1)
show_with_matplotlib(smooth_image_f2D_5_5, "cv2.filter2D() (5,5) kernel", 2)
show_with_matplotlib(smooth_image_f2D_10_10, "cv2.filter2D() (10,10) kernel", 3)
show_with_matplotlib(smooth_image_b, "cv2.blur()", 4)
show_with_matplotlib(smooth_image_bfi, "cv2.boxFilter()", 5)
show_with_matplotlib(smooth_image_gb, "cv2.GaussianBlur()", 6)
show_with_matplotlib(smooth_image_mb, "cv2.medianBlur()", 7)
show_with_matplotlib(smooth_image_bf, "cv2.bilateralFilter() - small values", 8)
show_with_matplotlib(smooth_image_bf_2, "cv2.bilateralFilter() - big values", 9)

# Show the created image:
plt.show()


#### sharpen filters
def show_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(2, 3, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')


def unsharped_filter(img):
    """The unsharp filter enhances edges subtracting the smoothed image from the original image"""

    smoothed = cv2.GaussianBlur(img, (9, 9), 10)
    return cv2.addWeighted(img, 1.5, smoothed, -0.5, 0)


# Create the dimensions of the figure and set title:
plt.figure(figsize=(12, 6))
plt.suptitle("Sharpening images", fontsize=14, fontweight='bold')

# We create the kernel for sharpening images
kernel_sharpen_1 = np.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]])

kernel_sharpen_2 = np.array([[-1, -1, -1],
                             [-1, 9, -1],
                             [-1, -1, -1]])

kernel_sharpen_3 = np.array([[1, 1, 1],
                             [1, -7, 1],
                             [1, 1, 1]])

kernel_sharpen_4 = np.array([[-1, -1, -1, -1, -1],
                             [-1, 2, 2, 2, -1],
                             [-1, 2, 8, 2, -1],
                             [-1, 2, 2, 2, -1],
                             [-1, -1, -1, -1, -1]]) / 8.0

# Apply all the kernels we have created:
sharp_image_1 = cv2.filter2D(image, -1, kernel_sharpen_1)
sharp_image_2 = cv2.filter2D(image, -1, kernel_sharpen_2)
sharp_image_3 = cv2.filter2D(image, -1, kernel_sharpen_3)
sharp_image_4 = cv2.filter2D(image, -1, kernel_sharpen_4)

# Try the unsharped filter:
sharp_image_5 = unsharped_filter(image)

# Display all the resulting images:
show_with_matplotlib(image, "original", 1)
show_with_matplotlib(sharp_image_1, "sharp 1", 2)
show_with_matplotlib(sharp_image_2, "sharp 2", 3)
show_with_matplotlib(sharp_image_3, "sharp 3", 4)
show_with_matplotlib(sharp_image_4, "sharp 4", 5)
show_with_matplotlib(sharp_image_5, "sharp 5", 6)

# Show the Figure:
plt.show()