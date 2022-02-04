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

# Question2:
# There is a list with two number with odd appearance and all the other number has even appearance, find the two
# number separately

def getFirstSetBitPos(n):
    return math.log2(n & -n) + 1

def oddAppearceTwoNumber(nums):
    """
    :param nums: List[int]
    :return: (int,int)
    """
    # find the exclusive or for two numbers
    final = 0
    for i in range(len(nums)):
        final = nums[i] ^ final

    # the number right shift n steps for the rightmost one
    n = getFirstSetBitPos(final)

    onlyone = 0
    # shift right for n times and %2 to seperate two categories to do exlusive or
    for i in range(len(nums)):
        if((nums[i] >> int(n)) % 2 == 0 ): ## Seperate the bit on specific one into two parts
            onlyone = nums[i] ^ onlyone

    #do the exclusive or to seperate these two numbers
    return onlyone,onlyone^final

A = [1,1,2,3,2,3,5,6,7,7,13,14,13,14]
print(oddAppearceTwoNumber(A))



