# cannot handle negative case
def add(a, b):
    sum = a
    while b != 0:
        sum = a ^ b
        b = (a & b) << 1
        a = sum
    return sum

def neg_num(n):
    return add(~n, 1)

def minus(a, b):
    return add(a, neg_num(b))

def multi(a, b):
    res = 0
    while b != 0:
        if ((b & 1) != 0):
            res = add(res, a)
        a = a << 1
        b = b >> 1
    return res

def isNeg(n):
    return n < 0

# cannot handle negative cases, might change in add function
def div(a, b):
    x = neg_num(a) if isNeg(a) else a
    y = neg_num(b) if isNeg(b) else b
    res = 0
    i = 31
    while i > -1:
        if ((x >> i) >= y):
            res |= (1 << i)
            x = minus(x, y << i)
        i = minus(i, 1)
    return neg_num(res) if isNeg(a) ^ isNeg(b) else res

def divide(a, b):
    if b == 0:
        return False
    if (a == float("-Inf") and (b == float("-Inf"))):
        return 1
    elif (b == float("-Inf")):
        return 0
    elif (a == float("-Inf")):
        res = div(add(a, 1), b)
        return add(res, div(minus(a, multi(res, b)), b))
    else:
        return div(a,b)

add(3,5)
minus(3,5)
multi(3,5)
divide(6,3)