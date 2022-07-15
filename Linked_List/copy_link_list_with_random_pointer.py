# Ke Shi on July 11th, 2022

class node:
    def __init__(self,element, next = None, rand = None):
        self.element = element
        self.next = next
        self.rand = rand

def copy_linked_list_with_random_pointer(head):
    map = {}
    cur = head
    while cur:
        map[cur] = node(cur.element)
        cur = cur.next
    cur = head
    while cur:
        try:
            map[cur].next = map[cur.next]
        except:
            map[cur].next = None
        try:
            map[cur].rand = map[cur.rand]
        except:
            map[cur].rand = None
        cur = cur.next
    return map[head]

def copy_linked_list_with_random_pointer2(head):
    cur = head
    while cur:
        cur_next = cur.next
        cur.next = node(cur.element)
        cur.next.next = cur_next
        cur = cur_next
    cur = head
    cur_copy = cur.next
    while cur:
        cur_copy.rand = cur.rand.next
        cur = cur_copy.next
        if cur == None:
            break
        cur_copy = cur.next
    return head.next



l1 = node(3)
l2 = node(2)
l3 = node(1)
l4 = node(9)
l1.next = l2
l2.next = l3
l3.next = l4
l1.rand = l3
l2.rand = l1
l3.rand = l4
l4.rand = l1
# l5 = copy_linked_list_with_random_pointer(l1)
l6 = copy_linked_list_with_random_pointer2(l1)

