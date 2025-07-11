import java.util.HashMap;
import java.util.Map;

public boolean checkInclusion(String s1, String s2) {
    if (s1.length() > s2.length()) {
        return false;
    }
    
    Map<Character, Integer> counts = new HashMap<>();
    Map<Character, Integer> s1Count = new HashMap<>();
    
    // Initialize window to s1.length()
    for (int i = 0; i < s1.length(); i++) {
        s1Count.put(s1.charAt(i), s1Count.getOrDefault(s1.charAt(i), 0) + 1);
        counts.put(s2.charAt(i), counts.getOrDefault(s2.charAt(i), 0) + 1);
    }
    
    if (counts.equals(s1Count)) {
        return true;
    }
    
    int l = 0;
    int r = s1.length();
    while (r < s2.length()) {
        // Calculate new window counts
        char leftChar = s2.charAt(l);
        counts.put(leftChar, counts.get(leftChar) - 1);
        if (counts.get(leftChar) == 0) {
            counts.remove(leftChar);
        }
        
        char rightChar = s2.charAt(r);
        counts.put(rightChar, counts.getOrDefault(rightChar, 0) + 1);
        
        // Check if counts are same
        if (counts.equals(s1Count)) {
            return true;
        }
        
        // Shift window
        l++;
        r++;
    }
    
    return false;
}