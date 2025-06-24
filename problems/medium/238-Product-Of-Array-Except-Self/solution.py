from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    forward_mult = []
    backward_mult = [0] * len(nums)
    res = []

    accumulated_sum = 1
    for i in range(len(nums)):
        accumulated_sum *= nums[i]
        forward_mult.append(accumulated_sum)

    accumulated_sum = 1
    for i in range(len(nums) - 1, -1, -1):
        accumulated_sum *= nums[i]
        backward_mult[i] = accumulated_sum

    for i in range(len(nums)):
        if i == 0:
            res.append(backward_mult[i + 1])
        elif i == len(nums) - 1:
            res.append(forward_mult[i - 1])
        else:
            res.append(forward_mult[i - 1] * backward_mult[i + 1])

    return res
