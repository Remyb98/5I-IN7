"""
Edited by Rostom Kachouri
M1-IRV_ST2IAI _ Mars 2021
"""

#Read Video

# Adding sys to read params given to the program, in this case, the video path
import sys
import cv2

if 2 > len(sys.argv):
    print("Usage: python3 RK_Read_Video.py path/to/video.mp4")
    exit(1)

cap = cv2.VideoCapture(sys.argv[1])
while True:
    # Get the next frame
    success, img = cap.read()
    # We want to stop the video with "q" or it is finished
    if cv2.waitKey(1) == ord('q') or not success:
         break
    # Display the frame
    cv2.imshow("Video", img)
         
cv2.destroyWindow('Video')
