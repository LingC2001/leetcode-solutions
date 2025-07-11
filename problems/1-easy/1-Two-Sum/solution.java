import java.util.HashMap;
import java.util.Map;

public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> myMap = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int diff = target - nums[i];
        if (myMap.containsKey(diff)) {
            return new int[]{myMap.get(diff), i};
        }
        myMap.put(nums[i], i);
    }
    return new int[]{};
}