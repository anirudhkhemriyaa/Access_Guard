import cv2
import time

# Set your password
correct_password = "1234"

# Ask for password
user_input = input("Enter password: ")

# Check password
if user_input != correct_password:
    print("Wrong password! Capturing image...")

    # Open webcam (0 = default camera)
    cam = cv2.VideoCapture(0)

    # Give time for camera to warm 
    time.sleep(2)

    ret, frame = cam.read()
    if ret:
        # Save image with timestamp
        filename = f"unauthorized_{int(time.time())}.png"
        cv2.imwrite(filename, frame)
        print(f"Image captured and saved as {filename}")
    else:
        print("Failed to access camera.")

    # Release camera
    cam.release()
else:
    print("Access granted.")
