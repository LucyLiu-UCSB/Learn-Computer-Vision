import cv2
import matplotlib.pyplot as plt

##########################       split and merge channels       ##########################
image = cv2.imread('/Users/lucyliu/Documents/GitHub/LearnComputerVision/image/lucyface.png')
b, g, r = cv2.split(image)
# note that split function is slower than
b = image[:, :, 0]

## merge image
image_copy = cv2.merge((b, g, r))

def show_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(3, 6, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')


# create a figure() object with appropriate size and title:
plt.figure(figsize=(13, 5))
plt.suptitle("Splitting and merging channels in OpenCV", fontsize=14, fontweight='bold')

# Show the BGR image:
show_with_matplotlib(image, "BGR - image", 1)

# Show all the channels from the BGR image:
show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), "BGR - (B)", 2)
show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), "BGR - (G)", 2 + 6)
show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), "BGR - (R)", 2 + 6 * 2)

# Show the BGR image:
show_with_matplotlib(image_copy, "BGR - image (copy)", 1 + 6)


# We make a copy of the loaded image:
image_without_blue = image.copy()

# From the BGR image, we "eliminate" (set to 0) the blue component (channel 0):
image_without_blue[:, :, 0] = 0

# From the BGR image, we "eliminate" (set to 0) the green component (channel 1):
image_without_green = image.copy()
image_without_green[:, :, 1] = 0

# From the BGR image, we "eliminate" (set to 0) the red component (channel 2):
image_without_red = image.copy()
image_without_red[:, :, 2] = 0

# Show all the channels from the BGR image:
show_with_matplotlib(image_without_blue, "BGR without B", 3)
show_with_matplotlib(image_without_green, "BGR without G", 3 + 6)
show_with_matplotlib(image_without_red, "BGR without R", 3 + 6 * 2)

# Split the 'image_without_blue' image into its three components (blue, green and red):
(b, g, r) = cv2.split(image_without_blue)

# Show all the channels from the BGR image without the blue information:
show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), "BGR without B (B)", 4)
show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), "BGR without B (G)", 4 + 6)
show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), "BGR without B (R)", 4 + 6 * 2)

# Split the 'image_without_green' image into its three components (blue, green and red):
(b, g, r) = cv2.split(image_without_green)

# Show all the channels from the BGR image without the green information:
show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), "BGR without G (B)", 5)
show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), "BGR without G (G)", 5 + 6)
show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), "BGR without G (R)", 5 + 6 * 2)

# Split the 'image_without_red' image into its three components (blue, green and red):
(b, g, r) = cv2.split(image_without_red)

# Show all the channels from the BGR image without the red information:
show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), "BGR without R (B)", 6)
show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), "BGR without R (G)", 6 + 6)
show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), "BGR without R (R)", 6 + 6 * 2)

# Show the created image:
plt.show()

##########################       Geometric transformation of images       ##########################

def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()

## affine transformation, the transformation is on the position
# | m11, m12 | |x|   |m13|
# |          |*| | + |   |
# | m21, m22 | |y|   |m23|

