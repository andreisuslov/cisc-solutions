# max3.py
# Andrei Suslov
# CISC 120-91
import sys
import stdio

def max3(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if len(sys.argv) != 4:
    stdio.writeln("Usage: python max3.py <number1> <number2> <number3>")
else:
    first = float(sys.argv[1])
    second = float(sys.argv[2])
    third = float(sys.argv[3])

    biggest = max3(first, second, third)
    stdio.writef("The largest number is: %.0f\n", biggest)
