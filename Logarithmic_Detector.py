# Ke Shi on Feb 5th, 2022
import copy
import random
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

def logarithmic_Detector():
    MAX_SIZE = 100
    MAX_NUMBER = 100
    lst = [0] *MAX_SIZE
    for i in range(MAX_SIZE):
        lst[i] = random.randint(0,MAX_NUMBER)
        print(lst[i])
    lst2 = copy.deepcopy(lst)
    Insertion_Sort(lst)
    SystemSort(lst2)
    if (lst == lst2):
        print("success")
    else:
        print("NO")

