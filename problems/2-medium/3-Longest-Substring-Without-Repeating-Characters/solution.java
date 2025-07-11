import java.util.HashSet;
import java.util.Set;

public int lengthOfLongestSubstring(String s) {
    Set<Character> substrChars = new HashSet<>();
    int maxLen = 0;
    int l = 0;
    int r = 0;
    
    while (r < s.length()) {
        while (substrChars.contains(s.charAt(r))) {
            substrChars.remove(s.charAt(l));
            l++;
        }
        substrChars.add(s.charAt(r));
        r++;
        maxLen = Math.max(maxLen, r - l);
    }
    
    return maxLen;
}