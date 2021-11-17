import os


# Execution with a with an input ratio
if __name__ == '__main__':
    # Ratio input
    print("Set reduce ratio:")
    ratio = input()

    # Command line instruction and execution
    cmd = 'ffmpeg -i nier.jpg -vf scale="iw/' + ratio + ':-1" nier_resized.jpg'
    os.system(cmd)
