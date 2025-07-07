from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    max_deque = deque()
    res = []

    left = 0
    right = 0

    while right - left < k:
        while max_deque and max_deque[-1] < nums[right]:
            max_deque.pop()
        max_deque.append(nums[right])
        right += 1

    res.append(max_deque[0])

    while right < len(nums):
        if max_deque[0] == nums[left]:
            max_deque.popleft()

        while max_deque and max_deque[-1] < nums[right]:
            max_deque.pop()

        max_deque.append(nums[right])
        res.append(max_deque[0])

        left += 1
        right += 1

    return res
