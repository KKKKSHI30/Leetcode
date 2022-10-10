import string
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s = list(s)
        result = ""
        for i in range(len(s)):
            if s[i] == " " and result == "":
                i += 1
                continue
            elif s[i] == " " and result != "":
                break
            if s[i] == "+" and result == "":
                result += s[i]
                continue
            elif s[i] == "+" and result != "":
                break
            if s[i] == "-" and result == "":
                result += s[i]
                continue
            elif s[i] == "-" and result == "":
                break
            if s[i].isnumeric():
                result += s[i]
                continue
            if not s[i].isnumeric():
                break
        if result == "" or result == "+"  or result == "-":
            return 0
        result = int(result)
        if result > 2**31 -1:
            result = 2**31 -1
        elif result < -2**31:
            result = -2**31
        return result


class Solution2:
    def myAtoi(self, input: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(input)

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        # Discard all spaces from the beginning of the input string.
        while index < n and input[index] == ' ':
            index += 1

        # sign = +1, if it's positive number, otherwise sign = -1.
        if index < n and input[index] == '+':
            sign = 1
            index += 1
        elif index < n and input[index] == '-':
            sign = -1
            index += 1

        # Traverse next digits of input and stop if it is not a digit.
        # End of string is also non-digit character.
        while index < n and input[index].isdigit():
            digit = int(input[index])

            # Check overflow and underflow conditions.
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.
                return INT_MAX if sign == 1 else INT_MIN

            # Append current digit to the result.
            result = 10 * result + digit
            index += 1

        # We have formed a valid number without any overflow/underflow.
        # Return it after multiplying it with its sign.
        return sign * result


class StateMachine:
    def __init__(self):
        self.State = {"q0": 1, "q1": 2, "q2": 3, "qd": 4}
        self.INT_MAX, self.INT_MIN = pow(2, 31) - 1, -pow(2, 31)

        # Store current state value.
        self.__current_state = self.State["q0"]
        # Store result formed and its sign.
        self.__result = 0
        self.__sign = 1

    def to_state_q1(self, ch: chr) -> None:
        """Transition to state q1."""
        self.__sign = -1 if (ch == '-') else 1
        self.__current_state = self.State["q1"]

    def to_state_q2(self, digit: int) -> None:
        """Transition to state q2."""
        self.__current_state = self.State["q2"]
        self.append_digit(digit)

    def to_state_qd(self) -> None:
        """Transition to dead state qd."""
        self.__current_state = self.State["qd"]

    def append_digit(self, digit: int) -> None:
        """Append digit to result, if out of range return clamped value."""
        if ((self.__result > self.INT_MAX // 10) or
                (self.__result == self.INT_MAX // 10 and digit > self.INT_MAX % 10)):
            if self.__sign == 1:
                # If sign is 1, clamp result to INT_MAX.
                self.__result = self.INT_MAX
            else:
                # If sign is -1, clamp result to INT_MIN.
                self.__result = self.INT_MIN
                self.__sign = 1

            # When the 32-bit int range is exceeded, a dead state is reached.
            self.to_state_qd()
        else:
            # Append current digit to the result.
            self.__result = (self.__result * 10) + digit

    def transition(self, ch: chr) -> None:
        """Change state based on current input character."""
        if self.__current_state == self.State["q0"]:
            # Beginning state of the string (or some whitespaces are skipped).
            if ch == ' ':
                # Current character is a whitespaces.
                # We stay in same state.
                return
            elif ch == '-' or ch == '+':
                # Current character is a sign.
                self.to_state_q1(ch)
            elif ch.isdigit():
                # Current character is a digit.
                self.to_state_q2(int(ch))
            else:
                # Current character is not a space/sign/digit.
                # Reached a dead state.
                self.to_state_qd()

        elif self.__current_state == self.State["q1"] or self.__current_state == self.State["q2"]:
            # Previous character was a sign or digit.
            if ch.isdigit():
                # Current character is a digit.
                self.to_state_q2(int(ch))
            else:
                # Current character is not a digit.
                # Reached a dead state.
                self.to_state_qd()

    def get_integer(self) -> None:
        """Return the final result formed with it's sign."""
        return self.__sign * self.__result

    def get_state(self) -> None:
        """Get current state."""
        return self.__current_state


class Solution3:
    def myAtoi(self, input: str) -> int:
        q = StateMachine()

        for ch in input:
            q.transition(ch)
            if q.get_state() == q.State["qd"]:
                break

        return q.get_integer()
test = Solution()
test.myAtoi("+12")
test.myAtoi("words and 987")
