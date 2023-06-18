# Ke Shi on July 11th, 2022

class node:
    def __init__(self,element,next = None):
        self.element = element
        self.next = next

def divide_based_on_pivot(head, pivot):
    lst = []
    head_copy = head
    while head:
        lst.append(head.element)
        head = head.next
    length = len(lst)
    i = 0
    start_point = 0
    mid_point = 0
    end_point = length - 1
    while mid_point <= end_point:
        if lst[i] < pivot:
            lst[i], lst[start_point] = lst[start_point], lst[i]
            start_point += 1
            mid_point += 1
            i += 1
        elif lst[i] > pivot:
            lst[i], lst[end_point] = lst[end_point], lst[i]
            end_point -= 1
        else:
            lst[mid_point], lst[i] = lst[i], lst[mid_point]
            mid_point += 1
            i += 1
    print(lst)
    j = 0
    head = head_copy
    while j < length:
        head_copy.element = lst[j]
        head_copy = head_copy.next
        j += 1
    return head

def divide_based_on_pivot2(head, pivot):
    small_head = node(None)
    mid_head = node(None)
    big_head = node(None)
    while head:
        if head.element < pivot:
            if small_head.element == None:
                small_head.element = head.element
                tmp = small_head
            else:
                tmp.next = node(None)
                tmp = tmp.next
                tmp.element = head.element
        elif head.element > pivot:
            if big_head.element == None:
                big_head.element = head.element
                tmp2 = big_head
            else:
                tmp2.next = node(None)
                tmp2 = tmp2.next
                tmp2.element = head.element
        else:
            if mid_head.element == None:
                mid_head.element = head.element
                tmp3 = mid_head
            else:
                tmp3.next = node(None)
                tmp3 = tmp3.next
                tmp3.element = head.element
        head = head.next
    if small_head.element != None:
        if mid_head.element != None:
            tmp.next = mid_head
            if big_head.element != None:
                tmp3.next = big_head
        elif big_head.element != None:
            tmp.next = big_head
        return small_head
    if mid_head.element != None:
        if big_head.element != None:
            tmp3.next = big_head
        return mid_head
    if big_head != None:
        return big_head
    else:
        return None


l1 = node(3)
l1.next = node(2)
l1.next.next = node(1)
l1.next.next.next = node(9)
divide_based_on_pivot(l1, 2)
l11 = divide_based_on_pivot2(l1, 2)

l2 = node(3)
l2.next = node(2)
l2.next.next = node(1)
l2.next.next.next = node(1)
l2.next.next.next.next = node(2)
l2.next.next.next.next.next = node(3)
divide_based_on_pivot(l2, 2)
l21 = divide_based_on_pivot2(l2, 2)

l3 = node(3)
l3.next = node(2)
l3.next.next = node(1)
l3.next.next.next = node(4)
l3.next.next.next.next = node(7)
l3.next.next.next.next.next = node(3)
divide_based_on_pivot(l3, 3)
l31 = divide_based_on_pivot2(l3, 3)