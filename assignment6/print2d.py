import sys
import ast

def print_2d_array(arr):
    for row in arr:
        for val in row:
            print('*' if val else ' ', end='')
        print()

arr = ast.literal_eval(sys.argv[1])
print_2d_array(arr)