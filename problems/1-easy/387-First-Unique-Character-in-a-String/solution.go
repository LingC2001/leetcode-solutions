func firstUniqChar(s string) int {
    char_count := make(map[rune]int)
    for _, c := range s {
        char_count[c] += 1
    }
    for i, c := range s {
        if char_count[c] == 1 {
            return i
        }
    }
    return -1
}