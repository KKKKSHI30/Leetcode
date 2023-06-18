def flip(n):
    return n^1

# 非负数返回1， 负数返回1
def sign(n):
    return flip((n >> 31) & 1)

def max(a,b):
    c = a - b
    sa = sign(a)
    sb = sign(b)
    sc = sign(c)
    dif_sab = sa ^ sb
    same_sab = flip(sa ^ sb)
    returnA = dif_sab * sa + same_sab * sc
    returnB = flip(returnA)
    return returnA * a + returnB * b

max(3,5)