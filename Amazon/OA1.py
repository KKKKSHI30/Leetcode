import math
import heapq


def findRestaurants(allLocations, numRestaurants):
    def distanceFromCustomer(restPos):
        x, y = restPos
        return math.sqrt(x ** 2 + y ** 2)

    if not allLocations:
        return [[]]

    heap = []
    for loc in allLocations:
        locDist = distanceFromCustomer(loc)
        xDist = abs(loc[0])
        heap.append((locDist, xDist, loc))

    heapq.heapify(heap)

    result = []
    for i in range(numRestaurants):
        nextMin = heapq.heappop(heap)
        result.append(nextMin[2])

    return result

allLocations = [[1,2],[3,4],[1,-1]]
numRestaurants = 2
findRestaurants(allLocations,numRestaurants)


"""
Q2: 1. I used a min priority queue (heap) to solve this problem.
Firstly, add all locations to the heap sort by distance, then by x distance. 
Secondly, pop minimum from heap for numRestaurants number of times and add to the result array. 
2. Let n = size of allLocations and m = numRestaurants. 
Compute distance and add  element to heap take O(1) times, 
we do this for every location so that is O(n) tims, 
heapify a list of n elements also take O(n) times. 
Pop for heap takes log(n) times and we did that for numRestaurants number of times. 
The answer is O(n + mlogn)
"""