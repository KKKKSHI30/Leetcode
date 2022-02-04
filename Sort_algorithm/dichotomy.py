# Ke Shi on Feb 5th, 2022
# Using Dichotomy to find a number if it existed in an ordered array

# Loop
def binary_search_while(lst, value):
    lo, hi = 0, len(lst) - 1
    if value > lst[len(lst)-1] or value < lst[0]:
        return print("not in it")
    while lo <= hi:
        half = int((lo + hi) / 2)
        if lst[half] > value:
            hi = half - 1
        elif lst[half] < value:
            lo = half - 1
        elif lst[half] == value:
            return print("in it")
    return print("not in it")

A = [1,2,3,4,5]