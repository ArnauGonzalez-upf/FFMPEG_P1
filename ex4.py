def run_length_encoding(values):
    # Array to store the result
    result = []
    # Loop to get every value
    i = 0
    while i < len(values):
        if values[i] == 0:
            # Append the zero value
            result.append(values[i])
            zeros_num = 0
            # Identify how many zeros are
            for j in range(i, len(values)):
                if values[j] == 0:
                    zeros_num += 1
                else:
                    break
            result.append(zeros_num)
            i += zeros_num - 1  # -1 so that the first zero is not counted to advance
        else:
            result.append(values[i])
        i += 1
    return result


# Execution with a predefined vector
if __name__ == '__main__':
    a = [1, 0, 0, 0, 3, 2, 0, 0, 1, 0, 5, 8, 20, 0, 0, 0]
    print(a, " encoded using Run-Length Encoding =", run_length_encoding(a))
