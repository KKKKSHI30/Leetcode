# Ke Shi on Feb 4th, 2022

# Question:
# There is a list with one number with odd appearance and all the other number has even appearances.
# print out the even number in the list
import math

def oddAppearceNum(nums):
    """
    :param nums: List[int]
    :return: int
    """
    final = 0
    for i in range(len(nums)):
        final = nums[i] ^ final
    return final


A = [1,2,3,4,5,4,3,2,1]
print(oddAppearceNum(A))

# Question2: NOT SOLVED
# There is a list with two number with odd appearance and all the other number has even appearance, find the two
# number separately
# Not Solved
def oddAppearceTwoNumber(nums):
    """
    :param nums: List[int]
    :return: (int,int)
    """
    final = 0
    for i in range(len(nums)):
        final = nums[i] ^ final

    onlyone = 0
    for i in range(len(nums)):
        if(nums[i] & onlyone == onlyone): ## Seperate the bit on specific one into two parts
            onlyone = nums[i] ^ onlyone

    return onlyone,onlyone^final

A = [1,1,2,3,2,3,5,6,7,7,13,14,13,14]
print(oddAppearceTwoNumber(A))

def getFirstSetBitPos(n):
    return math.log2(n & -n) + 1


