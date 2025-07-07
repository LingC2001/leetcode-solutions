from typing import List


def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    sols = []

    for i in range(len(nums)):
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        lo = i + 1
        hi = len(nums) - 1

        target = 0 - nums[i]

        while lo < hi:
            curr_sum = nums[lo] + nums[hi]
            if target == curr_sum:
                sols.append([nums[lo], nums[hi], nums[i]])
                hi -= 1
                while lo < hi and nums[hi + 1] == nums[hi]:
                    hi -= 1
                lo += 1
                while lo < hi and nums[lo - 1] == nums[lo]:
                    lo += 1

            elif target < curr_sum:
                hi -= 1
                # while lo < hi and nums[hi+1] == nums[hi]:
                #     hi -= 1
            else:
                lo += 1
                # while lo < hi and nums[lo-1] == nums[lo]:
                #     lo += 1

    return sols
