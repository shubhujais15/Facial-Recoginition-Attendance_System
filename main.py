import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# open ur camera....Index 0 shows the primary cam will open if we change the index it will open other cameras.
video_capture = cv2.VideoCapture(1)

# Load known faces
shubham_img = face_recognition.load_image_file("faces/shubham.png")
# creating img encodings in digits so it can easy to compare img
# the index 0 specify that :- if in img there are 10 faces then it creates list of those img and by passing 0 index it create encodings of that face
shubham_encoding = face_recognition.face_encodings(shubham_img)[0]

abhi_img = face_recognition.load_image_file("faces/abhi.jpg")
abhi_encoding = face_recognition.face_encodings(abhi_img)[0]

# Now we store name of encodings
known_face_encodings = [shubham_encoding, abhi_encoding]
# Now we give the names for both encodings
known_face_names = ["Shubham", "Abhi"]

# list of expected student who came for giving attendance
students = known_face_names.copy()

face_locations = []
face_encodings = []

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Now create csv file
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read() # here the _ is bcz the video_capture.read gives two arguments first one is vdo capture is succesful or not second is frame so we want frame only
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize Faces
    face_locations = face_recognition.face_locations(rgb_small_frame) #It returns bounding boxes after recognizing face
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations) # encodings of face that captures through camera

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if(matches[best_match_index]):
            name = known_face_names[best_match_index]

        # Add the text if person is present
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10,100)
            fontScale = 1.5
            fontColor = (255,0,0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name + " Present At : " + current_time])

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
