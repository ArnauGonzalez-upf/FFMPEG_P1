import numpy as np
from scipy.fftpack import dct

def my_dct(values):
	
	m,n = values.shape
	dct = np.zeros((m,n))

	for p in range(m):
	
		if (p == 0):
			ci = 1 / np.sqrt(m)
		else:
			ci = np.sqrt(2) / np.sqrt(m)
			
		for q in range(n): 
				
			if (q == 0):
				cj = 1 / np.sqrt(n)
			else:
				cj = np.sqrt(2) / np.sqrt(n)

			result = 0; 
			for k in range(m):
				for l in range(n):
					dct1 = ci * cj * values[k][l] * np.cos((2 * k + 1) * p * np.pi / (2 * m)) * np.cos((2 * l + 1) * q * np.pi / (2 * n))
					result += dct1

			dct[p][q] = result
			
	return dct

def my_idct(values):
	
	m,n = values.shape
	idct = np.zeros((m,n))

	for k in range(m):
			
		for l in range(n): 

			result = 0; 
			for p in range(m):
	
				if (p == 0):
					ci = 1 / np.sqrt(m)
				else:
					ci = np.sqrt(2) / np.sqrt(m)
			
				for q in range(n):
				
					if (q == 0):
						cj = 1 / np.sqrt(n)
					else:
						cj = np.sqrt(2) / np.sqrt(n)
				
					dct1 = ci * cj * values[p][q] * np.cos((2 * k + 1) * p * np.pi / (2 * m)) * np.cos((2 * l + 1) * q * np.pi / (2 * n))
					result += dct1

			idct[k][l] = result
			
	return idct

if __name__ == '__main__':
	a = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]])
	dct = my_dct(a)
	idct = my_idct(dct)
	print(dct)
	print(idct)
    #print("[1, 2, 3, 4, 5, 6, 7, 8] is:", my_dct(a))
    #print("[1, 2, 3, 4, 5, 6, 7, 8] is:", my_idct(my_dct([1, 2, 3, 4, 5, 6, 7, 8])))
