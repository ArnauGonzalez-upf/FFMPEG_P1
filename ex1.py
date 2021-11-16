def rgb_yuv(values, rgb_to_yuv = True):

    if rgb_to_yuv:
    	Y = 0.257 * values[0] + 0.504 * values[1] + 0.098 * values[2] + 16
    	Cb = -0.148 * values[0] - 0.291 * values[1] + 0.439 * values[2] + 128
    	Cr = 0.439 * values[0] - 0.368 * values[1] - 0.071 * values[2] + 128
    	result = [round(Y), round(Cb), round(Cr)]
    else:
    	Y = values[0] - 16
    	Cb = values[1] - 128
    	Cr = values[2] - 128
    	R = 1.164 * Y + 1.596 * Cr
    	G = 1.164 * Y - 0.813 * Cr - 0.391 * Cb
    	B = 1.164 * Y + 2.018 * Cb
    	result = [round(R), round(G), round(B)]
        
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	rgb = [128, 54, 201]
	yuv = rgb_yuv(rgb)
	rgb_from_yuv = rgb_yuv(yuv, False)
	print(rgb, "in YUV:", yuv)
	print(yuv, "in RGB:", rgb_from_yuv)

