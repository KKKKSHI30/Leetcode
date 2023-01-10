# Ke Shi on Feb 5th, 2022

# In a sorted list, find the left position for larger or equal than a value using Dichotomy
def FindPosition(nums,value):
    """
    :param nums: List[int]
    :param value: int
    :return:int
    """
    lo, hi = 0, len(nums) - 1
    pos = hi
    while lo <= hi:
        half = (lo+hi)//2
        if nums[half] > value:
            hi = half -1
            pos = hi
        elif value > nums[half]:
            lo = half +1
        elif nums[half] == value:
            pos = half
            if nums[half-1] == nums[half]:
                # check if we need to loop the rest of the left part
                # if the two numbers are same, we are end of the loop,
                # otherwise, the small number might still be the left side
                hi = half -1
            else:
                return pos
    return print("not in it")
A = [1,2,3,4,5]
FindPosition(A,3)
B = [1,2,2,2,2,3,3,3,3,3,4,4,5,6]
FindPosition(B,3)


# In an unsorted array,each two number next to each other is a different number,find the local minimum
# of the list
def LocalMinimum(nums):
    """
    :param nums: List[int]
    :return: int
    """
    lo, hi = 0, len(nums)-1
    if nums[lo] < nums[lo+1]:
        pos = lo
        print("1")
        return pos
    elif nums[hi] < nums[hi-1]:
        pos = hi
        print("2")
        return pos

    while lo <= hi:
        half = (lo + hi)//2
        if nums[half] < nums[half-1] and nums[half]< nums[half +1]:
            pos = half
            return pos
        elif nums[half] > nums[half +1]:
            lo = half +1
        else:
            hi = half -1

    return print("some error appears")

C = [3,2,1,4,5,6,3,2,6,8]








