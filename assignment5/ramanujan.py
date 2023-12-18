import sys

n = int(sys.argv[1])
results = []
for a in range(1, int(n ** (1 / 3)) + 1):
    for b in range(a, int(n ** (1 / 3)) + 1):  
        for c in range(1, int(n ** (1 / 3)) + 1):
            for d in range(c, int(n ** (1 / 3)) + 1):  
                if a ** 3 + b ** 3 == c ** 3 + d ** 3 and a != c and a != d and b != c and b != d:
                    found = False
                    for result in results:
                        if result[1] == a ** 3 + b ** 3:
                            found = True
                            break
                    if not found:
                        results.append(((a, b, c, d), a ** 3 + b ** 3))
for result in results:
    print(f"{result[0][0]}^3 + {result[0][1]}^3 = {result[0][2]}^3 + {result[0][3]}^3 = {result[1]}")