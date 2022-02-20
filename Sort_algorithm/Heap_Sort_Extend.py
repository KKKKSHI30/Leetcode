# Ke Shi on Feb 19th, 2022
from queue import PriorityQueue


def sort_array_distance_less_k(nums, k):
    """
    :param nums: List[int]
    :param k: int
    :return: List[int]
    """
    pq = PriorityQueue()
    for i in range(k):
        pq.put(nums[i])
    print(pq.queue)
    index = 0
    for j in range(len(nums) - k):
        nums[index] = pq.get()
        pq.put(nums[j + k])
        index += 1

    for k in range(k):
        nums[index] = pq.get()
        index += 1
    print(nums)
    return nums


A = [1, 3, 2, 4, 5, 8, 7, 9]
print(sort_array_distance_less_k(A, 3))
