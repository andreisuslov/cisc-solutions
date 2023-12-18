import sys
import math

P = float(sys.argv[1])  # Principal amount
r = float(sys.argv[2])  # Annual interest rate
t = float(sys.argv[3])  # Number of years

amount = P * math.exp(r * t)

print("Amount after", t, "years:", amount)