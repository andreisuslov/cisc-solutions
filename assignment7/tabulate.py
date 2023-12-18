import stdio

def main():
    while not stdio.isEmpty():
        line = stdio.readLine()
        parts = line.split()

        name = parts[0]
        num1 = int(parts[1])
        num2 = int(parts[2])

        result = num1 / num2
        stdio.writef("%-10s %4d %5d %8.3f\n", name, num1, num2, result)

if __name__ == "__main__":
    main()
