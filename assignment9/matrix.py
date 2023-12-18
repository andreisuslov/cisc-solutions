#-------------
# matrix.py
# Andrei Suslov
# CISC 120-91
#-------------

import random

def rand(m, n):
    """Create an m-by-n matrix with random floats between 0 and 1."""
    return [[random.random() for _ in range(n)] for _ in range(m)]

def identity(n):
    """Create an n-by-n identity matrix."""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def dot(v1, v2):
    """Compute the dot product of vectors v1 and v2."""
    return sum(x * y for x, y in zip(v1, v2))

def transpose(matrix):
    """Transpose the matrix."""
    return list(map(list, zip(*matrix)))

def add(m1, m2):
    """Add two matrices."""
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

def subtract(m1, m2):
    """Subtract two matrices."""
    return [[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

def multiplyMM(m1, m2):
    """Multiply two matrices."""
    return [[sum(m1[i][k] * m2[k][j] for k in range(len(m1[0]))) for j in range(len(m2[0]))] for i in range(len(m1))]

def multiplyMV(m, v):
    """Multiply a matrix by a vector."""
    return [sum(m[i][j] * v[j] for j in range(len(m[0]))) for i in range(len(m))]

def multiplyVM(v, m):
    """Multiply a vector by a matrix."""
    return [sum(v[j] * m[j][i] for j in range(len(m))) for i in range(len(m[0]))]

def main():
    # Sample matrices for demonstration
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]

    # Demonstrate matrix addition
    print("Matrix A:")
    print_matrix(matrix_a)
    print("Matrix B:")
    print_matrix(matrix_b)

    print("Matrix A + B:")
    result = add(matrix_a, matrix_b)  # Updated function name
    print_matrix(result)

    # Demonstrate matrix subtraction
    print("Matrix A - B:")
    result = subtract(matrix_a, matrix_b)  # Updated function name
    print_matrix(result)

    # Demonstrate matrix multiplication
    print("Matrix A * B:")
    result = multiplyMM(matrix_a, matrix_b)  # Updated function name
    print_matrix(result)

    # Add demonstrations for other functions as needed

def print_matrix(matrix):
    """Utility function to print a matrix."""
    for row in matrix:
        print(' '.join(map(str, row)))
    print()

if __name__ == "__main__":
    main()
