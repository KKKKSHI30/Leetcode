def print_alternating_pattern(n):
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("W", end=" ")
            else:
                print("B", end=" ")
        print()


print_alternating_pattern(3)