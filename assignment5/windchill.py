import sys

def calculate_wind_chill(t, v):
    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)
    return w

if len(sys.argv) != 3:
    print("ERROR: Invalid number of input arguments")
    sys.exit(1)

t = float(sys.argv[1])
v = float(sys.argv[2])

if not (-58 < t < 41) or v < 2:
    print("ERROR: Invalid input argument value")
else:
    w = calculate_wind_chill(t, v)
    print(f"{w:.2f}")
