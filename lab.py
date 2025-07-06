#lab2: write a program  to read element of 20 list convert it into array and perform add, sub, mul and transpose of matrices
import numpy as np
matrix=[]
n=int(input("enter number of rows: "))
m=int(input("enter number of columns: "))
print("enter elements of matrix1: ")
for i in range(n):
  row=[]
  for j in range(m):
    e=int(input())
    row.append(e)
  matrix.append(row)

matrix2=[]
print("enter elements of matrix1: ")
for i in range(n):
  row2=[]
  for j in range(m):
    a=int(input())
    row2.append(a)
  matrix.append(row2)


a1=np.array(matrix)
b1=np.array(matrix2)
c=a1+b1    
print("addition: ", c)

