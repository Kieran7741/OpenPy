
import cv2 as cv


class Capture:

    def __init__(self, mode='picture', camera=0):
        self.mode = mode
        self.video_stream = cv.VideoCapture(camera)

    def run(self):
        if self.mode == 'video':
            self.record_video()
        else:
            self.capture_image()

        self.video_stream.release()

    def record_video(self):
        """
        Record video using OpenCV
        """
        video_name = input('Please enter video name: ')
        print('Press q to quit view recording')

        frame_width = int(self.video_stream.get(3))
        frame_height = int(self.video_stream.get(4))
        # Define the codec and create VideoWriter object
        fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')
        out = cv.VideoWriter(f'{video_name}.avi', fourcc,
                             10.0, (frame_width, frame_height))
        while(self.video_stream.isOpened()):
            ok, frame = self.video_stream.read()
            if ok == True:
                # write the flipped frame
                out.write(frame)
                cv.imshow('frame', frame)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        out.release()
        cv.destroyAllWindows()

    def capture_image(self):
        """
        Capture and save image.
        """
        image_name = input('Please enter image name: ')
        print("Press 'c' to capture image: ")
        while(self.video_stream.isOpened()):
            ok, frame = self.video_stream.read()
            cv.imshow('frame', frame)

            if cv.waitKey(1) & 0xFF == ord('c'):
                cv.imwrite(f'./{image_name}.jpg', frame)
                break
        cv.destroyAllWindows()
