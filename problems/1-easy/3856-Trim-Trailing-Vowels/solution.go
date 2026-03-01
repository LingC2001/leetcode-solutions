func trimTrailingVowels(s string) string {
    vowels := map[byte]bool{
        'a': true,
        'e': true,
        'i': true,
        'o': true,
        'u': true,
    }

    for i := len(s)-1; i >= 0; i-- {
        if _, ok := vowels[s[i]]; !ok {
            return s[:i+1]
        }
    }

    return ""

}