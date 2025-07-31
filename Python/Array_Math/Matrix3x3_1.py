import numpy as np
matrix=np.array([[1,2,3],           #index start from 0
                 [4,5,6],
                 [7,8,9]])
print(f"\nMatrix:\n{matrix}")

#Use(row,column) Ex:index(0,0)=matrix[(0,0)]=1
print(f"r,c(0,0) is: {matrix[0,0]}")
print(f"r,c(2,1) is: {matrix[2,1]}")

#Slicing:

#Slicing row Ex: row_0 = matrix[(0,0),(0,1),(0,2),....,(0,n)] 
row_0=matrix[0,:]
print(f"Row 0 :{row_0}")

#Slicing column Ex: col_1 = matrix[(0,1),(1,1),(2,1),....,(n,1)]
col_1=matrix[:,1]
print(f"Col 1 :{col_1}")

#Slicing Sub_matrix Ex: sub_m = matrix[1:3]=matrix[(1,1),(1,2)]=
sub_matrix=matrix[0:3,0:2]
print(f"Sub_Matrix is: \n{sub_matrix}")