import cv2 as cv
from cv2.data import haarcascades
import os


class Detector:

    def __init__(self, detector_name, camera=0):

        self.detector_path = os.path.join(haarcascades, detector_name)
        self.video_stream = cv.VideoCapture(camera)
        self.detector = cv.CascadeClassifier(self.detector_path)

    def run(self):
        while self.video_stream.isOpened():
            ok, frame = self.video_stream.read()
            if ok:
                print('showing frame')
                gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                objs = self.detector.detectMultiScale(gray_frame, 1.1, 5)
                for (x, y, w, h) in objs:
                    cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv.imshow('frame', frame)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
