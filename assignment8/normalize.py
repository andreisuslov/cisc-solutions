# normalize.py
# Andrei Suslov
# CISC 120-91
import stdio
import stdarray

def normalize(values):
    # Implement the normalization logic
    min_val = min(values)
    max_val = max(values)
    return [(x - min_val) / (max_val - min_val) for x in values]

# Main section of the script
values = stdarray.readFloat1D()
normalized_values = normalize(values)
for val in normalized_values:
    stdio.writef("%.3f ", val)
stdio.writeln()
