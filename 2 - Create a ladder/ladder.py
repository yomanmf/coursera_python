import sys
num_steps = int(sys.argv[1])
step = "#"

for number in range(num_steps):
    print(" " * (num_steps - number - 1) + step * (number + 1))