def create_new_string(s):
    # manacher算法
    s = list(s)
    new_s = []
    for i in s:
        new_s.append("#")
        new_s.append(i)
    new_s.append("#")
    return new_s

def longest_palindrome(s):
    s = create_new_string(s)
    center = -1
    radius = -1
    max_value = -1
    ptr = []
    for i in range(len(s)):
        if radius > i:
            ptr.append(min((2*center - i), radius - i))
        else:
            ptr.append(1)
        # 至少不用验的区域
        while (i + ptr[i] < len(s) and i - ptr[i] > -1):
            # 虽然不同情况不同分析，但是每个都测一下也是ok
            if (s[i + ptr[i]] == s[i - ptr[i]]):
                ptr[i] += 1
            else:
                break
        if i + ptr[i] > radius:
            radius = i + ptr[i]
            center = i
        max_value = max(max_value, ptr[i])
    return max_value - 1

longest_palindrome("abcba")


