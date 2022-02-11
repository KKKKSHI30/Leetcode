def Dutch_Flag_Pre(lst,num):
    """
    :param lst: List[int]
    :param num: int
    :return: List[int]
    """
    j = 0 # for left bound
    for i in range(len(lst)):
        if lst[i] > num:
            continue
        else:
            lst[j],lst[i] = lst[i],lst[j]
            j += 1
    return lst


def Dutch_Flag_Problem(lst,num):
    """
    :param lst: List[int]
    :param num: int
    :return: List[int]
    """
    j, k = 0, len(lst)-1
    for i in range(len(lst)):
        if lst[i] > num:
            lst[i],lst[k] = lst[k],lst[i]
            i -= 1
            k -= 1
        elif lst[i] < num:
            lst[j],lst[i] = lst[i],lst[j]
            j +=1
        else:
            continue
    return lst



A = [3,7,5,2,2,6,8,2,3,6,7,8]
b = 6
print(Dutch_Flag_Pre(A,b))
print(Dutch_Flag_Problem(A,b))
