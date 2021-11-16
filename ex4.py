def run_length_encoding(values):
    result = []
    i = 0
    while i < len(values):
        if values[i] == 0:
            result.append(0)
            zeros_num = 0
            for j in range(i, len(values)):
                if values[j] == 0:
                    zeros_num += 1
                else:
                    break
            result.append(zeros_num)
            i += zeros_num - 1
        else:
            result.append(values[i])
        i += 1
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("[1,0,0,0,3,2,0,0,1,0,5,8,20,0,0,0] is:", run_length_encoding([1,0,0,0,3,2,0,0,1,0,5,8,20,0,0,0]))
