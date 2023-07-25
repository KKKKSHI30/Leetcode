# stack Approach
# Time: O(n)
# Space: O(1)
# 2023.07.18: yes
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        total = 0
        if len(tokens) == 1:
            total = int(tokens[0])
        s = []
        for i in tokens:
            if i in ("+", "-", "*", "/"):
                second = int(s.pop())
                first = int(s.pop())
                if i == "+":
                    total = first+second
                elif i == "-":
                    total = first - second
                elif i == "*":
                    total = first*second
                else:
                    total = int(first/second)
                s.append(total)
            else:
                s.append(i)
        return total

    def evalRPN2(self, tokens):
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }
        stack = []
        for token in tokens:
            if token in operations:
                number_2 = stack.pop()
                number_1 = stack.pop()
                operation = operations[token]
                stack.append(operation(number_1, number_2))
            else:
                stack.append(int(token))
        return stack.pop()


# Reducing the List In-place Approach
# Time: O(n^2)
# Space: O(1)
# 2023.07.18: yes
# notes: 可以，但是意义不大，写法参考意义不错
class Solution2(object):
    def evalRPN(self, tokens):
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }
        current_position = 0

        while len(tokens) > 1:

            # Move the current position pointer to the next operator.
            while tokens[current_position] not in "+-*/":
                current_position += 1

            # Extract the operator and numbers from the list.
            operator = tokens[current_position]
            number_1 = int(tokens[current_position - 2])
            number_2 = int(tokens[current_position - 1])

            # Calculate the result to overwrite the operator with.
            operation = operations[operator]
            tokens[current_position] = operation(number_1, number_2)

            # Remove the numbers and move the pointer to the position
            # after the new number we just added.
            tokens.pop(current_position - 2)
            tokens.pop(current_position - 2)
            current_position -= 1

        return tokens[0]


# Tests:
test = Solution()
test.evalRPN(["18"])
test.evalRPN2(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
test.evalRPN(["2","1","+","3","*"])
test.evalRPN(["4","13","5","/","+"])

