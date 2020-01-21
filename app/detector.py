
import cv2 as cv
from cv2.data import haarcascades
import os

class Detector:

    def __init__(self, detector_name):

        self.detector_path = os.path.join(haarcascades, detector_name)
        self.detector = cv.CascadeClassifier(self.detector_path)


