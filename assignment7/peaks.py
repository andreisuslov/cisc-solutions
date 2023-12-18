import stdarray
import stdio

def is_peak(grid, row, col):
    current = grid[row][col]

    if row > 0 and grid[row - 1][col] >= current: return False
    if row < len(grid) - 1 and grid[row + 1][col] >= current: return False
    if col > 0 and grid[row][col - 1] >= current: return False
    if col < len(grid[0]) - 1 and grid[row][col + 1] >= current: return False

    return True

def main():
    terrain = stdarray.readFloat2D()

    num_peaks = 0
    for row in range(len(terrain)):
        for col in range(len(terrain[row])):
            if is_peak(terrain, row, col):
                num_peaks += 1

    stdio.writeln(num_peaks)

if __name__ == "__main__":
    main()
