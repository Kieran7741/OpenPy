from app import operations
import sys

if __name__ == '__main__':
    operation = sys.argv[1]
    operations[operation]()
