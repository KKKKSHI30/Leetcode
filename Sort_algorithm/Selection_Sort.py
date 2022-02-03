# Ke Shi on Feb 2nd, 2022

def SelectionSort(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums


A = [64, 25, 12, 22, 11]
SelectionSort(A)