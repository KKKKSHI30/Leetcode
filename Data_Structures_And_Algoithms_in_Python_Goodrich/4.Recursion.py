# Ke Shi on Mar 14st, 2022
# 4.1 Experimental Studies

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 4.1.2 Drawing an English Ruler
def draw_line(tick_length, tick_label = ''):
    """Draw one line with given tick length(followed by optional label),"""
    line = '-'* tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:          # stop when length drops to 0
        draw_interval(center_length - 1)     #recursively draw top ticks
        draw_line(center_length)     # draw center tick
        draw_interval(center_length - 1)     # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length."""
    draw_line(major_length,'0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)  # draw interior ticks for inch
        draw_line(major_length, str(j))    # draw inch j line and label

draw_ruler(3,4)

# 4.1.3 Binary Search
def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive
    """
    if low > high:
        return False      # interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]:   # found a match
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid-1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)

# 4.1.4 File Systems
import os
def disk_usage(path):
    """Return the number of bytes used by a file/folder and descendents."""
    total = os.path.getsize(path) # account for direct usage
    if os.path.isdir(path):       # if this is a directory,
        for filename in os.listdir(path):  # then for each child:
            childpath = os.path.join(path, filename) # compose full path to child
            total += disk_usage(childpath)  # add child's usage to total
    print('{0:<7}'.format(total),path)   # descriptive output(optional)
    return total

# 4.2 Analyzing Recursive Algorithms

# 4.3 Recursion Run Amok
def unique1(S):
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False

def unique3(S, start, stop):
    if stop - start <= 1: return True
    elif not unique1(S, start, stop-1): return False
    elif not unique1(S, start + 1, stop): return False
    else: return S[start] != S[stop - 1]

def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)

def good_fibonacci(n):
    if n <= 1:
        return (n,0)
    else:
        (a,b) = good_fibonacci(n-1)
        return(a+b, a)

# 4.3.1 Maximum Recursive Depth in Python
import sys
old = sys.getrecursionlimit()
sys.setrecursionlimit(10000)

# 4.4 Further Examples of Recursion
# 4.4.1 Linear Recursion
def linear_sum(S,n):
    """Return the sum of the first n numbers of sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

def reverse(S, start, stop):
    if start < stop-1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start +1, stop -1)

def power(x, n):
    """Compute the value x**n for integer n."""
    if n==0:
        return 1
    else:
        return x*power(x, n-1)












