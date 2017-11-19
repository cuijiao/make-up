import cv2
import json
import numpy
import face_recognition
from PIL import Image, ImageDraw


class VideoCamera(object):
    def __init__(self, eyebrows, lips, eyeliner):
        self.video = cv2.VideoCapture(0)
        self.eyebrows = eyebrows
        self.eyeliner = eyeliner
        self.lips = lips

    def __del__(self):
        self.video.release()

    def get_frame(self):
        eyebrows = json.loads(self.eyebrows)
        eyeliner = json.loads(self.eyeliner)
        lips = json.loads(self.lips)

        while True:
            ret, image = self.video.read()

            face_landmarks_list = face_recognition.face_landmarks(image)
            pil_image = Image.fromarray(image)

            for face_landmarks in face_landmarks_list:
                d = ImageDraw.Draw(pil_image, 'RGBA')

                # Make the eyeliner into a nightmare
                d.polygon(face_landmarks['left_eyebrow'],
                          fill=(eyebrows["g"], eyebrows["b"], eyebrows["r"], eyebrows["opacity"]))
                d.polygon(face_landmarks['right_eyebrow'],
                          fill=(eyebrows["g"], eyebrows["b"], eyebrows["r"], eyebrows["opacity"]))
                d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=3)
                d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=3)

                # Gloss the lips
                d.polygon(face_landmarks['top_lip'], fill=(lips["g"], lips["b"], lips["r"], lips["opacity"]))
                d.polygon(face_landmarks['bottom_lip'], fill=(lips["g"], lips["b"], lips["r"], lips["opacity"]))
                d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=5)
                d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=5)

                # Sparkle the eyes
                d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
                d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

                # Apply some eyeliner
                d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]],
                       fill=(eyeliner["g"], eyeliner["b"], eyeliner["r"], eyeliner["opacity"]), width=3)
                d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]],
                       fill=(eyeliner["g"], eyeliner["b"], eyeliner["r"], eyeliner["opacity"]), width=3)

            ret, jpeg = cv2.imencode('.jpg', numpy.array(pil_image))
            return jpeg.tobytes()
