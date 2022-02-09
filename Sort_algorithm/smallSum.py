# Ke Shi on Feb 9th, 2022
def small_sum(nums):
    """
    :param nums: List[int]
    :return: int
    """
    if len(nums) == 0 or len(nums) == 1:
        return 0
    return process(nums,0,len(nums)-1)

def process(nums,left,right):
    """
    :param nums: List[int]
    :param left: int
    :param right: int
    :return: int
    """
    if left == right: # reach only one element case
        return 0
    else:
        mid = (left + right) // 2
    return process(nums,left, mid) + process(nums,mid+1, right) + merge(nums,left,mid,right)

def merge(nums,left,mid,right):
    """
    :param nums: List[int]
    :param left: int
    :param mid: int
    :param right: int
    :return: int
    """
    lst = []
    i,j = left, mid+1
    total = 0
    for k in range(right-left+1):
        if i == (mid+1):
            lst.extend(nums[j:right+1])
            break
        elif j == (right + 1):
            lst.extend(nums[i:mid+1])
            break
        elif nums[i] < nums[j]:
            total += (right - j + 1) * nums[i]
            lst.append(nums[i])
            i += 1
        else:
            lst.append(nums[j])
            j += 1
    for k in range(len(lst)):
        nums[left] = lst[k]
        left += 1
    return total

A = [1,3,4,2,5]
B = [2,5,7,5,6]
print(small_sum(A)) # 16
print(small_sum(B)) #23


