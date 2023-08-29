# 题目: https://www.1point3acres.com/bbs/thread-1011199-1-1.html
def findMinimumEffort(developerSkill, k):
    developerSkill.sort()
    m = k
    sm = 0
    sm1 = 0
    j = 0
    j1 = m
    ind = m // 2
    # Initial effort for the first m developers
    for i in range(m // 2):
        sm += developerSkill[i]
        sm1 += developerSkill[(m + 1) // 2 + i]
    ans = sm1 - sm
    # Sliding window approach to calculate the effort
    for i in range((m + 1) // 2, len(developerSkill) - (m + 1) // 2):
        sm += (developerSkill[ind] - developerSkill[j])
        sm1 += (developerSkill[j1] - developerSkill[i])
        ans = min(ans, sm1 - sm)
        ind += 1
        j += 1
        j1 += 1
    return ans
findMinimumEffort([10, 12, 14, 4, 5, 7, 100, 101], 3)