import cv2
import numpy as np

# Load the video file or initialize the camera
video_capture = cv2.VideoCapture(0)

# Load the pre-trained Haar cascade for fire detection
fire_cascade = cv2.CascadeClassifier('path_to_fire_cascade.xml')

while True:
    # Read the video frame
    ret, frame = video_capture.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect fires in the frame
    fires = fire_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around the detected fires
    for (x, y, w, h) in fires:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, 'Fire', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    
    # Display the resulting frame
    cv2.imshow('Fire Detection', frame)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
video_capture.release()
cv2.destroyAllWindows()
