# Ke Shi on Aug 7th, 2022

def hanoi(num):
    if num > 0:
        process(num, "left", "right", "middle")

def process(n, start, end, other):
    if n == 1:
        print(f"move 1 from {start} to {end}")
    else:
        process(n-1, start, other, end)
        print(f"move {n} from {start} to {end}")
        process(n-1, other, end, start)

hanoi(3)