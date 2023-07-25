# Ke Shi on June 6th, 2022
# PositionalList from chap 7
class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'  # streamline memory

        def __init__(self, element, prev, next):  # initialize node's fields
            self._element = element  # user's element
            self._prev = prev  # previous node reference
            self._next = next  # next node reference

    def __init__(self):
        """Create and empty list."""
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer    # trailer is after header
        self._trailer._prev = self._header    # header is before trailer
        self._size = 0                        # number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor,successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self,node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._elemnt          # record deleted element
        node._prev = node._next = node._element = None  # deprecate node
        return element                  # return deleted element

class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    #---------------nested Position class-----------
    class Position:
        """An abstraction representing the location of a single element."""
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Psition."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self,other):
            """Return True if other does not represent the same location."""
            return not (self == other)        # opposite of __eq__

    #--------------utility method-------------
    def _validate(self,p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:       # convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p.node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None         # boundary violation
        else:
            return self.Position(self,node)     # legitimate position

    #-------------------accessors-----------------
    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the lsit."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #----------------------- mutators---------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)     # inherited method returns element

    def replace(self, p, e):
        """Replace the element at Position p with e.

        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element      # temporarily store old element
        original._element = e              # replace with new element
        return old_value


# 9.1 The Priority Queues
# 9.2 Implementing a Priority Queue
# 9.2.1 The composition Design Pattern
class PriorityQueueBase:
    """Abstract base class for priority queue."""

    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key  # compare item based on their keys

    def is_empty(self):  # concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0

# 9.2.2 Implementation with an Unsorted List
class UnsortedPriorityQueue(PriorityQueueBase): # base class defines _Item
    """A min-oriented priority queue implemented with an unsorted list."""

    def _find_min(self):  # nonpublic utility
        """Return Position of iem with minimum key."""
        if self.is_empty():   # is_empty inheirted from base class
            raise ValueError("Priority queue is empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                if walk.element() < small.element():
                    small = walk
                walk = self._data.after(walk)
        return small

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)

# 9.2.3 Implemenetation with a Sorted List
class SortedPriorityQueue(PriorityQueueBase): # base class defines _Item
    """A min-oriented priority queue implemeneted with a sorted list"""
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        newest = self._Item(key,value) # make new instance
        walk = self._data.last()   # walk backward looking for smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)   # new key is smallest
        else:
            self._data.add_after(walk, newest)  # newest goes after walk

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        item = self._data.delete(self._data.first())
        return (item._key, item._value)

# 9.3 Heaps
class HeapPriorityQueue(PriorityQueueBase): # base class defines _Item
    """A min-oriented priority queue implemented with a binary heap."""
    # -------------nonpublic behaviors--------------------
    def _parent(self, j):
        return (j-1) //2

    def _left(self,j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)   # recur at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    # ----------------public behaviors--------------------
    """
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []
    """

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key,value))
        self._upheap(len(self._data) - 1)  # upheap newly added position

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        self._swap(0, len(self._data) - 1)  # put minimum item at the end
        item = self._data.pop()   # and remove it from the list
        self._downheap(0)    # then fix new root
        return (item._key, item._value)

    def __init__(self, contents = ()):
        """Create a new priority queue.

        By default, queue will be empty. If contents is given, it should be as an iterable
        sequence of (k,v) tuples specifying the initial contents.
        """
        self._data = [self._Item(k,v) for k,v in contents] # empty by default
        if len(self._data) > 1:
            self._heapify()

    def _heapify(self):
        start = self._parent(len(self) - 1)  # start at PARENT of last leaf
        for j in range(start, -1, -1):    # going to and including the root
            self._downheap(j)

# 9.4 Sorting with a priority queue

# 9.5 Adaptable Priority Queues
class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a binary heap."""

    # ------------------nested Locator class-----------------
    class Locator(HeapPriorityQueue._Item):
        """Token for locating an entry of the priority queue."""
        __slots__ = '_index'

        def __init__(self,k,v,j):
            super().__init__(k,v)
            self._index = j

    # ------------------nonpublic behaviors--------------------
    def _swap(self, i, j):
        super()._swap(i,j)
        self._data[i]._index = i    # reset locator index (post-swap)
        self._data[j]._index = j    # reset locator index (post-swap)

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self,key,value):
        """Add a key-value pair."""
        token = self.Locator(key,value,len(self._data)) # initialize locator index
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self,loc,newkey,newval):
        """Update the key and value for the entry identified by Locator loc."""
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc):
        """Remove and return the (k,v) pair identified by Locator loc."""
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        if j == len(self) - 1:  # item at last position
            self._data.pop()  # just remov it
        else:
            self._swap(j, len(self)- 1)    # swap item to the last position
            self._data.pop()
            self._bubble(j)
        return (loc._key, loc._value)















