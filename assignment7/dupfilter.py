import stdio

def main():
    previous = None

    while not stdio.isEmpty():
        current = stdio.readInt()

        if current != previous:
            if previous is not None:
                stdio.write(" ")
            stdio.write(str(current))
            previous = current

    stdio.writeln()

if __name__ == "__main__":
    main()
