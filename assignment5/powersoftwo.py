import sys

n = int(sys.argv[1])
power = 1

while power <= n:
    print(power, end=' ')
    power *= 2
