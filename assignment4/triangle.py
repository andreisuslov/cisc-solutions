import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

result = not (a >= b + c or b >= a + c or c >= a + b)

print(result)

