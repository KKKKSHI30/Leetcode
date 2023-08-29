# 题目: https://leetcode.com/discuss/interview-question/object-oriented-design/3694878/OA:-max-LENGTH-of-perfect-set
def perfectSet(arr):
    arr = sorted(arr)
    hashtable = {}   # number: times
    for i in arr:
        if i in hashtable:
            hashtable[i**2] = hashtable[i]+1
        else:
            hashtable[i**2] = 1
    return max(hashtable.values())

# Tests:
perfectSet([3, 9, 4, 2, 16])