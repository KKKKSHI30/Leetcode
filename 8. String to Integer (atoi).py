# Follow the Rules Approach
# Time: O(n)
# Space: O(1)
# 2023.06.25: yes
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        results = []
        number_started = False
        sign = False
        for i in range(len(s)):
            if s[i] == ' ':
                if number_started:
                    break
                continue
            elif s[i] == '+' and results == [] and sign == False:
                sign = True
                number_started = True
            elif s[i] == '-' and results == [] and sign == False:
                sign = True
                number_started = True
                results.append('-')
            elif s[i].isdigit():
                number_started = True
                results.append(s[i])
            else:
                break
        if len(results) == 0:
            return 0
        negative = False
        if results[0] == '-':
            negative = True
            if len(results) == 1:
                return 0
            number = int(results[1])
            results.pop(0)
        elif results[0] == "+":
            if len(results) == 1:
                return 0
            number = int(results[1])
            results.pop(0)
        else:
            number = int(results[0])
        results.pop(0)

        while results:
            number = 10 * number + int(results[0])
            results.pop(0)
        if negative:
            number = number *-1
        clamped_number = max(min(number, 2 ** 31 - 1), -2 ** 31)
        return clamped_number

# Deterministic Finite Automaton (DFA) Approach
# Time: O(n)
# Space: O(1)
# 2023.06.25: no
# notes: 非常好的方法，就是一道题写这么多真的很离谱，但是思路很巧妙，解决复杂的题可用
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


class Solution2:
    def myAtoi(self, input: str) -> int:
        q = StateMachine()

        for ch in input:
            q.transition(ch)
            if q.get_state() == q.State["qd"]:
                break
        return q.get_integer()

# Tests:
test = Solution2()
test.myAtoi("  +  413")
test.myAtoi("   +0 123")
test.myAtoi("-91283472332")
test.myAtoi("words and 987")
test.myAtoi("  -42")
test.myAtoi("42")

test.myAtoi("4193 with words")