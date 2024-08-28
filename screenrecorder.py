import cv2
import numpy as np
from PIL import ImageGrab

def screenrecorder():
    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Define codec for video writing
    out = cv2.VideoWriter('output.avi', fourcc, 5.0, (1366, 768))  # Output file name, codec, FPS, and resolution

    while True:
        # Capture the screen
        img = ImageGrab.grab()  # Capture the screen using PIL's ImageGrab module
        img_np = np.array(img)  # Convert the captured image to a numpy array
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)  # Convert BGR image to RGB format

        # Display the screen recording
        cv2.imshow("Screen Recorder", frame)  # Display the captured frame in a window named "Screen Recorder"

        # Write the frame to the video file
        out.write(frame)  # Write the frame to the video file

        # Break the loop if 'Esc' key is pressed
        if cv2.waitKey(1) == 27:
            break

    # Release resources
    out.release()  # Release the VideoWriter object
    cv2.destroyAllWindows()  # Close all OpenCV windows

# Call the function to start screen recording
screenrecorder()
