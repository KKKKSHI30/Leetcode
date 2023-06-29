# Ke Shi on Feb 17th, 2022
def heap_sort(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    if (len(nums) == 0) or (len(nums) == 1):
        return nums
    else:
        # for i in range(len(nums)):
        #    print(heap_insert(nums,i))
        # notes: 重点，这里是O(N)，因为可以看做是从右到左一个个heapify子树，把子树堆好了，再搞父树
        i = len(nums) - 1
        while i >= 0:
            heapify(nums, i, len(nums))
            i -= 1

    heapSize = len(nums)
    nums[0], nums[heapSize - 1] = nums[heapSize - 1], nums[0]
    heapSize -= 1
    while heapSize > 0:
        heapify(nums, 0, heapSize)
        nums[0], nums[heapSize - 1] = nums[heapSize - 1], nums[0]
        heapSize -= 1
    return nums


def heap_insert(nums, index):
    """
    :param nums: List[nums]
    :param index: num
    :return: List[nums]
    """
    while nums[index] > nums[max((index - 1) // 2, 0)]:    # 如果index比父节点大
        nums[index], nums[(index - 1) // 2] = nums[(index - 1) // 2], nums[index]   # 与父节点交换
        index = (index - 1) // 2    # 然后来到父节点的位置
    return nums


def heapify(nums, index, heapSize):
    """
    :param nums: List[int]
    :param index: int
    :param heapSize: int
    :return: List[int]
    """
    left = index * 2 + 1  # 从index开始做heapify
    while left < heapSize:  # 如果左树的值是在树内
        if (left + 1 < heapSize) & (nums[left + 1] > nums[left]):  # 如果右树也在树内，且右树大于左树
            largest = left + 1  # 大的是右树
        else:
            largest = left  # 否则大的是左树
        if nums[largest] < nums[index]:  # 比较当前节点和子树，谁值大，谁是largest
            largest = index
        if largest == index:  # 父节点已经是最大的
            break
        nums[largest], nums[index] = nums[index], nums[largest]  # 父节点不是最大的，交换，继续判断
        index = largest
        left = index * 2 + 1
    return nums


A = [3, 5, 2, 7, 3, 4, 9]
print(heap_sort(A))
