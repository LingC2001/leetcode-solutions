def isPalindrome(s: str) -> bool:
    stripped_str = "".join([c for c in s.lower() if c.isalnum()])

    forward_index = 0
    backward_index = len(stripped_str) - 1

    while forward_index < backward_index:
        if stripped_str[forward_index] == stripped_str[backward_index]:
            forward_index += 1
            backward_index -= 1
        else:
            return False

    return True
