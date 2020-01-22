from app import operations
import sys

if __name__ == '__main__':

    operations['CAPTURE'](mode='video').run()
    # operation = sys.argv[1]
    # operations[operation]().run()
