# Ke Shi on Feb 4th, 2022


def Insertion_Sort(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    for i in range(1, len(nums)):
        for j in range(i - 1):
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
    return nums


A = [1, 2, 3, 4, 5, 7, 2, 3, 5, 6]
Insertion_Sort(A)
