# Ke Shi on Feb 16th, 2022

# when some number is on index, moving up
def heap_insert(nums,index):
    """
    :param nums: List[nums]
    :param index: num
    :return: List[nums]
    """
    while (nums[index] > nums[(index-1)/2]):
        nums[index],nums[(index-1)/2] = nums[(index-1)/2],nums[index]
        index = (index-1)/2
    return nums