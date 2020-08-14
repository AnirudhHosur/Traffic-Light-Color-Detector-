import cv2
import numpy as np

# Load the video 
cap = cv2.VideoCapture('video.asf')

# Capture the video frame by frame
while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the r,b,y colors
    lower_red = np.array([161,155,84])
    upper_red = np.array([179,255,180])
    
    lower_green = np.array(([25,52,72]))
    upper_green = np.array([102,255,255])
    
    lower_blue = np.array(([94,80,2]))
    upper_blue = np.array([126,255,255])
    
    # To extract the ROI from the video
    # If the mask is in range, mask will be 1 i.e white & this will result in with frame
    # Where there are ones in the mask, we will show color from the frame
    "mask is the color we are allowing"
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    red = cv2.bitwise_and(frame,frame, mask= red_mask)
    green = cv2.bitwise_and(frame,frame, mask= green_mask)

    # Show the video
    cv2.imshow('frame',frame)
    cv2.imshow('Red',red)
    cv2.imshow('Green',green)
    
    # Press x to stop the video
    if cv2.waitKey(25) == ord('x'):
            break

cv2.destroyAllWindows()
cap.release()

