import cv2 as cv


class ShowVideoStream:

    def __init__(self, camera=0):
        self.operation = 'SHOW_VIDEO'
        self.video_stream = cv.VideoCapture(camera)

    def run(self):
        print('Displaying video stream. Press q to quit.')
        while(self.video_stream.isOpened()):
            ok, frame = self.video_stream.read()
            if ok == True:
                cv.imshow('frame', cv.flip(frame,0))
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        
        self.video_stream.release()
