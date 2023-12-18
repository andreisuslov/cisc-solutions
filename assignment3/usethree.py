import stdio
import sys

if len(sys.argv) < 4:
    stdio.writeln('Please provide three names as arguments.')
    sys.exit()

stdio.write('Hi ')
stdio.write(sys.argv[3])
stdio.write(', ')
stdio.write(sys.argv[2])
stdio.write(', and ')
stdio.write(sys.argv[1])
stdio.writeln('.')
