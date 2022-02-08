# Ke Shi on Feb 7th, 2022
def get_max(nums):
    """
    :param nums: List[int]
    :return: int
    """
    return process(nums,0,len(nums)-1)

def process(nums,left, right):
    if left == right:
        return nums[left]

    for i in range(left,right+1):
        print(nums[i])

    mid = (left+right)//2
    leftmax = process(nums,left,mid)
    rightmax= process(nums,mid+1,right)
    return max(leftmax,rightmax)

A = [1,2,3,4,3,2,1,8]
get_max(A)