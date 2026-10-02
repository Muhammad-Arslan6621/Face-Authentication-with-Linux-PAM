import cv2
import os
import numpy as np
import face_recognition
import sys
import time

ALLOWED_DIR = "/home/aether_quasar/Videos/os_project/allowed_faces/"

def authenticate_face():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera could not be accessed.")
        sys.exit(1)  # Exit with error code

    # Load all allowed face encodings from the "allowed_faces" directory
    allowed_faces = {}
    for file in os.listdir(ALLOWED_DIR):
        if file.endswith(".npy"):
            name = file.replace(".npy", "")
            encoding = np.load(os.path.join(ALLOWED_DIR, file))
            allowed_faces[name] = encoding

    print(f"Loaded {len(allowed_faces)} allowed faces.")
    
    # Start capturing frames for face recognition
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error accessing the webcam.")
            break

        # Convert frame to RGB for face_recognition
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Get face locations and encodings
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        recognized_face = None

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(list(allowed_faces.values()), face_encoding)
            face_distances = face_recognition.face_distance(list(allowed_faces.values()), face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = list(allowed_faces.keys())[best_match_index]
                recognized_face = name
                print(f"Face recognized: {name}")
                break  # Exit the loop once a face is recognized

        if recognized_face is not None:
            # If a face is recognized, stop the camera and exit the loop
            print("Authentication successful.")
            cap.release()
            sys.exit(0)  # Exit successfully if recognized face
        else:
            print("Face not recognized.")
            time.sleep(2)  # Wait for 2 seconds before checking again

    cap.release()

authenticate_face()
