# Exhaustive Search [Time Limit Exceeded]
# Time: O(2^n)
# Space: O(tx*ty)
# 2023.07.17: yes
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        if sx > tx or sy > ty: return False
        if sx == tx and sy == ty: return True
        return self.reachingPoints(sx+sy, sy, tx, ty) or \
               self.reachingPoints(sx, sx+sy, tx, ty)


# Dynamic Programming [Time Limit Exceeded]
# Time: O(tx*ty)
# Space: O(tx*ty)
# 2023.07.17: yes
class Solution2(object):
    def reachingPoints(self, sx, sy, tx, ty):
        seen = set()
        def search(x, y):
            if (x, y) in seen: return
            if x > tx or y > ty: return
            seen.add((x, y))
            search(x+y, y)
            search(x, x+y)

        search(sx, sy)
        return (tx, ty) in seen

# Work Backwards [Time Limit Exceeded]
# Time: O(max(tx, ty))
# Space: O(1)
# 2023.07.17: yes
# notes: Every parent point (x, y) has two children, (x, x+y) and (x+y, y).
# However, every point (x, y) only has one parent candidate (x-y, y) if x >= y, else (x, y-x).
# This is because we never have points with negative coordinates.
# notes: 这是最关键的一句，因为coordinate不能为负，所以每次一个parent只能有一个child
class Solution3(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty: return True
            if tx > ty:
                tx -= ty
            else:
                ty -= tx
        return False

# Work Backwards (Modulo Variant)
# Time: O(log(max(tx, ty)))
# Space: O(1)
# 2023.07.17: yes
# notes: 承接上一个方法，如果一个点已经比开始坐标点小了，或者想等，说明他和初始坐标系中只有一种节点转换可能(tx-sx)%ty即可
class Solution4(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy

# Tests:
test = Solution4()
test.reachingPoints(sx = 1, sy = 1, tx = 3, ty = 5)
