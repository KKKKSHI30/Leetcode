# Ke Shi on Feb 10th, 2022
def Reverse_Order_Pair(nums):
    """
    :param nums: List[int]
    :return: List[tuple]
    """
    if len(nums) == 1 or len(nums) == 0:
        return []
    return process(nums,0,len(nums)-1)

def process(nums,left,right):
    """
    :param nums: List[int]
    :param left: int
    :param right: int
    :return: List[tuple]
    """
    if left == right:
        return []
    mid = (left + right) //2
    print("in process, ",nums[left:mid+1], "and ", nums[mid+1:right+1])
    nums2 = []
    nums2.extend(process(nums,left, mid))
    nums2.extend(process(nums, mid+1,right))
    nums2.extend(merge(nums,left,mid,right))
    #return process(nums,left, mid) + process(nums, mid+1,right) + merge(nums,left,mid,right)
    return nums2

"""
A = [1,3,4,2,5]
= [5,4,3,2,1]
= 2 tuple
= (3,2),(4,2)
"""

def merge(nums,left,mid,right):
    """
    :param nums: List[int]
    :param left: int
    :param mid: int
    :param right: int
    :return: List[tuple]
    """
    lst = []
    i,j = left, mid+1
    total = 0
    nums2 = []
    for k in range(right - left +1):
        if i == (mid +1):
            lst.extend(nums[j:right+1])
            print("here")
            print(f"lst is {lst}")
            break
        elif j == (right +1):
            lst.extend(nums[i:mid+1])
            print("here2")
            print(f"lst is {lst}")
            break
        elif nums[j] < nums[i]:
            lst.append(nums[i])
            total += right - j + 1
            print("here3")
            print(f"lst is {lst}")
            nums2.append((nums[i],nums[j]))
            i += 1
        else:
            lst.append(nums[j])
            j += 1
            print("here4")
            print(f"lst is {lst}")

    for k in range(len(lst)):
        nums[left] = lst[k]
        left += 1
    print(f"nums is {nums} right now.")
    print(f"nums2 is {nums2}")
    return nums2

A = [1,3,4,2,5]
print(Reverse_Order_Pair(A))







