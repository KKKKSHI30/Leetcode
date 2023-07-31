def predictDays(day, k):
    nonIncreasingCount = []
    nonIncStart = 0
    for i in range(len(day)):
        if i == 0 or day[i] <= day[i-1]:
            nonIncreasingCount.append(i-nonIncStart)
        else:
            nonIncreasingCount.append(0)
            nonIncStart = i

    nonDecreasingCount = []
    nonDecStart = len(day) - 1
    for i in range(len(day)-1, -1, -1):
        if i == len(day)-1 or day[i] <= day[i+1]:
            nonDecreasingCount.append(nonDecStart - i)
        else:
            nonDecreasingCount.append(0)
            nonDecStart = i
    nonDecreasingCount.reverse()

    print(nonIncreasingCount)
    print(nonDecreasingCount)

    result = []
    for i in range(len(day)):
        if nonIncreasingCount[i] >= k and nonDecreasingCount[i] >= k:
            result.append(i+1)
    return result


days1 = [1,0,1,0,1]
k1 = 1
days2 = [1,0,0,0,1]
k2 = 2
days3 = [1,1,1,1,1,1,1,1,1,1]
k3 = 3
predictDays(days2, k2)

"""
Q4: 1. This is a 3 pass solution. Firstly, iterate from left to right and calculate non increasing 
count for each index.
Secondly, iterate from right to left and calculate non decreasing count for each index.
Thridly, we iterate over all index, and find indexes that satisfy the
condition by indexing into the count array we created during the first 2 iteration.
2. in total we iterate the array 3 times, for each single element in each iteration,
we are only during O(1) time operations. So each iteration take O(n) times and we did it 3 times,
3*O(n) is still O(n).
"""