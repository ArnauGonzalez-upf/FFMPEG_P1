def rgb_yuv(values, rgb_to_yuv=True):
    # Apply rgb to yuv formula
    if rgb_to_yuv:
        y = 0.257 * values[0] + 0.504 * values[1] + 0.098 * values[2] + 16
        u = -0.148 * values[0] - 0.291 * values[1] + 0.439 * values[2] + 128
        v = 0.439 * values[0] - 0.368 * values[1] - 0.071 * values[2] + 128
        result = [round(y), round(u), round(v)]

    # Apply yuv to rgb formula
    else:
        # Normalize the yuv values to be used in the formula
        y = values[0] - 16
        u = values[1] - 128
        v = values[2] - 128

        r = 1.164 * y + 1.596 * v
        g = 1.164 * y - 0.813 * v - 0.391 * u
        b = 1.164 * y + 2.018 * u
        result = [round(r), round(g), round(b)]

    return result


# Execution with a predefined rgb vector
if __name__ == '__main__':
    rgb = [128, 54, 201]
    yuv = rgb_yuv(rgb)
    rgb_from_yuv = rgb_yuv(yuv, False)
    print(rgb, "in YUV:", yuv)
    print(yuv, "in RGB:", rgb_from_yuv)
