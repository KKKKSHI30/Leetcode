# Ke Shi on Feb 21th, 2022
def Radix_Sort(nums):
    """
    for non-negative value
    :param nums: List[int]
    :return: List[int]
    """
    if len(nums) == 0 or len(nums) == 1:
        return nums
    else:
        radix_sort(nums,0,len(nums)-1,maxbits(nums))

def maxbits(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    max_value = nums[0]
    for i in range(len(nums)):
        max_value = max(max_value,nums[i])
    bit = 0
    while (max_value != 0):
        max_value = max_value//10
        bit += 1
    return bit

def get_digit(number, digit):
    """
    :param number: int
    :param digit: int
    :return: int
    """
    return int(number/pow(10,digit-1)%10)


def radix_sort(nums,left,right,digit):
    """
    :param nums: List[int]
    :param left: int
    :param right: int
    :param digit: int
    :return: List[int]
    """
    radix = 10
    i, j = 0,0
    bucket = []
    count = [0]*10

