import argparse
import cv2
import numpy as np
from matplotlib import pyplot as plt

## create the argumentparser object, it can parse the command-line arguments into data types
parser = argparse.ArgumentParser()

## add 'path_image' argument using add_argment() including a help
parser.add_argument('path_image', help="path to input image to be displayed")
# Add 'path_image_output' argument using add_argument() including a help. The type is string
parser.add_argument("path_image_output", help="path of the processed image to be saved")

## the imformation is stored in 'parser'. use information when the parser calls parse_args() method
args = parser.parse_args()

## we can load the input from disk using the path in args
image = cv2.imread(args.path_image)

## parse the argument and store it in a dictionary
args = vars(parser.parse_args())

## load the input image from disk using args element in a dictionary
image2 = cv2.imread(args['path_image'])


img_concats = np.concatenate((image, image2), axis=1)
plt.imshow(img_concats[:, :, ::-1])
plt.show()

# Process the input image (convert it to grayscale):
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray', vmin=0, vmax=255)
plt.show()


# Save the processed image to disk:
cv2.imwrite(args["path_image_output"], gray_image)

#### test function by run in terminal
#  python Chapter3_argparse_load_image.py /Users/lucyliu/Documents/GitHub/LearnComputerVision/image/lucyface.png /Users/lucyliu/Documents/GitHub/LearnComputerVision/image/lucyface_gray.png

'''
# Show the loaded image:
cv2.imshow("loaded image", image)
cv2.imshow("loaded image2", image2

# Wait until a key is pressed:
cv2.waitKey(0)
# Destroy all windows: 
cv2.destroyAllWindows()
'''