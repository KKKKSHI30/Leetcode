# Ke Shi on Feb 3rd, 2022

def BubbleSort(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    for i in reversed(range(1,len(nums))):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


A = [64, 25, 12, 22, 11]
BubbleSort(A)