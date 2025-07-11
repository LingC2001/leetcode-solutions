public boolean isPalindrome(String s) {
    StringBuilder filtered = new StringBuilder();
    for (char c : s.toCharArray()) {
        if (Character.isLetterOrDigit(c)) {
            filtered.append(Character.toLowerCase(c));
        }
    }
    
    int start = 0;
    int end = filtered.length() - 1;
    while (start < end) {
        if (filtered.charAt(start) != filtered.charAt(end)) {
            return false;
        }
        start++;
        end--;
    }
    return true;
}