# LeetCode [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

---

## 1. Problem Description

### Description:
Koko loves to eat bananas. There are `n` piles of bananas, where the `i`-th pile has `piles[i]` bananas. Guards leave for `h` hours, and during this time, Koko wants to eat all the bananas. Koko can decide her eating speed `k` (bananas per hour). Each hour, she chooses exactly one pile and eats `k` bananas from it. If the pile has fewer than `k` bananas, she eats all of them and stops eating for that hour. Koko wants to finish all the piles within `h` hours.  

Return the minimum integer `k` such that she can eat all the bananas in at most `h` hours.

---

### Input:
- `piles`: List[int] — an array of positive integers representing the number of bananas in each pile.
- `h`: int — a positive integer representing the total number of hours Koko has.

---

### Output:
- int — the minimum eating speed `k` (bananas per hour) that allows Koko to finish within `h` hours.

---

### Example(s):
**Example 1:**
```
Input: piles = [3, 6, 7, 11], h = 8
Output: 4
```

**Example 2:**
```
Input: piles = [30, 11, 23, 4, 20], h = 5
Output: 30
```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```
Input: piles = [1, 1, 1, 1], h = 4
Output: 1
Explanation: With speed k = 1, Koko spends exactly 4 hours, one banana per hour.
```

**Test Case 2:**
```
Input: piles = [1000000000], h = 2
Output: 500000000
Explanation: She needs to split one huge pile in 2 hours.
```

**Test Case 3:**
```
Input: piles = [5, 5, 5, 5, 5], h = 5
Output: 5
Explanation: She must eat one full pile per hour.
```

**Test Case 4:**
```
Input: piles = [312884470], h = 968709470
Output: 1
Explanation: Plenty of time, so she can eat slowly.
```

</details>

---

## 2. Approach

We use a **Binary Search** on the eating speed `k`:

1. **Search Space**  
   - Minimum possible speed is `1`.  
   - Maximum possible speed is `max(piles)` (eat the largest pile in one hour).

2. **Feasibility Check**  
   - For a candidate speed `mid`, compute the total hours needed:  
     hours = sum( ceil(pile / mid) for each pile ).  
   - If `hours <= h`, Koko can finish in time with speed `mid` (store it as a potential answer and try to lower `mid`).  
   - If `hours > h`, speed `mid` is too slow, so increase `mid`.

3. **Binary Search Loop**  
   - Initialize `left = 1`, `right = max(piles)`, `ans = right`.  
   - While `left <= right`:  
     - `mid = (left + right) // 2`  
     - Compute `hours_taken`.  
     - If `hours_taken > h`, set `left = mid + 1`.  
     - Else, set `ans = mid` (record valid speed) and `right = mid - 1`.  
   - Return `ans`.

This yields the minimum valid eating speed in O(n · log m), where n = number of piles and m = max pile size.

---

## 3. Algorithm Complexity

- Time Complexity: O(n · log m), where  
  - n = number of piles,  
  - m = maximum pile size.  
  We perform a binary search over [1..m] (≈ log m steps), and each step sums over all piles (O(n)).  
- Space Complexity: O(1) extra space (excluding input storage).

---

## 4. Usage

```python
from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            hours_taken = sum(ceil(pile / mid) for pile in piles)

            if hours_taken > h:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1

        return ans

# Example run
sol = Solution()
print(sol.minEatingSpeed([3, 6, 7, 11], 8))  # Output: 4
```

This implementation finds the minimum integer speed `k` that allows Koko to finish eating all piles within `h` hours.