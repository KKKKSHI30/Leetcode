# Ke Shi on July 14th, 2022

class node:
    def __init__(self,element,next = None):
        self.element = element
        self.next = next

def check_loop(head):
    """Check if there is a loop. If no loop, return None; else return the start of the loop."""
    set = []
    cur = head
    while cur:
        if id(cur) in set:
            return cur
        else:
            set.append(id(cur))
        cur = cur.next
    return None

def check_loop2(head):
    """Using fast and slow pointer"""
    if head == None:
        return None
    if head.next == None:
        return None
    fast = head.next.next
    slow = head.next
    while id(fast) != id(slow):
        if fast == None:
            return None
        elif fast.next == None:
            return None
        fast = fast.next.next
        slow = slow.next
    fast = head
    while id(fast) != id(slow):
        fast = fast.next
        slow = slow.next
    return fast

def both_no_loop(head1, head2):
    cur1 = head1
    cur2 = head2
    length1 = 0
    length2 = 0
    if cur1 == None or cur2 == None:
        return None
    while cur1.next:
        cur1 = cur1.next
        length1 += 1
    while cur2.next:
        cur2 = cur2.next
        length2 += 1
    length1 += 1
    length2 += 1
    if id(cur1) == id(cur2):
        cur1 = head1
        cur2 = head2
        diff = length1 - length2
        if diff > 0:
            while diff != 0:
                cur1 = cur1.next
                diff -= 1
        elif diff < 0:
            while diff != 0:
                cur2 = cur2.next
                diff += 1
        while id(cur1) != id(cur2):
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        return None

def both_loop(head1, head2):
    cur1 = head1
    cur2 = head2
    length1 = length2 = 0
    loop1 = check_loop2(head1)
    loop2 = check_loop2(head2)
    if loop1 == loop2:
        while id(cur1) != id(loop1):
            cur1 = cur1.next
            length1 += 1
        while id(cur2) != id(loop2):
            cur2 = cur2.next
            length2 += 1
        diff = length1 - length2
        cur1 = head1
        cur2 = head2
        if diff > 0:
            while diff != 0:
                cur1 = cur1.next
                diff -= 1
        elif diff < 0:
            while diff != 0:
                cur2 = cur2.next
                diff += 1
        while id(cur1) != id(cur2):
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        cur1 = loop1.next
        while cur1 != loop1:
            if cur1 == loop2:
                return cur1
            else:
                cur1 = cur1.next
        return None


def linked_list_intersect(head1, head2):
    """check if two list intersect or not, if intersect, return the first point they intersect, if not
    return None"""
    result1 = check_loop2(head1)
    result2 = check_loop2(head2)
    if result1 == result2 == None:
        return both_no_loop(head1, head2)
    elif result1 != None and result2 != None:
        return both_loop(head1, head2)
    else:
        return None

l1 = node(3)
l2 = node(2)
l3 = node(1)
l4 = node(9)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l2
# l1_return = check_loop(l1)
l1_return2 = check_loop2(l1)
l11 = node(3)
l21 = node(2)
l31 = node(1)
l41 = node(9)
l11.next = l21
l21.next = l31
l31.next = l41
l41.next = l21
l12_return = check_loop2(l11)
result1 = both_loop(l1, l11)

l12 = node(3)
l22 = node(2)
l32 = node(1)
l12.next = l22
l22.next = l32
l32.next = l3
l13_return = check_loop2(l12)
result2 = both_loop(l1, l12)

l5 = node(1)
l6 = node(2)
l7 = node(3)
l8 = node(4)
l5.next = l6
l6.next = l7
l7.next = l8
# l5_return = check_loop(l5)
l5_return2 = check_loop2(l5)

l9 = node(5)
l10 = node(6)
l9.next = l10
l10.next = l7
l9_return = check_loop2(l9)

no_loop1 = both_no_loop(l5, l9)
no_loop2 = both_no_loop(l9, l5)

final_result1 = linked_list_intersect(l1,l11)
final_result2 = linked_list_intersect(l1,l12)
final_result3 = linked_list_intersect(l1,l5)
final_result4 = linked_list_intersect(l5, l9)
