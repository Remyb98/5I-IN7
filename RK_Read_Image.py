"""
Edited by Rostom Kachouri
M1-IRV_ST2IAI _ Mars 2021
"""

# Read Image

# Adding sys to read params given to the program, in this case, the image path
import sys
import cv2

if 2 > len(sys.argv):
    print("Usage: python3 RK_Read_image.py path/to/image.png")
    exit(1)

# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread(sys.argv[1])

# DISPLAY
cv2.imshow("Image", img)
cv2.waitKey(0)

cv2.destroyWindow ('Image')
