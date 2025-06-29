from typing import List


def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1

    max_height = 0
    while left < right:
        current_height = min(height[left], height[right]) * (right - left)
        if max_height < current_height:
            max_height = current_height

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_height
