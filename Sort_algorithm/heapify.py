# Ke Shi on Feb 16th, 2022

# when the number is on index, moving down
def heapify(nums,index,heapSize):
    """
    :param nums: List[int]
    :param index: int
    :param heapSize: int
    :return: List[int]
    """
    left = index * 2 + 1
    while(left < index): # there is left tree
        if (left +1 < heapSize) & (nums[left+1] > nums[left]):
            largest = left+1
        else:
            largest = left

        if nums[largest] > nums[index]:  # the parent and the bigger child node compare
            continue
        else:
            largest = index

        if largest == index: break

        nums[largest],nums[index] = nums[index],nums[largest]
        index = largest
        left = index*2+1
    return nums

