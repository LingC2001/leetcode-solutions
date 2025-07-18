from math import ceil
from typing import List


def minEatingSpeed(self, piles: List[int], h: int) -> int:
    left = 1
    right = max(piles)
    ans = right

    while left <= right:
        mid = (left + right) // 2

        hours_taken = sum(ceil(pile / mid) for pile in piles)

        if hours_taken > h:
            left = mid + 1
        else:
            right = mid - 1
            ans = mid
    return ans
