
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

        # Define the codec and create VideoWriter object
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        out = cv.VideoWriter(f'{video_name}.avi',fourcc, 20.0, (640,480))
        while(self.video_stream.isOpened()):
            ok, frame = self.video_stream.read()
            if ok == True:
                frame = cv.flip(frame,0)
                # write the flipped frame
                out.write(frame)
                cv.imshow('frame',frame)
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
            cv.imshow('frame',frame)

            if cv.waitKey(1) & 0xFF == ord('c'):
                cv.imwrite(f'./{mage_name}.jpg', frame)
                break
        cv.destroyAllWindows()



