import cv2
import sys
import argparse
from matplotlib import pyplot as plt

## using sys to pass arguments
print("The name of the script being processed is: '{}'".format(sys.argv[0]))
print("The number of arguments of the script is: '{}'".format(len(sys.argv)))
print("The arguments of the script are: '{}'".format(str(sys.argv)))

# run in Terminal to test: python Chapter3_handle_files_images.py
# run in Terminal to test: python Chapter3_handle_files_images.py OpenCV

## using argparse library
parser = argparse.ArgumentParser()
parser.parse_args()

