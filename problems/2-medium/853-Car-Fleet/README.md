# LeetCode [853. Car Fleet](https://leetcode.com/problems/car-fleet/description/)

---

## 1. Problem Description

### Description:
There are `n` cars going to the same destination along a one-lane road. The destination is `target` miles away.

You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the position of the ith car and `speed[i]` is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

---

### Input:
- `target`: An integer representing the destination distance in miles.
- `position`: A list of integers representing the initial position of each car.
- `speed`: A list of integers representing the speed of each car in miles per hour.

---

### Output:
- An integer representing the number of car fleets that will arrive at the destination.

---

### Example(s):
**Example 1:**
```

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3

```

**Example 2:**
```

Input: target = 10, position = [3], speed = [3]
Output: 1

```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```

Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation: All cars eventually form one fleet. Cars at positions 0 and 2 meet at position 4, then this fleet meets the car at position 4 at position 6.

```

**Test Case 2:**
```

Input: target = 10, position = [6,8], speed = [3,2]
Output: 2
Explanation: The car at position 8 is slower and will never be caught by the car at position 6, so they remain separate fleets.

```

</details>

---

## 2. Approach

The key insight is that once a faster car catches up to a slower car ahead, they form a fleet and must travel at the slower car's speed. This means we need to determine which cars will catch up to others before reaching the destination.

**Algorithm:**
1. **Calculate arrival times**: For each car, compute the time it would take to reach the target if traveling alone: `time = (target - position) / speed`.

2. **Sort by position**: Sort cars by their starting positions in descending order (closest to target first). This is crucial because cars closer to the target act as "barriers" for cars behind them.

3. **Greedy fleet counting**: Iterate through the sorted cars:
   - If a car's arrival time is greater than the previous maximum time seen, it forms a new fleet (it won't catch up to any car ahead).
   - Otherwise, it will catch up to a slower fleet ahead and join it.

4. **Track maximum time**: Keep track of the maximum arrival time seen so far, which represents the time of the slowest fleet that cars behind must catch up to.

The approach is greedy because we process cars from front to back, and each car either joins an existing fleet or starts a new one based on whether it can catch up to the slowest fleet ahead.

---

## 3. Algorithm Complexity

- **Time Complexity:** O(n log n), where n is the number of cars. The sorting step dominates the time complexity.
- **Space Complexity:** O(n), for storing the paired position-speed data and the time calculations.

---