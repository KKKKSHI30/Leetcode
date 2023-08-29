from collections import Counter

def calculate_mean(arr):
    return round(sum(arr) / len(arr), 2)

def calculate_mode(arr):
    count = Counter(arr)
    mode = max(count, key=count.get)
    return mode

# Example usage
arr = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7]
mean = calculate_mean(arr)
mode = calculate_mode(arr)
print("Mean:", mean)
print("Mode:", mode)
