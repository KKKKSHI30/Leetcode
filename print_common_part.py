# Ke Shi on July 9th, 2022

class node:
    def __init__(self,element,next = None):
        self.element = element
        self.next = next

l1 = node(0)
l1.next = node(2)
l1.next.next = node(4)
l1.next.next.next = node(9)
print(l1.element, l1.next.element, l1.next.next.element, l1.next.next.next.element)

l2 = node(1)
l2.next = node(2)
l2.next.next = node(9)
l2.next.next.next = node(15)
print(l2.element, l2.next.element, l2.next.next.element, l2.next.next.next.element)

def common_part(head1, head2):
    while (head1 and head2):
        if head1.element < head2.element:
            head1 = head1.next
        elif head1.element > head2.element:
            head2 = head2.next
        else:
            print(head1.element)
            head1 = head1.next
            head2 = head2.next

common_part(l1,l2)