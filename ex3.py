import os


# Execution with a with an input option
if __name__ == '__main__':
    # Input options
    print("Select option:")
    print("0) B&W Conversion")
    print("1) Maximum Compression")
    print("2) Both")
    option = input()

    # Different command line instructions for every option
    if option == "0":
        cmd = 'ffmpeg -i nier.jpg -vf format=gray nier_bw.jpg'
    elif option == "1":
        cmd = 'ffmpeg -i nier.jpg -compression_level 100 nier_compressed.jpg'
    elif option == "2":
        cmd = 'ffmpeg -i nier.jpg -compression_level 100 -vf format=gray nier_bw_compressed.jpg'
    else:
        print("Not an option!")
        cmd = ''

    # Execute instruction
    os.system(cmd)
