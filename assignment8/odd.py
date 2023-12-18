# odd.py
# Andrei Suslov
# CISC 120-91
import sys
import stdio

def is_odd_true(a, b, c):
    count_true = sum([a, b, c])
    return count_true % 2 == 1

if len(sys.argv) != 4:
    stdio.writeln("Usage: python odd.py <value1> <value2> <value3>")
else:
    values = [bool(int(arg)) for arg in sys.argv[1:4]]

    result = is_odd_true(*values)
    stdio.writeln(result)

