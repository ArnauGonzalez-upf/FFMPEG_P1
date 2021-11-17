import numpy as np


def my_dct(values):
    # Get dimensions and create result matrix
    m, n = values.shape
    dct_mat = np.zeros((m, n))
    # Set line matrix index values
    for p in range(m):
        # Define alphas
        if p == 0:
            ci = 1 / np.sqrt(m)
        else:
            ci = np.sqrt(2) / np.sqrt(m)
        # Set column matrix index values
        for q in range(n):
            # Define alphas
            if q == 0:
                cj = 1 / np.sqrt(n)
            else:
                cj = np.sqrt(2) / np.sqrt(n)
            # Set matrix position value applying formula
            result = 0
            for i in range(m):
                for j in range(n):
                    dct1 = ci * cj * values[i][j] \
                           * np.cos((2 * i + 1) * p * np.pi / (2 * m)) \
                           * np.cos((2 * j + 1) * q * np.pi / (2 * n))
                    result += dct1
            dct_mat[p][q] = result
    return dct_mat


def my_idct(values):
    # Get dimensions and create result matrix
    m, n = values.shape
    inv_dct_mat = np.zeros((m, n))
    # Set line matrix index values
    for i in range(m):
        # Set column matrix index values
        for j in range(n):
            # Set matrix position value applying formula
            result = 0
            for p in range(m):
                # Set alpha
                if p == 0:
                    ci = 1 / np.sqrt(m)
                else:
                    ci = np.sqrt(2) / np.sqrt(m)
                for q in range(n):
                    # Set alpha
                    if q == 0:
                        cj = 1 / np.sqrt(n)
                    else:
                        cj = np.sqrt(2) / np.sqrt(n)
                    # Apply formula
                    dct2 = ci * cj * values[p][q] * np.cos((2 * i + 1) * p * np.pi / (2 * m)) \
                        * np.cos((2 * j + 1) * q * np.pi / (2 * n))
                    result += dct2
            inv_dct_mat[i][j] = result
    return inv_dct_mat


# Execution with a predefined matrix
if __name__ == '__main__':
    a = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
                  [1, 2, 3, 4, 5, 6, 7, 8]])
    dct = my_dct(a)
    idct = my_idct(dct)
    print(a, "DCT =", dct)
    print(dct, "IDCT =", idct)
