import cv2
import numpy as np
import matplotlib.pyplot as plt


## build a color dictionary
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

## matplotlib plot
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()

## show color map
# We set background to black using np.zeros():
image = np.zeros((500, 500, 3), dtype="uint8")

# If you want another background color you can do the following:
image[:] = colors['light_gray']

# We draw all the colors to test the dictionary
# We draw some lines each one in one color. To get the color use 'colors[key]'
separation = 40
for key in colors:
    # Draw a line using the function cv2.line():
    cv2.line(image, (0, separation), (500, separation), colors[key], 10)
    separation += 40

# Show image:
show_with_matplotlib(image, 'Dictionary with some predefined colors')

## Draw basic shapes

# We create the canvas to draw: 400 x 400 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set the background to black using np.zeros()

image = np.zeros((400, 400, 3), dtype="uint8")
# If you want another background color, you can do the following:
image[:] = colors['light_gray']

## drawing lines
cv2.line(image, pt1 = (0, 0), pt2 = (400, 400), color = colors['green'], thickness = 3)
cv2.line(image, (0, 400), (400, 0), colors['blue'], thickness=10)
cv2.line(image, (200, 0), (200, 400), colors['red'], 3)
cv2.line(image, (0, 200), (400, 200), colors['yellow'], 10)
show_with_matplotlib(image, 'cv2.line()')

## Drawing rectangles
cv2.rectangle(image, pt1 =  (10, 50), pt2 = (60, 300), color = colors['green'], thickness = 3)
# thickness -1 to fill the rectangles
cv2.rectangle(image, (80, 50), (130, 300), colors['blue'], -1)
cv2.rectangle(image, (150, 50), (350, 100), colors['red'], -1)
cv2.rectangle(image, (150, 150), (350, 300), colors['cyan'], 10)
show_with_matplotlib(image, 'cv2.rectangle()')

## drawing circles
cv2.circle(image, center = (50, 50), radius = 20, color = colors['green'], thickness = 3)
cv2.circle(image, (100, 100), 30, colors['blue'], -1)
cv2.circle(image, (200, 200), 40, colors['magenta'], 10)
cv2.circle(image, (300, 300), 40, colors['cyan'], -1)
show_with_matplotlib(image, 'cv2.circle()')

## write text

## other font choices, textbox and underline -- page 198
image.fill(255)
# img = cv.putText( img, text, org, fontFace, fontScale, color, thickness=1, lineType)
cv2.putText(image, 'Mastering OpenCV4 with Python', (10, 30), 6, 0.5, colors['red'], 2,
            cv2.LINE_4)
cv2.putText(image, 'Mastering OpenCV4 with Python', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors['green'], 1,
            cv2.LINE_8)
cv2.putText(image, 'Mastering OpenCV4 with Python', (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors['blue'], 3,
            cv2.LINE_AA)

show_with_matplotlib(image, 'cv2.putText()')