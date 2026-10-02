import cv2
import os
import numpy as np
import face_recognition  # Install via `pip install face_recognition`

# Directory to store allowed face encodings
ALLOWED_DIR = "allowed_faces/"
os.makedirs(ALLOWED_DIR, exist_ok=True)

def register_face():
    cap = cv2.VideoCapture(0)
    print("Press 's' to save the face or 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error accessing the webcam.")
            break

        cv2.imshow("Register Face", frame)

        # Wait for user to press 's' or 'q'
        key = cv2.waitKey(1)
        if key == ord('s'):  # Save face
            # Detect face and encode
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            if face_encodings:
                # Save the first face encoding
                face_encoding = face_encodings[0]
                face_name = input("Enter name for this face: ")
                np.save(os.path.join(ALLOWED_DIR, f"{face_name}.npy"), face_encoding)
                print(f"Face registered for {face_name}.")
                break
            else:
                print("No face detected. Try again.")

        elif key == ord('q'):  # Quit
            print("Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()

register_face()
