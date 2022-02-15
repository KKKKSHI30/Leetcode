import random
def Quick_Sort(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    if len(nums) == 0 or len(nums) == 1:
        return nums
    Sort(nums, 0, len(nums) - 1)
    print(nums)
    return nums

def Sort(nums,left,right):
    """
    :param nums: List[int]
    :param left: int
    :param right: int
    :return: List[int]
    """
    if left == right:
        return nums
    else:
        chosen = nums[random.randint(left,right)]
        p = partition(nums,chosen,left,right)
        Sort(nums,left,p[0])
        Sort(nums,p[1],right)
        return nums

def partition(nums,chosen,left,right):
    """
    :param nums: List[int]
    :param chosen: int
    :param left: int
    :param right: int
    :return: tuple
    """
    i, j, k = left,left, right
    while i < (k+1):
        if nums[i] > chosen:
            nums[i],nums[k] = nums[k],nums[i]
            k -= 1
        elif nums[i] < chosen:
            nums[j],nums[i] = nums[i],nums[j]
            j +=1
            i +=1
        else:
            i +=1
            continue
    return (max(left,j-1),min(k+1,right))
# max(left, j-1) is for if j doesn't change, it will not exceed the array




A = [3,6,2,5,4,7,4,7,2,7,9,2]
Quick_Sort(A)







