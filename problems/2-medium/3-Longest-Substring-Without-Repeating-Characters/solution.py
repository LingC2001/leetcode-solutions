def lengthOfLongestSubstring(self, s: str) -> int:
    current_sub = set()

    left = 0
    right = 0
    max_length = 0
    current_length = 0

    while right < len(s):
        if s[right] not in current_sub:
            current_length += 1

            if max_length < current_length:
                max_length = current_length

            current_sub.add(s[right])
            right += 1

        else:
            current_length -= 1
            current_sub.remove(s[left])
            left += 1

    return max_length
