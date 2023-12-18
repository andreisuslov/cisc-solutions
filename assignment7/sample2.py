import random
import sys
import stdarray
import stdio

def main():
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    voters = []

    for _ in range(n):
        voters.append(stdio.readString())

    random.shuffle(voters)
    for i in range(m):
        stdio.writeln(voters[i])

if __name__ == "__main__":
    main()
