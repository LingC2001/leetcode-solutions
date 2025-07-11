public int characterReplacement(String s, int k) {
    int[] charCounts = new int[26];
    int l = 0;
    int r = 0;
    int maxLength = 0;
    int maxFreq = 0;
    
    while (r < s.length()) {
        // Increment s[r] count
        int currCharIdx = getCharIndex(s.charAt(r));
        charCounts[currCharIdx]++;
        // Finding char with max freq
        maxFreq = Math.max(maxFreq, charCounts[currCharIdx]);
        
        // Satisfy condition + calculate length
        int length = r - l + 1;
        while ((length - maxFreq) > k) {
            charCounts[getCharIndex(s.charAt(l))]--;
            l++;
            length--;
        }
        maxLength = Math.max(maxLength, length);
        r++;
    }
    
    return maxLength;
}

private int getCharIndex(char c) {
    return c - 'A';
}