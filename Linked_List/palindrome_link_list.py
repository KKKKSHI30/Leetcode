# Ke Shi on July 10th, 2022
from queue import LifoQueue
myStack = LifoQueue()
myStack.put('a')
myStack.put('b')
myStack.put('c')
myStack.get()
myStack.get()
myStack.get()
myStack.empty()

class node:
    def __init__(self,element,next = None):
        self.element = element
        self.next = next

def palindrome_link_list(head):
    palindrome_stack = LifoQueue()
    tmp = head
    while head:
        palindrome_stack.put(head.element)
        head = head.next
    head = tmp
    while head:
        if head.element != palindrome_stack.get():
            print("False")
            return None
        else:
            head = head.next
    print("True")

def palindrome_link_list2(head):
    palindrome_stack2 = LifoQueue()
    quick = head
    slow = head
    while quick.next:
        if quick.next.next != None:
            quick = quick.next.next
            slow = slow.next
        else:
            break
    while slow:
        palindrome_stack2.put(slow.element)
        slow = slow.next
    while not palindrome_stack2.empty():
        if palindrome_stack2.get() != head.element:
            print("False")
            return None
        else:
            head = head.next
    print("True")

def palindrome_link_list3(head):
    quick = head
    slow = head
    while quick.next:
        if quick.next.next:
            quick = quick.next.next
            slow = slow.next
        else:
            break
    tmp = slow
    slow = slow.next
    now = slow
    tmp.next = None
    now = now.next
    while now:
        slow.next = tmp
        tmp = slow
        slow = now
        now = now.next
    slow.next = tmp
    while slow and head:
        if slow.element != head.element:
            print("False")
            return None
        else:
            slow = slow.next
            head = head.next
    print("True")

l1 = node(3)
l1.next = node(2)
l1.next.next = node(1)
l1.next.next.next = node(2)
l1.next.next.next.next = node(3)
print (l1.element, l1.next.element, l1.next.next.element, l1.next.next.next.element, l1.next.next.next.next.element)
palindrome_link_list(l1)
palindrome_link_list2(l1)
palindrome_link_list3(l1)

l2 = node(3)
l2.next = node(2)
l2.next.next = node(1)
l2.next.next.next = node(1)
l2.next.next.next.next = node(2)
l2.next.next.next.next.next = node(3)
print (l2.element, l2.next.element, l2.next.next.element, l2.next.next.next.element, l2.next.next.next.next.element,
       l2.next.next.next.next.next.element)
palindrome_link_list(l2)
palindrome_link_list2(l2)
palindrome_link_list3(l2)

l3 = node(3)
l3.next = node(2)
l3.next.next = node(1)
l3.next.next.next = node(4)
l3.next.next.next.next = node(7)
l3.next.next.next.next.next = node(3)
print (l3.element, l3.next.element, l3.next.next.element, l3.next.next.next.element, l3.next.next.next.next.element,
       l3.next.next.next.next.next.element)
palindrome_link_list(l3)
palindrome_link_list2(l3)
palindrome_link_list3(l3)



