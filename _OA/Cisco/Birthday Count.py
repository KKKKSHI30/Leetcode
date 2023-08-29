def find_day(arr):
    res = 0
    map = {}
    for num in arr:
        map[num] = map.get(num, 0) + 1
    for key in map:
        result = map[key]
        if result % 2 == 1:
            res += 1
    return res
# Example usage
arr = [4, 8, 2, 8, 9]
print(find_day(arr))