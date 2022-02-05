# Ke Shi on Feb 4th, 2022
def Insertion_Sort(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    for i in range(1,len(nums)):
        for j in range(i-1):
            if nums[j]> nums[i]:
                nums[j],nums[i] = nums[i], nums[j]
    return nums

def SystemSort(nums):
    nums.sort()
    return nums