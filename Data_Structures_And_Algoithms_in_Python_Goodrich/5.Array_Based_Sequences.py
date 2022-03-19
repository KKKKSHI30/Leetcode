# Ke Shi on Mar 18st, 2022
# 5.1 Python's Sequence Types
# 5.2 Low-Level Arrays
# 5.3 Dynamic Arrays and Amortization
import sys
data = []
for k in range(20):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length:{0:3d}; Size in bytes: {1:4d}'.format(a,b))
    data.append(None)

# 5.3.1 Implementing a Dynamic Array
import ctypes

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        """Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self,obj):
        """Add object to end of the array."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self,c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self,c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()

    def insert(self,k,value):
        """Insert value at index k, shifting subsequent values rightward."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1

    def remove(self,value):
        """Remove first occurrence of value (or raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n-1):
                    self._A[j] = self._A[j+1]
                self._A[self._n-1] = None
                self._n -= 1
                return
        raise ValueError('Value not found')

# 5.3.3 Python's List Class
from time import time
def compute_average(n):
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / n

# 5.4 Efficiency of Python's Sequence Types
# 5.4.2 Python's String Class
letters = ''
file = "abc"
for c in file:
    if c.isalpha():
        letters += c

temp = []
for c in file:
    if c.isalpha():
        temp.append(c)
    letters = ''.join(temp)

letters = ''.join(c for c in file if c.isalpha())


