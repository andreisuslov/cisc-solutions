import math
import sys

x1, y1, x2, y2 = map(float, sys.argv[1:])

x1_rad = math.radians(x1)
y1_rad = math.radians(y1)
x2_rad = math.radians(x2)
y2_rad = math.radians(y2)

d = 60 * math.acos(math.sin(x1_rad) * math.sin(x2_rad) + math.cos(x1_rad) * math.cos(x2_rad) * math.cos(y1_rad - y2_rad))
print(f"Great-circle distance: {d:.2f} nautical miles")