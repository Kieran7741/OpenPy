from app import operations
import sys

if __name__ == '__main__':

    operations['DETECTOR']('haarcascade_eye.xml').run()
    # operations['SHOW_VIDEO']().run()

    # operation = sys.argv[1]
    # operations[operation]().run()
