import random
def Quick_Sort(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    if len(nums) == 0 or len(nums) == 1:
        return nums
    return Sort(nums,0,len(nums)-1)

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
        chosen = nums[random.randint(left,right-1)]
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
    j, k = 0, len(nums)-1
    for i in range(len(nums)):
        if nums[i] > chosen:
            nums[i],nums[k] = nums[k],nums[i]
            i -= 1
            k -= 1
        elif nums[i] < chosen:
            nums[j],nums[i] = nums[i],nums[j]
            j +=1
        else:
            continue
    return (j,k)




A = [3,7,5,2,2,6,8,2,3,6,7,8]
Quick_Sort(A)







