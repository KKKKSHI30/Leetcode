# Lexicographically Next Permutation of given String
# a) Traverse from the right and find the first item that is not following the ascending order.
# For example in “abedc”, the character ‘b’ does not follow the ascending order.
# b) Swap the found character with the closest greater (or smallest greater) element on the right side of it.
# In the case of “abedc”, we have ‘c’ as the closest greater element. After swapping ‘b’ and ‘c’, the string becomes “acedb”.
# c) After swapping, reverse the string after the position of the character found in step a.
# After reversing the substring “edb” of “acedb”, we get “acbde” which is the required next permutation.
def next_permutation(s: str) -> str:
    # Convert the input string to a list of characters
    arr = list(s)
    n = len(arr)
    i = n - 2

    # Find the largest index i such that arr[i] < arr[i+1]
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    # If no such index exists, return "No next Permutation"
    if i < 0:
        return "No next Permutation possible"
    j = n - 1

    # Find the largest index j such that arr[i] < arr[j]
    while j >= 0 and arr[j] <= arr[i]:
        j -= 1
    # Swap arr[i] and arr[j]
    arr[i], arr[j] = arr[j], arr[i]
    # Reverse the sublist arr[start:end+1]
    rev(arr, i + 1, n - 1)
    return ''.join(arr)


# Function to reverse the array
def rev(arr: list, start: int, end: int) -> None:
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1



# Driver code
if __name__ == '__main__':
    s2 = "gfg"
    s = "abedc"
    s3 = "abcfde"
    print(next_permutation(s3))