# 1. Scaling or resizing
# Resize the input image using cv2.resize()
# Resize using the scaling factor for each dimension of the image
# In this case the scaling factor is 0.5 in every dimension
dst_image = cv2.resize(image, dsize = None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Get the height and width of the image:
height, width = image.shape[:2]

# You can resize also the image specifying the new size:
dst_image_2 = cv2.resize(image, (width * 2, height * 2), interpolation=cv2.INTER_LINEAR)

# We see the two resized images:
show_with_matplotlib(dst_image, 'Resized image')
show_with_matplotlib(dst_image_2, 'Resized image 2')

# 2. Translation
# You need to create the 2x3 transformation matrix making use of numpy array with float values (float32)
# Translation in the x direction: 200 pixels, and a translation in the y direction: 30 pixels:
M = np.float32([[1, 0, 200], [0, 1, 30]])
# Once this transformation Matrix is created, we can pass it to the function cv2.warpAffine():
dst_image = cv2.warpAffine(image, M, dsize = (width, height))
# Show the translated image:
# the image move to right by 200 and down by 30
show_with_matplotlib(dst_image, 'Translated image (positive values)')

M = np.float32([[1, 0, -200], [0, 1, -30]]) # move left and up
dst_image = cv2.warpAffine(image, M, (width, height))
show_with_matplotlib(dst_image, 'Translated image (negative values)')

aa = np.sqrt(2)*0.5
M_rotation = np.float32([[aa, aa, 0], [-aa, aa, 0]]) # rotate the photo
dst_image = cv2.warpAffine(image, M_rotation, (width, height))
show_with_matplotlib(dst_image, 'rotate image')

# note that
left_bottom = np.dot(M_rotation[:, [0, 1]],  np.array([0, 600]).reshape((2, 1)))

# 3. Rotation
# To rotate the image we make use of the function  cv.getRotationMatrix2D() to build the 2x3 rotation matrix:
# In this case, we are going to rotate the image 180 degrees (upside down):
M = cv2.getRotationMatrix2D((width / 2.0, height / 2.0), 180, 1)
dst_image = cv2.warpAffine(image, M, (width, height))


# Show the center of rotation and the rotated image:
cv2.circle(dst_image, (round(width / 2.0), round(height / 2.0)), 5, (255, 0, 0), -1)
show_with_matplotlib(dst_image, 'Image rotated 180 degrees')

# Now, we are going to rotate the image 30 degrees changing the center of rotation
M = cv2.getRotationMatrix2D((width / 1.5, height / 1.5), 30, 1)
dst_image = cv2.warpAffine(image, M, (width, height))

# Show the center of rotation and the rotated image:
cv2.circle(dst_image, (round(width / 1.5), round(height / 1.5)), 5, (255, 0, 0), -1)
show_with_matplotlib(dst_image, 'Image rotated 30 degrees')


# 4. Affine Transformation
# In an affine transformation we first make use of the function cv2.getAffineTransform()
# to build the 2x3 transformation matrix, which is obtained from the relation between three points
# from the input image and their corresponding coordinates in the transformed image.

# the transformation is determined by move the first three points to the second three points. six equations solve six parameters in M.

# A copy of the image is created to show the points that will be used for the affine transformation:
image_points = image.copy()
cv2.circle(image_points, (135, 45), 5, (255, 0, 255), -1)
cv2.circle(image_points, (385, 45), 5, (255, 0, 255), -1)
cv2.circle(image_points, (135, 230), 5, (255, 0, 255), -1)

# Show the image with the three created points:
show_with_matplotlib(image_points, 'before affine transformation')

# We create the arrays with the aforementioned three points and the desired positions in the output image:
pts_1 = np.float32([[135, 45], [400, 45], [135, 230]])
pts_2 = np.float32([[135, 45], [400, 45], [150, 230]])

# We get the 2x3 tranformation matrix based on pts_1 and pts_2 and apply cv2.warpAffine():
M = cv2.getAffineTransform(pts_1, pts_2)
dst_image = cv2.warpAffine(image_points, M, (width, height))

# Show the image:
show_with_matplotlib(dst_image, 'Affine transformation')



# 5. Perspective transformation
# A copy of the image is created to show the points that will be used for the perspective transformation:
image_points = image.copy()
cv2.circle(image_points, (450, 65), 5, (255, 0, 255), -1)
cv2.circle(image_points, (517, 65), 5, (255, 0, 255), -1)
cv2.circle(image_points, (431, 164), 5, (255, 0, 255), -1)
cv2.circle(image_points, (552, 164), 5, (255, 0, 255), -1)

# Show the image:
show_with_matplotlib(image_points, 'before perspective transformation')

# cv2.getPerspectiveTransform() needs four pairs of points
# (coordinates of a quadrangle in both the source and output image)
# We create the arrays for these four pairs of points:
pts_1 = np.float32([[450, 65], [517, 65], [431, 164], [552, 164]])
pts_2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# stretch the first four points to form the perspective of second four points

# To correct the perspective (also known as perspective transformation) you need to create the transformation matrix
# making use of the function cv2.getPerspectiveTransform(), where a 3x3 matrix is constructed:
M = cv2.getPerspectiveTransform(pts_1, pts_2)

# Then, apply cv2.warpPerspective(), where the source image is transformed applying
# the specified matrix and with a specified size:
dst_image = cv2.warpPerspective(image, M, (300, 300))

# Show the image:
show_with_matplotlib(dst_image, 'perspective transformation')


# 6. Cropping
# A copy of the image is created to show the points that will be used for the cropping example:
image_points = image.copy()

# Show the points and lines connecting the points:
cv2.circle(image_points, (230, 80), 5, (0, 0, 255), -1)
cv2.circle(image_points, (330, 80), 5, (0, 0, 255), -1)
cv2.circle(image_points, (230, 200), 5, (0, 0, 255), -1)
cv2.circle(image_points, (330, 200), 5, (0, 0, 255), -1)
cv2.line(image_points, (230, 80), (330, 80), (0, 0, 255))
cv2.line(image_points, (230, 200), (330, 200), (0, 0, 255))
cv2.line(image_points, (230, 80), (230, 200), (0, 0, 255))
cv2.line(image_points, (330, 200), (330, 80), (0, 0, 255))

# Show the image with the points and lines:
show_with_matplotlib(image_points, 'Before cropping')

# For cropping, we make use of numpy slicing:
dst_image = image[80:200, 230:330]

# Show the image:
show_with_matplotlib(dst_image, 'Cropping image')