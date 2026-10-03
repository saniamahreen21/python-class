obstacles = [(1, 2), (3, 3), (0, 4)]

for row in range(5):
    for col in range(5):
        if (row, col) in obstacles:
            print("#", end="")
        else:
            print(".", end="")
    print()