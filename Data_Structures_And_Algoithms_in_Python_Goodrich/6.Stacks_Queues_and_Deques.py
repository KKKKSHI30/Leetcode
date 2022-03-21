# Ke Shi on Mar 21st, 2022
# 6.1 Stacks
# 6.1.2 Simple Array-Based Stack
class ArrayStack:
    """LIFO stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """Create an empty stack."""
        self._data = []    # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self,e):
        """Add element e to the top of the stack."""
        self._data.append(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise ValueError('Stack is emtpy')
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._data.pop()

S = ArrayStack()
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
print(S.is_empty())
print(S.pop())
print(S.is_empty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)

# 6.1.3 Reversing Data Using a Stack
def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n')) # we will re-insert newlines when writing
    original.close()

    # now we overwrite with contents in LIFO order
    output = open(filename,'w')  # reopening file overwrites original
    while not S.is_empty():
        output.write(S.pop() + '\n')   # re-insert newline characters
    output.close()

# 6.1.4 Matching Parenthesis and HTML Tags
def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack()
    j = raw.find('<')  # find first '<' character (if any)
    while j != -1:
        k = raw.find('>', j+1) # find next '>' character
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:        # this is closing tag
            if S.is_empty():
                return False
            if tag[1:]  != S.pop():
                return False
        j = raw.find('<', k+1)    # find next '<' character (if any)
    return S.is_empty()

# 6.2 Queues






