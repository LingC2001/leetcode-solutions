from collections import defaultdict


def characterReplacement(s: str, k: int) -> int:
    sub_letters = defaultdict(int)
    left = 0
    right = 0
    res = 0
    max_letter_count = 0

    while right < len(s):
        sub_letters[s[right]] += 1
        max_letter_count = max(max_letter_count, sub_letters[s[right]])
        right += 1

        while (right - left) - max_letter_count > k:
            sub_letters[s[left]] -= 1
            left += 1

        if right - left > res:
            res = right - left

    return res
