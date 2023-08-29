# 题目: https://www.1point3acres.com/bbs/thread-1009988-1-1.html

# A utility function to calculate area
# of triangle formed by (x1, y1),
# (x2, y2) and (x3, y3)

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


# A function to check whether point P(x, y)
# lies inside the triangle formed by
# A(x1, y1), B(x2, y2) and C(x3, y3)
def isInside(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    A = area(x1, y1, x2, y2, x3, y3)
    if A == 0:
        return 0
    p, q = False, False

    A1 = area(xp, yp, x2, y2, x3, y3)
    A2 = area(x1, y1, xp, yp, x3, y3)
    A3 = area(x1, y1, x2, y2, xp, yp)
    if (A == A1 + A2 + A3):
        p = True
    A4 = area(xq, yq, x2, y2, x3, y3)
    A5 = area(x1, y1, xq, yq, x3, y3)
    A6 = area(x1, y1, x2, y2, xq, yq)
    if (A == A4+A5+A6):
        q = True
    if p and q:
        return 3
    if p and not q:
        return 1
    if not p and q:
        return 2
    if not p and not q:
        return 4

isInside(0,0,2,0,4,0,2,0,4,0)
isInside(3,1,7,1,5,5,3,1,0,0)
isInside(3,1,7,1,5,5,1,1,4,3)
isInside(3,1,7,1,5,5,5,2,6,3)
isInside(3,1,7,1,5,5,1,1,2,2)