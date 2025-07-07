from typing import List


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    current_min = prices[0]
    for i in range(1, len(prices)):
        temp_profit = prices[i] - current_min
        if temp_profit > max_profit:
            max_profit = temp_profit

        if prices[i] < current_min:
            current_min = prices[i]

    return max_profit
