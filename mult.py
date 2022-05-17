import numpy as np
import os
os.system("clear")
print("Matrices will be multiplied as AxB NOT BxA")
print("input matrix A, inputting every value from left to right and up to down")
A = np.array([[int(input()), int(input()), int(input())] for x in range(3)])
print("input the transposed version of matrix B")
B = np.array([[int(input()), int(input()), int(input())] for x in range(3)])
ANS = [[[] for x in range(3)] for x in range(3)]
for x in range(3):
	for y in range(3):
		ANS[x][y] = sum(np.multiply(A[x], B[y]))
os.system("clear")
print(str(np.matrix(ANS)).translate({ord("[") : "", ord("]") : ""}))
