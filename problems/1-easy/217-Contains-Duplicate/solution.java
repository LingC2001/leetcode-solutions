import java.util.HashSet;
import java.util.Set;

public boolean containsDuplicate(int[] nums) {
    Set<Integer> myset = new HashSet<>();
    for (int num : nums) {
        if (myset.contains(num)) {
            return true;
        } else {
            myset.add(num);
        }
    }
    return false;
}