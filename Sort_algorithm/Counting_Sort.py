# Ke Shi on Feb 21st, 2022
from itertools import repeat
def counting_sort(nums):
    """
    :param nums: List[int], int 0-200
    :return: List[int]
    """
    lst = [0] * 11
    for i in range(len(nums)):
        lst[nums[i]] += 1

    nums2 = []
    for i in range(len(lst)):
        if lst[i] != 0:
            nums2.extend(repeat(i, lst[i]))
    return nums2

A = [5,2,3,6,8,7,7,7]
print(counting_sort(A))
