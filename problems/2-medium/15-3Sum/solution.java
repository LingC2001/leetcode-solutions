import java.util.*;

public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> res = new ArrayList<>();
    
    int i = 0;
    while (i < nums.length - 2) {
        long target = 0 - nums[i];
        int j = i + 1;
        int k = nums.length - 1;
        
        while (j < k) {
            int sum = nums[j] + nums[k];
            if (sum > target) {
                // Decrement k skipping dupes
                k--;
            } else if (sum < target) {
                // Increment j skipping dupes  
                j++;
            } else {
                // Store solution
                res.add(Arrays.asList(nums[i], nums[j], nums[k]));
                // Increment both to new nums
                j++;
                while (j < k && nums[j] == nums[j - 1]) j++;
                k--;
                while (j < k && nums[k] == nums[k + 1]) k--;
            }
        }
        
        // Increment i skipping dupes
        i++;
        while (i < nums.length - 2 && nums[i] == nums[i - 1]) i++;
    }
    
    return res;
}