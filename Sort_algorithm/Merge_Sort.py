# Ke Shi on Feb 8th, 2022
def merge_sort(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    if len(nums) == 0 or len(nums) == 1:
        return nums
    process(nums,0,len(nums)-1)
    return nums

def process(nums,left,right):
    """
    :param nums: List[int]
    :param left: int
    :param right: int
    :return: List[int]
    """
    if left == right:
        return nums
    else:
        mid = (left + right) // 2
        process(nums,left, mid)
        process(nums,mid+1, right)
        merge(nums,left,mid,right)
    return nums

def merge(nums,left,mid,right):
    """
    :param nums: List[int]
    :param left: int
    :param mid: int
    :param right: int
    :return: List[int]
    """
    lst = []
    i,j = left, mid+1
    for k in range(right-left+1):
        if i == (mid+1):
            lst.append(nums[j])
            j += 1
        elif j == (right + 1):
            lst.append(nums[i])
            i += 1
        elif nums[i] <= nums[j]:
            lst.append(nums[i])
            i += 1
        else:
            lst.append(nums[j])
            j += 1
    for k in range(len(lst)):
        nums[left] = lst[k]
        left += 1
    return lst

A = [-2,3,-5]
merge_sort(A)


