# sigmoid.py
# Andrei Suslov
# CISC 120-91
import sys
import stdio
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

if len(sys.argv) != 2:
    stdio.writeln("Usage: python sigmoid.py <number>")
else:
    x = float(sys.argv[1])
    result = sigmoid(x)
    stdio.writef("%.3f\n", result)
