# # An ideal number is a positive integer that has only 3 and 5 as prime divisons，
# an ideal number can be exposed in the form of 3^x * 5^y, where x and y are non-negative integers.
# For example, 15, 45 and 75 are ideal but 6, 10, 21 are not.  Find
# the number of ideal integers within the given segment[low, high] inclusive.
def perfectNum(low, high):
    arr_3 = []
    arr_35 = []
    x = 1
    while x <= high:
        arr_3.append(x)
        x *= 3

    for x in arr_3:
        while x <= high:
            if x >= low:
                arr_35.append(x)
            x *= 5
    return len(arr_35)


perfectNum(20, 730)
perfectNum(200,405)
perfectNum(1,1)
