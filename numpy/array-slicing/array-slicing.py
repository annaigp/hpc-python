import numpy as np

my_list=[[1., 2, 4.5, 3],[1,2,3,4],[5,6,7,8],[1,3,5,7]]

matrix = np.array(my_list)
print(matrix)

second_row = matrix[1,:]
print(second_row)

third_column = matrix[:,2]
print(third_column)

matrix[:2,:2] = 0.21 
print(matrix)

matrix8 = np.zeros((8,8),'int')

matrix8[::2,::2] = 1
matrix8[1::2,1::2] = 1
print(matrix8)


