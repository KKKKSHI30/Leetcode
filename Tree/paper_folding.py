# Ke Shi on July 17th, 2022

class node:
    def __init__(self, element, left = None, right = None):
        self.element = element
        self.left = left
        self.right = right

def paper_folding(n):
    # True means down
    sub_pf(1, 3, True)


def sub_pf(i, n, down):
    if i > n:
        return
    sub_pf(i+1, n, True)
    print("down") if down else print("up")
    sub_pf(i+1, n, False)

paper_folding(3)



