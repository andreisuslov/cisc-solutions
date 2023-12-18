import math
import sys

def euclidean_distance(vector1, vector2):
    sum_of_squares = 0
    for i in range(len(vector1)):
        difference = vector1[i] - vector2[i]
        sum_of_squares += difference ** 2
    return math.sqrt(sum_of_squares)

vector1 = list(map(float, sys.argv[1].split(',')))
vector2 = list(map(float, sys.argv[2].split(',')))

distance = euclidean_distance(vector1, vector2)
print(f"{distance:.4f}")
