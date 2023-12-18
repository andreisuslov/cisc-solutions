import sys

def is_strictly_between_0_and_1(value):
    return 0.0 < value < 1.0

if len(sys.argv) != 2:
    print("False")
else:
    argument = float(sys.argv[1])
    print(is_strictly_between_0_and_1(argument))
