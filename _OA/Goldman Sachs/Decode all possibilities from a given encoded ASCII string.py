solutions = []
currentSolution = ''
unprocessed = ''


def decode(s):
    flipped = s[::-1]
    global solutions
    global unprocessed
    global currentSolution
    currentSolution = ''
    unprocessed = flipped
    _decode()
    return solutions


def is_valid(split):
    if split.startswith('0'):
        return False
    value = int(split)
    if value < 65 or value > 122 and value != 32:
        return False
    return True


def _decode():
    global unprocessed
    global currentSolution
    global solutions
    if len(unprocessed) == 0:
        solutions.append(currentSolution)
    else:
        possible_splits = list()
        possible_splits.append(unprocessed[0:2])
        possible_splits.append(unprocessed[0:3])

        for split in possible_splits:
            if is_valid(split):
                decoded_character = chr(int(split))
                currentSolution += decoded_character
                unprocessed = unprocessed[len(split):]
                _decode()
                currentSolution = currentSolution[0: len(currentSolution) - 1]
                unprocessed = split + unprocessed



decode('0018014111117811180180110127')
decode("23511011501782351112179911801562340161171141148")


# 不愧是我，类似LC91
class Solution:
    def numDecodings(self, encoded):
        encoded = encoded[::-1]
        dp = [0 for _ in range(len(encoded) + 1)]
        dp[0] = 0
        dp[1] = 1
        if 99 >= int(encoded[1:3]) >= 10:
            dp[2] = 2
        else:
            dp[2] = 1
        for i in range(3, len(dp)):
            two_digit = int(encoded[i-1:i+1])
            if 10 <= two_digit <= 99:
                dp[i] = dp[i - 2]
            three_digit = int(encoded[i - 2: i+1])
            if 100 <= three_digit <= 126:
                dp[i] += dp[i - 3]
        return dp[len(encoded)-1]
# Test:
test = Solution()
test.numDecodings("0018014111117811180180110127")