import sys
import math

x = float(sys.argv[1])  # x-coordinate
y = float(sys.argv[2])  # y-coordinate

r = math.sqrt(x**2 + y**2)
theta = math.atan2(y, x)

theta_degrees = math.degrees(theta)

print(f"r = {r:.2f}")
print(f"theta = {theta_degrees:.2f}")