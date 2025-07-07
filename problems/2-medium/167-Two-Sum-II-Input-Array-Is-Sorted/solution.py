from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    lower_index = 0
    higher_index = len(numbers) - 1

    while lower_index < higher_index:
        current_sum = numbers[lower_index] + numbers[higher_index]

        if current_sum > target:
            higher_index -= 1

        elif current_sum < target:
            lower_index += 1

        else:
            return [lower_index + 1, higher_index + 1]
