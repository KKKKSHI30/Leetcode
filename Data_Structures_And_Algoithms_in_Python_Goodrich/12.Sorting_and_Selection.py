# Ke Shi on June 13th, 2022
# 12 Sorting and Selection
# 12.1 Why Study Sorting Algorithms?

# 12.2 Merge-Sort
import math
from random import random


def merge(S1, S2, S):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]     # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]    # copy jth element of S2 as next item of S
            j += 1

def merge_sort(S):
    """Sort the elements of Pytho list S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return           # list is already sorted
    # divide
    mid = n//2
    S1 = S[0:mid]     # copy of first half
    S2 = S[mid:n]     # copy of second half
    # conquer (with recursion)
    merge_sort(S1)    # sort copy of first half
    merge_sort(S2)    # sort copy of second half
    # merge results
    merge(S1, S2, S)     # merge sorted halves back into S

def merge2(S1, S2, S):
    """Merge two sorted queue instances S1 and S2 into empty queue S."""
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    while not S1.is_empty():     # move remaining elements of S1 to S
        S.enqueue(S1.dequeue())
    while not S2.is_empty():     # move remianing element of S2 to S
        S.enqueue(S2.dequeue())

def merge_sort2(S):
    """Sort the elements of queue S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return     # list if already sorted
    # divide
    S1 = LinkedQueue()    # or any other queue implementation
    S2 = LinkedQueue()
    while len(S1) < n//2:     # move the first n//2 elements to S1
        S1.enqueue(S.dequeue())
    while not S.is_empty():     # move the rest to S2
        S2.enqueue(S.dequeue())
    merge_sort2(S1)    # sort first half
    merge_sort2(S2)    # sort second half
    # merge results
    merge(S1, S2, S)    #merge sorted halves back into S

def merge3(src, result, start, inc):
    """Merge src[start:start+inc] and src[start+inc:start+2*inc] into result."""
    end1 = start + inc     # boundary for run 1
    end2 = min(start + 2*inc,len(src))    # boundary for run 2
    x, y, z = start, start + inc, start    # index into run1, run2, result
    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z]  = src[x]; x += 1  # copy form run 1 and increment x
        else:
            result[z] = src[y]; y += 1    # copy from run 2 and increment y
        z += 1                            # increment z to reflect new result
    if x < end1:
        result[z:end2] = src[x:end1]     # copy remainder of run 1 to output
    elif y < end2:
        result[z:end2] = src[y:end2]      # copy remainder of run 2 to output


def merge_sort3(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    logn = math.ceil(math.log(n, 2))
    src, dest = S, [None] * n      # make temporary storage for dest
    for i in (2 ** k for k in range(logn)):     # pass i creates all runs of length 2i
        for j in range(0, n, 2*i):     # each pass merges two lengh i runs
            merge(src, dest, j, i)
        src, dest = dest, src     # reverse roles of lists
    if S is not src:
        S[0:n] = src[0:n]         # additional copy to get results to S

# 12.3 Quick-Sort
def quick_sort(S):
    """Sort the elements of queue S using the quick-sort algorithm."""
    n = len(S)
    if n < 2:
        return
    # divide
    p = S.first()    # using first as arbitrary pivot
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not S.is_empty():     # divide S into L, E, and G
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())     # S.first() must equal pivot
    quick_sort(L)    # sort element less than p
    quick_sort(G)    # sort elements greater than p
    # concatenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())

def inplace_quick_sort(S, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
    if a >= b: return         # range is trivially sorted
    pivot = S[b]      # last element of range is pivot
    left = a          # will scan rightward
    right = b - 1     # will scan leftward
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:               # scans did not strictly cross
            S[left], S[right] = S[right], S[left]       # swap values
            left, right = left + 1, right - 1           # shrink range

    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    inplace_quick_sort(S, a, left-1)
    inplace_quick_sort(S, left + 1, b)

# 12.4 Studying Sorting through an Algorithmic Lens

# 12.5 Comparing Sorting Algorithms

# 12.6 Python's Built-In Sorting Functions
def decorated_merge_sort(data, key = None):
    """Demonstration of the decorate-sort-undecorate pattern."""
    if key is not None:
        for j in range(len(data)):
            data[j] = _Item(key(data[j]), data[j])      # decorate each element
    merge_sort(data)
    if key is not None:
        for j in range(len(data)):
            data[j] = data[j]._value     #undecorate each element

# 12.7 Selection
def quick_select(S,k):
    """Return the kth smallest element of list S, for k from 1 to len(S)."""
    if len(S) == 1:
        return S[0]
    pivot = random.choice(S)      # pick random pivot element from S
    L = [x for x in S if x < pivot]    # elements less than pivot
    E = [x for x in S if x == pivot]     # elements equal to pivot
    G = [x for x in S if pivot < x]     # elements grater than pivot
    if k <= len(S):
        return quick_select(L, k)     # kth smallest lies in L
    elif k <= len(L) + len(E):
        return pivot        # kth smallest equal to pivot
    else:
        j = k - len(L) - len(E)      # new selection parameter
        return quick_select(G, j)     # kth smallest is jth in G











