from typing import List

def search(nums: List[int], target: int) -> int:
    right = len(nums) - 1
    left = 0

    while left <= right:
        index = (right + left) // 2

        if nums[index] > target:
            right = index - 1
        elif nums[index] < target:
            left = index + 1
        else:
            return index
    
    return -1