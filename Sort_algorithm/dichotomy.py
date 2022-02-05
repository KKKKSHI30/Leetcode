# Ke Shi on Feb 5th, 2022
# Using Dichotomy to find a number if it existed in an ordered array
# Note: lo = half + 1 to prevent the lst[half] == value situation
# hi = half - for the similar case

# Loop
def BinarySearchWhile(lst, value):
    lo, hi = 0, len(lst) - 1
    while lo <= hi:
        half = ((lo + hi) // 2)
        if lst[half] > value:
            hi = half - 1
        elif value > lst[half]:
            lo = half + 1
        elif lst[half] == value:
            return print("in it")
    return print("not in it")

A = [1,2,3,4,5]

# Recursion

def BinarySearchRecursion(lst, value,lo,hi):
    if lst[lo] <= value <= lst[hi]:
        half = ((lo + hi) // 2)
        if lst[half] == value:
            return print("in it")
        elif lst[half] < value:
            return BinarySearchRecursion(lst,value,half+1,hi)
        else:
            return BinarySearchRecursion(lst,value,lo,half-1)
    else:
        return print("not in it")

