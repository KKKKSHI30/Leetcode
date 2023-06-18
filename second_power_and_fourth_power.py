def is2power(num):
    # 二次幂只有一个1， 拿到最右边的1，然后和0比较一下，看看是不是只有一个1就行了
    return (num & (num -1)) == 0

def is4power(num):
    # 四次幂是不是只有一个1，还必须是奇数位上
    return (num & (num -1)) == 0 and (num & 0x55555555) != 0




is2power(5)
is2power(4)
is4power(4)
is4power(8)
is4power(16)