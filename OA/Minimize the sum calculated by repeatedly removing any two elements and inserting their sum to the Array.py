# Given N elements, you can remove any two elements from the list, note their sum,
# and add the sum to the list. Repeat these steps while there is more than a single
# element in the list. The task is to minimize the sum of these chosen sums in the end.
# Python3 implementation of the approach

import heapq
def getMinSum(arr):
	summ = 0
	heapq.heapify(arr)
	while (len(arr) > 1):
		min1 = arr.pop(0)
		heapq.heapify(arr)
		min2 = arr.pop(0)
		min_total = min1 + min2
		summ += min_total
		arr.append(min_total)
		heapq.heapify(arr)
	return summ



arr = [1,2,3,4]
getMinSum(arr)
