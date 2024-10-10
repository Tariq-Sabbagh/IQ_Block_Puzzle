import cv2
import numpy as np
from IQ_Block_Puzzle import get_bigcontour


def nothing(x):
    pass


# Load an image
image,_ = get_bigcontour.run_code()# Replace with your image path
image=cv2.resize(image,(600,500))
if image is None:
    raise ValueError("Image not found. Please check the path.")

# Convert the image to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Create a window
cv2.namedWindow('Calibration')

# Create trackbars for lower HSV values
cv2.createTrackbar('Lower Hue', 'Calibration', 0, 179, nothing)
cv2.createTrackbar('Lower Saturation', 'Calibration', 0, 255, nothing)
cv2.createTrackbar('Lower Value', 'Calibration', 0, 255, nothing)

# Create trackbars for upper HSV values
cv2.createTrackbar('Upper Hue', 'Calibration', 179, 179, nothing)
cv2.createTrackbar('Upper Saturation', 'Calibration', 255, 255, nothing)
cv2.createTrackbar('Upper Value', 'Calibration', 255, 255, nothing)

while True:
    # Get current trackbar positions for lower and upper HSV values
    l_hue = cv2.getTrackbarPos('Lower Hue', 'Calibration')
    l_saturation = cv2.getTrackbarPos('Lower Saturation', 'Calibration')
    l_value = cv2.getTrackbarPos('Lower Value', 'Calibration')

    u_hue = cv2.getTrackbarPos('Upper Hue', 'Calibration')
    u_saturation = cv2.getTrackbarPos('Upper Saturation', 'Calibration')
    u_value = cv2.getTrackbarPos('Upper Value', 'Calibration')

    # Create lower and upper bounds for HSV
    lower_bound = np.array([l_hue, l_saturation, l_value])
    upper_bound = np.array([u_hue, u_saturation, u_value])

    # Create a mask based on the current HSV bounds
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=mask)

    # Display the original image, mask, and result
    cv2.imshow('Original', image)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
