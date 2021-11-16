import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    select = 100
    while select != "0":
        print("Select:")
        print("0) Exit")
        print("1) RGB and YUV translator")
        print("2) Image Resize")
        print("3) B&W Image Compressed")
        print("4) Run-Length Encoding")
        print("5) 1D DCT")
        print("6) 2D DCT")
        select = input()

        if (select == "0"):
            break
        elif (select == "1"):
            cmd = 'python3 ex1.py'
        elif (select == "2"):
            cmd = 'python3 ex2.py'
        elif (select == "3"):
            cmd = 'python3 ex3.py'
        elif (select == "4"):
            cmd = 'python3 ex4.py'
        elif (select == "5"):
            cmd = 'python3 ex5.py' 
        elif (select == "6"):
            cmd = 'python3 ex5_2d.py'    
        else:
            print("Not an option!")

        os.system(cmd)
    exit()
