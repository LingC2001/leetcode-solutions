import java.util.HashSet;
import java.util.Set;

public int longestConsecutive(int[] nums) {
    int maxLength = 0;
    Set<Integer> numsSet = new HashSet<>();
    
    // Add all numbers to set
    for (int num : nums) {
        numsSet.add(num);
    }
    
    for (int num : numsSet) {
        // Only start counting if this is the beginning of a sequence
        if (!numsSet.contains(num - 1)) {
            int length = 0;
            while (numsSet.contains(num)) {
                num++;
                length++;
            }
            maxLength = Math.max(maxLength, length);
        }
    }
    
    return maxLength;
}