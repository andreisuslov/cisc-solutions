# signum.py
# Andrei Suslov
# CISC 120-91
import sys
import stdio

def signum(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

if len(sys.argv) != 2:
    stdio.writeln("Usage: python signum.py <number>")
else:
    x = float(sys.argv[1])
    result = signum(x)
    stdio.writeln(result)
