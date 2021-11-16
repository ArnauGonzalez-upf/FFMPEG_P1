import numpy as np
from scipy.fftpack import dct

def dct_mat(n):
    D = np.zeros((8, 8))
    for u in range(n):
       if u == 0:
           au = np.sqrt(1/n)
       else:
           au = np.sqrt(2/n)

       for x in range(n):
           D[u,x] = au * np.cos(((2*x+1) * u * np.pi) / (2*n))
           
    return D

def my_dct(values):
    n = len(values)
    D = dct_mat(n)
    y = D @ values
    return y

def my_idct(values):
    n = len(values)
    D = dct_mat(n)
    y = np.linalg.inv(D) @ values
    return y

if __name__ == '__main__':
    print("[1, 2, 3, 4, 5, 6, 7, 8] is:", my_dct([1, 2, 3, 4, 5, 6, 7, 8]))
    print("[1, 2, 3, 4, 5, 6, 7, 8] is:", my_idct(my_dct([1, 2, 3, 4, 5, 6, 7, 8])))
