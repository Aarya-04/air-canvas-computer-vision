import numpy as np
import cv2
from collections import deque

# Default callback function for the trackbar
def setValues(x):
   print("")

# Creating the trackbars needed for adjusting the marker color
cv2.namedWindow("Color detectors")
cv2.createTrackbar("Upper Hue", "Color detectors", 80, 180, setValues)  # Adjusted for green color
cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255, setValues)
cv2.createTrackbar("Upper Value", "Color detectors", 255, 255, setValues)
cv2.createTrackbar("Lower Hue", "Color detectors", 40, 180, setValues)  # Adjusted for green color
cv2.createTrackbar("Lower Saturation", "Color detectors", 40, 255, setValues)
cv2.createTrackbar("Lower Value", "Color detectors", 40, 255, setValues)

# Array to handle the green color points
gpoints = [deque(maxlen=1024)]

# Index to mark points for green color
green_index = 0

# The kernel to be used for dilation
kernel = np.ones((5, 5), np.uint8)

# Green color for drawing
color = (0, 255, 0)

# Canvas setup
paintWindow = np.zeros((471, 636, 3)) + 255
paintWindow = cv2.rectangle(paintWindow, (40, 1), (140, 65), (0, 0, 0), 2)
cv2.putText(paintWindow, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)

cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)

# Loading the default webcam of PC
cap = cv2.VideoCapture(0)

# Keep looping
while True:
    # Reading the frame from the camera
    ret, frame = cap.read()
    # Flipping the frame to see the same side as yours
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get values from the trackbar for the green color
    u_hue = cv2.getTrackbarPos("Upper Hue", "Color detectors")
    u_saturation = cv2.getTrackbarPos("Upper Saturation", "Color detectors")
    u_value = cv2.getTrackbarPos("Upper Value", "Color detectors")
    l_hue = cv2.getTrackbarPos("Lower Hue", "Color detectors")
    l_saturation = cv2.getTrackbarPos("Lower Saturation", "Color detectors")
    l_value = cv2.getTrackbarPos("Lower Value", "Color detectors")
    Upper_hsv = np.array([u_hue, u_saturation, u_value])
    Lower_hsv = np.array([l_hue, l_saturation, l_value])

    # Adding the clear button to the live frame
    frame = cv2.rectangle(frame, (40, 1), (140, 65), (122, 122, 122), -1)
    cv2.putText(frame, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    # Identifying the pointer by making its mask for green color
    Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
    Mask = cv2.erode(Mask, kernel, iterations=1)
    Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
    Mask = cv2.dilate(Mask, kernel, iterations=1)

    # Find contours for the pointer
    cnts, _ = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    center = None

    # If contours are formed
    if len(cnts) > 0:
        # Sorting the contours to find the biggest
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
        # Get the radius of the enclosing circle around the found contour
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        # Draw the circle around the contour
        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        # Calculating the center of the detected contour
        M = cv2.moments(cnt)
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

        # Check if the user wants to click on the clear button
        if center[1] <= 65:
            if 40 <= center[0] <= 140:  # Clear Button
                gpoints = [deque(maxlen=512)]
                green_index = 0
                paintWindow[67:, :, :] = 255
        else:
            gpoints[green_index].appendleft(center)

    # Append the next deque when nothing is detected to avoid messing up
    else:
        gpoints.append(deque(maxlen=512))
        green_index += 1

    # Draw lines of the green color on the canvas and frame
    for j in range(len(gpoints)):
        for k in range(1, len(gpoints[j])):
            if gpoints[j][k - 1] is None or gpoints[j][k] is None:
                continue
            cv2.line(frame, gpoints[j][k - 1], gpoints[j][k], color, 2)
            cv2.line(paintWindow, gpoints[j][k - 1], gpoints[j][k], color, 2)

    # Show all the windows
    cv2.imshow("Tracking", frame)
    cv2.imshow("Paint", paintWindow)
    cv2.imshow("mask", Mask)

    # If the 'q' key is pressed then stop the application
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and all resources
cap.release()
cv2.destroyAllWindows()
