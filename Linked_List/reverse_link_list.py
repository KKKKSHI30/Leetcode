# Ke Shi on Feb 28th, 2022

class node:
    def __init__(self,element,next = None):
        self.element = element
        self.next = next

class node2:
    def __init__(self, element, prev = None, next = None):
        self.element = element
        self.prev = prev
        self.next = next

# reverse single linked list
def reverse_single_linked_list(lst):
    new_lst = None
    if not lst or not lst.next:
        return lst
    while lst:
        tmp = lst.next
        lst.next = new_lst
        new_lst = lst
        lst = tmp
    lst = new_lst
    return lst

l1 = node(3)
l1.next = node(2)
l1.next.next = node(1)
l1.next.next.next = node(9)
print (l1.element, l1.next.element, l1.next.next.element, l1.next.next.next.element)
l = reverse_single_linked_list(l1)
print (l.element, l.next.element, l.next.next.element, l.next.next.next.element)

# reverse double linked list
def reverse_double_linked_list(head):
    while head.next != None:
        head.next, head.prev, head = head.prev, head.next, head.next
    head.next, head.prev = head.prev, None
    return head

l2 = node2(1)
l2.next = node2(2,l2,None)
l2.next.next = node2(3, l2.next, None)
l2.next.next.next = node2(4,l2.next.next, None)
print(l2.element, l2.next.element, l2.next.next.element, l2.next.next.next.element)
l = reverse_double_linked_list(l2)
print(l.element, l.next.element, l.next.next.element, l.next.next.next.element)

