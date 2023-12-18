import sys
import math

lambda_0 = float(sys.argv[1])  # Longitude of the center point
lambda_p = float(sys.argv[2])  # Longitude of the point
phi = float(sys.argv[3])       # Latitude of the point

x = lambda_p - lambda_0
y = 0.5 * math.log((1 + math.sin(math.radians(phi))) / (1 - math.sin(math.radians(phi))))

print(f"x = {x:.1f}")
print(f"y = {y:.3f}")