#!/usr/bin/python3
"""args divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """matrix must be list of lists or floats"""

    e1 = "matrix must be a matrix (list of lists) of integers/floats"
    e2 = "Each row of the matrix must have the same size"
    e3 = "Div must be a number"
    e4 = "Division by 0"
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError(e1)
    for i in range(len(matrix)):
        if type(matrix[i]) != list or len(matrix[i]) == 0:
            raise TypeError(e1)
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError(e1)
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError(e2)
    if type(div) not in [int, float]:
        raise TypeError(e3)
    if div == 0:
        raise ZeroDivisionError(e4)
    newmatrix = [list(map(lambda cc: round(cc / div, 2), rc)) for rc in matrix]
    return newmatrix
