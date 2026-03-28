import cv2
import numpy as np


def start_camera():

    cap = cv2.VideoCapture(0)

    face = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    body = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_fullbody.xml"
    )

    ret, prev_frame = cap.read()

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face.detectMultiScale(gray, 1.3, 5)
        bodies = body.detectMultiScale(gray, 1.1, 3)

        diff = cv2.absdiff(prev_frame, frame)
        gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(gray_diff, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)

        motion = thresh.sum()

        suspicious = motion > 2000000

        color = (0, 255, 0)
        label = "Normal"

        if suspicious:
            color = (0, 0, 255)
            label = "Suspicious"

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, label, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, label, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        cv2.imshow("AI Threat Detection Camera", frame)

        prev_frame = frame.copy()

        key = cv2.waitKey(1) & 0xFF

        if key == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()