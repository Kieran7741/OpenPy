
from .show_video import ShowVideoStream
from .capture import Capture
from .detector import Detector

operations = { 
    'SHOW_VIDEO': ShowVideoStream,
    'CAPTURE': Capture,
    'DETECTOR': Detector
}