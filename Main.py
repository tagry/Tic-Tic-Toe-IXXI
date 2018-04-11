import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while True:
    opponent_row, opponent_col = [int(i) for i in input().split()]
    valid_action_count = int(input())
    for i in range(valid_action_count):
        row, col = [int(j) for j in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print("0 0")