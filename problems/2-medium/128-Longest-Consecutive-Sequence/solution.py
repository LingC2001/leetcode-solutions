from typing import List


def longestConsecutive(nums: List[int]) -> int:
    longest = 0
    num_set = set(nums)

    # loop over the set to avoid
    for n in num_set:
        # if the number is the start of a sequence:
        if (n - 1) not in num_set:
            length = 1
            # then loop through the whole sequence but adding 1 until it the end.
            while (n + length) in num_set:
                length += 1
            # if the sequence is longer than the max sequence seen already, replace.
            longest = max(longest, length)

    return longest
