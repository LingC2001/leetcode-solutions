from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []
    my_dict = {"+", "-", "*", "/"}

    for value in tokens:
        if value not in my_dict:
            stack.append(int(value))
        else:
            val1 = stack.pop()
            val2 = stack.pop()

            if value == "+":
                stack.append(val2 + val1)
            elif value == "-":
                stack.append(val2 - val1)
            elif value == "*":
                stack.append(val2 * val1)
            else:
                stack.append(int(val2 / val1))

    return stack[0]
