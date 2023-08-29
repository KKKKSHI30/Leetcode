# 题目: https://www.1point3acres.com/bbs/thread-1007376-1-1.html
def warehouse(center, d):
    # center = (-2,1,0), d = 8
    left, right = min(center)-d//2-1, max(center)+d//2+1
    def check(point):
        total_distance = 0
        for i in center:
            total_distance += abs(i-point)*2
        if total_distance > d:
            return False
        else:
            return True
    def find_bound(sign):
        l, r = left, right
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                if sign:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if sign:
                    l = mid+1
                else:
                    r = mid-1
        return l
    left_bound = find_bound(True)  # left_bound可以，left_bound-1不可以
    right_bound = find_bound(False) # right_bound不可以，right_bound-1可以
    return right_bound - left_bound

warehouse([-2,1,0], 8)
