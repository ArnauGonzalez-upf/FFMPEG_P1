import numpy as np


def dct_mat(n):
    # Define dct matrix
    result = np.zeros((n, n))
    # Set the alpha value
    for u in range(n):
        if u == 0:
            au = np.sqrt(1/n)
        else:
            au = np.sqrt(2/n)
        # Compute the matrix value
        for x in range(n):
            result[u, x] = au * np.cos(((2 * x + 1) * u * np.pi) / (2 * n))
    return result


def my_dct(values):
    n = len(values)  # Get vector length
    dct_matrix = dct_mat(n)  # Create dct matrix
    y = dct_matrix @ values  # Compute dct
    return y


def my_idct(values):
    n = len(values)  # Get vector length
    dct_matrix = dct_mat(n)  # Create dct matrix
    y = np.linalg.inv(dct_matrix) @ values  # Compute idct
    return y


# Execution with a predefined vector
if __name__ == '__main__':
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    dct = my_dct(a)
    idct = my_idct(dct)
    print(a, "DCT =", dct)
    print(dct, "IDCT =", idct)
