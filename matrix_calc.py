import numpy as np

matrix1 = []

def matrice_multiply1():
    print("Matrix one")
    num_rows = int(input("Enter the number of rows: "))
    num_columns = int(input("Enter the number of columns: "))

    for i in range(num_rows):
        row = []
        for j in range(num_columns):
            try:
                cell_value = input("Enter value for row {} column {}: ".format(i+1, j+1))
                row.append(int(cell_value))
            except ValueError:
                row.append(float(cell_value))
        matrix1.append(row)

    print("[", end='')
    for i, row in enumerate(matrix1):
        print('[', end='')
        for j, cell in enumerate(row):
            print(cell, end='')
            if j < num_columns - 1:
                print(', ', end='')
        print(']', end='')
        if i < num_rows - 1:
            print(',')
    print(']')


    matrix = np.array(matrix1)

    return matrix
    
def matrice_multiply2_sum(matrix1):
    print("Matrix 2")
    num_rows = int(input("Enter the number of rows: "))
    num_columns = int(input("Enter the number of columns: "))

    matrix2 = []
    
    for i in range(num_rows):
        row = []
        for j in range(num_columns):
            try:
                cell_value = input("Enter value for row {} column {}: ".format(i+1, j+1))
                row.append(int(cell_value))
            except ValueError:
                row.append(float(cell_value))
        matrix2.append(row)

    print("[", end='')
    for i, row in enumerate(matrix2):
        print('[', end='')
        for j, cell in enumerate(row):
            print(cell, end='')
            if j < num_columns - 1:
                print(', ', end='')
        print(']', end='')
        if i < num_rows - 1:
            print(',')
    print(']')


    matrix = np.array(matrix1)
                
    matrix2 = np.array(matrix2)

    # calculate the dot product of the two matrices
    result = np.dot(matrix, matrix2)

    print("matrix1 x matrix2: \n",result)
    
    
matrice_multiply1()
matrice_multiply2_sum(matrix1)
