def is2power(num):
    return (num & (num -1)) == 0

def is4power(num):
    return (num & (num -1)) == 0 and (num & 0x55555555) != 0




is2power(5)
is2power(4)
is4power(4)
is4power(8)
is4power(16)