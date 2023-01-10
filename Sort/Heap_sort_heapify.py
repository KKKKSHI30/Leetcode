# Ke Shi on Feb 18th, 2022
# quicker than heap_sort
def heap_sort_heapify(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    if (len(nums) == 0) or (len(nums) == 1) :
        return nums
    else:
        i = len(nums)-1
        while (i >=0):
            heapify(nums,i,len(nums))
            i -=1
    heapSize = len(nums)
    nums[0],nums[heapSize-1] = nums[heapSize-1],nums[0]
    heapSize -= 1
    while (heapSize > 0):
        heapify(nums,0,heapSize-1)
        nums[0], nums[heapSize-1] = nums[heapSize-1], nums[0]
        heapSize -= 1
    return nums


def heapify(nums,index,heapSize):
    """
    :param nums: List[int]
    :param index: int
    :param heapSize: int
    :return: List[int]
    """
    left = index * 2 + 1
    while(left < heapSize): # there is left tree
        if (left +1 < heapSize) & (nums[left+1] > nums[left]):
            largest = left+1
        else:
            largest = left
        if nums[largest] < nums[index]:  # the parent and the bigger child node compare
            largest = index
        if largest == index: break
        nums[largest],nums[index] = nums[index],nums[largest]
        index = largest
        left = index*2+1
    return nums

A = [3,5,2,7,3,4,9]
print(heap_sort_heapify(A))