import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

is_ascending = x < y < z
is_descending = x > y > z

print(is_ascending or is_descending)