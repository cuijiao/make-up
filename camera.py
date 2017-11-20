import cv2
import numpy
import face_recognition
from styles import Styles
from PIL import Image, ImageDraw


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, image = self.video.read()

        face_landmarks_list = face_recognition.face_landmarks(image)
        pil_image = Image.fromarray(image)

        styles = Styles()

        for face_landmarks in face_landmarks_list:
            d = ImageDraw.Draw(pil_image, 'RGBA')

            # Make the eyebrows into a nightmare
            d.polygon(face_landmarks['left_eyebrow'], fill=(styles.eyebrows['b'],styles.eyebrows['g'],styles.eyebrows['r'],styles.eyebrows['opacity']))
            d.polygon(face_landmarks['right_eyebrow'], fill=(styles.eyebrows['b'],styles.eyebrows['g'],styles.eyebrows['r'],styles.eyebrows['opacity']))
            d.line(face_landmarks['left_eyebrow'], fill=(styles.eyebrows['b'],styles.eyebrows['g'],styles.eyebrows['r'],styles.eyebrows['opacity']), width=3)
            d.line(face_landmarks['right_eyebrow'], fill=(styles.eyebrows['b'],styles.eyebrows['g'],styles.eyebrows['r'],styles.eyebrows['opacity']), width=3)

            # Gloss the lips
            d.polygon(face_landmarks['top_lip'], fill=(styles.lips['b'], styles.lips['g'], styles.lips['r'], styles.lips['opacity']))
            d.polygon(face_landmarks['bottom_lip'], fill=(styles.lips['b'], styles.lips['g'], styles.lips['r'], styles.lips['opacity']))
            d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=5)
            d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=5)

            # Sparkle the eyes
            d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
            d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

            # Apply some eyeliner
            d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(styles.eyeliner['b'], styles.eyeliner['g'], styles.eyeliner['r'], styles.eyeliner['opacity']), width=3)
            d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(styles.eyeliner['b'], styles.eyeliner['g'], styles.eyeliner['r'], styles.eyeliner['opacity']), width=3)

        ret, jpeg = cv2.imencode('.jpg', numpy.array(pil_image))
        return jpeg.tobytes()
