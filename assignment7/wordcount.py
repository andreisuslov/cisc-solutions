import stdio

def main():
    word_count = 0

    while not stdio.isEmpty():
        line = stdio.readLine()
        words = line.split()
        word_count += len(words)

    stdio.writeln(str(word_count))

if __name__ == "__main__":
    main()
