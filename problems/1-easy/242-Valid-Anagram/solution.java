import java.util.HashMap;
import java.util.Map;

public boolean isAnagram(String s, String t) {
    Map<Character, Integer> counter = new HashMap<>();
    
    // Count characters in string s
    for (char c : s.toCharArray()) {
        counter.put(c, counter.getOrDefault(c, 0) + 1);
    }
    
    // Decrement counts based on string t
    for (char c : t.toCharArray()) {
        if (counter.containsKey(c)) {
            counter.put(c, counter.get(c) - 1);
            if (counter.get(c) <= 0) {
                counter.remove(c);
            }
        } else {
            return false;
        }
    }
    
    return counter.isEmpty();
}