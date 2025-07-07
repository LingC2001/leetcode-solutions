def isValid(s: str) -> bool:
    my_dict = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in s:
        if char not in my_dict:
            stack.append(char)
        elif stack and my_dict[char] == stack[-1]:
            stack.pop()
        else:
            return False

    return len(stack) == 0
