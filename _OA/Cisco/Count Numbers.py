def count_numbers_brute_force(x, y):
	count = 0

	def sum_digit(num):
		total = 0
		while num:
			total += num % 10
			num //= 10
		return total

	for i in range(1, x + 1):
		if sum_digit(i) == y:
			count += 1

	return -1 if count == 0 else count

count_numbers_brute_force(20,5)



# New methods
# https://www.tutorialspoint.com/count-numbers-smaller-than-or-equal-to-n-with-given-digit-sum-in-cplusplus
def funcDigits(number, sum):
	dp = [[[-1 for _ in range(162)] for _ in range(2)] for _ in range(18)]
	def solve(i, tight, sum_so_far, Sum, number, length):
		if i == length:

			# If sum_so_far equals to given
			# sum then return 1 else 0
			if sum_so_far == Sum:
				return 1
			else:
				return 0

		ans = dp[i][tight][sum_so_far]
		if ans != -1:
			return ans

		ans = 0
		for currdigit in range(0, 10):

			currdigitstr = str(currdigit)

			# Our constructed number should
			# not become greater than N.
			if not tight and currdigitstr > number[i]:
				break

			# If tight is true then it will also be true for (i+1) digit.
			ntight = tight or currdigitstr < number[i]
			nsum_so_far = sum_so_far + currdigit
			ans += solve(i + 1, ntight, nsum_so_far, Sum, number, length)

		return ans
	print(solve(0, 0, 0, sum, str(number), len(str(number))))
funcDigits(20,5)

