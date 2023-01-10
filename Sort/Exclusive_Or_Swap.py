# Ke Shi on Feb 3rd, 2022

def Exclusive_Or_Swap(x,y):
    """
    :param x: int
    :param y: int
    :return: null
    """
    x = x^y
    y = x^y
    x = x^y
    print(x,y)

x = 10
y = 20
Exclusive_Or_Swap(x,y)


