import os

if __name__ == '__main__':
    print("Select option:")
    print("0) B&W Conversion")
    print("1) Maximum Compression")
    print("2) Both")
    
    option = input()
    
    if option == "0":
    	cmd = 'ffmpeg -i nier.jpg -vf format=gray nier_bw.jpg'
    if option == "1":
    	cmd = 'ffmpeg -i nier.jpg -compression_level 100 nier_compressed.jpg'
    if option == "2":
    	cmd = 'ffmpeg -i nier.jpg -compression_level 100 -vf format=gray nier_bw_compressed.jpg'
    
    os.system(cmd)
