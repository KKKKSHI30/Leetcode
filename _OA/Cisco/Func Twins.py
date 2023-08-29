from collections import Counter
def check_twin(arr):
    arr = sorted(arr)
    counter = Counter(arr)
    for num in arr:
        if counter[num] == 1:
            return num
    return -1

check_twin([-2,1])
check_twin([1,1])
check_twin([5,3,6,2,3,6])