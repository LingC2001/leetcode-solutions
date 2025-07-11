import java.util.*;

public int[] maxSlidingWindow(int[] nums, int k) {
    Deque<Integer> maxDq = new ArrayDeque<>();
    List<Integer> maxSlidingWindow = new ArrayList<>();
    int l = 0;
    int r = 0;
    
    while (r < nums.length) {
        // Shrink left if length == k
        if ((r - l) == k) {
            if (!maxDq.isEmpty() && maxDq.peekFirst() == nums[l]) {
                maxDq.pollFirst();
            }
            l++;
        }
        
        // Increase right by 1
        while (!maxDq.isEmpty() && maxDq.peekLast() < nums[r]) {
            maxDq.pollLast();
        }
        maxDq.offerLast(nums[r]);
        r++;
        
        // Append to answer list if length == k
        if ((r - l) == k) {
            maxSlidingWindow.add(maxDq.peekFirst());
        }
    }
    
    return maxSlidingWindow.stream().mapToInt(i -> i).toArray();
}