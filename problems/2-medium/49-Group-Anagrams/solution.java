import java.util.*;

public List<List<String>> groupAnagrams(String[] strs) {
    List<List<String>> result = new ArrayList<>();
    Map<String, List<String>> groups = new HashMap<>();
    
    for (String s : strs) {
        String signature = getSignature(s);
        groups.computeIfAbsent(signature, k -> new ArrayList<>()).add(s);
    }
    
    for (List<String> group : groups.values()) {
        result.add(group);
    }
    
    return result;
}

private String getSignature(String s) {
    int[] count = new int[26];
    for (char c : s.toCharArray()) {
        count[c - 'a']++;
    }
    
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < 26; i++) {
        if (count[i] != 0) {
            sb.append((char)('a' + i)).append(count[i]);
        }
    }
    return sb.toString();
}