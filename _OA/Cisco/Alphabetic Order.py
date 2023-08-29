def is_sorted_alphabetically(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return i+1
    return 0

is_sorted_alphabetically("abc")
is_sorted_alphabetically("asd")