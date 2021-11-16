import os

if __name__ == '__main__':
    print("Set reduce ratio:")
    ratio = input()
    #cmd = 'ffmpeg -i nier.jpg -vf scale=' + '"' + width + ':' + height +'"' + ' nier_resized.jpg'
    cmd = 'ffmpeg -i nier.jpg -vf scale="iw/' + ratio + ':-1" nier_resized.jpg'
    os.system(cmd)
