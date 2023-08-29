def count_set_bits(number):
    count = 0
    while number > 0:
        count += number & 1
        number >>= 1
    return count

# Example usage
num = int(input("Enter a number: "))
bit_count = count_set_bits(num)
print("Number of set bits:", bit_count)
