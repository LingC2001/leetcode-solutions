func arrayStringsAreEqual(word1 []string, word2 []string) bool {
    
    word1_idx := 0
    word2_idx := 0
    str1_idx := 0
    str2_idx := 0

    for word1_idx < len(word1) && word2_idx < len(word2) {
        if word1[word1_idx][str1_idx] != word2[word2_idx][str2_idx] {
            return false
        }
        str1_idx += 1
        str2_idx += 1

        if str1_idx >= len(word1[word1_idx]) {
            word1_idx += 1
            str1_idx = 0
        }
        if str2_idx >= len(word2[word2_idx]) {
            word2_idx += 1
            str2_idx = 0
        }
    }

    // check if reached end of both words
    if word1_idx != len(word1) || str1_idx != 0 || word2_idx != len(word2) || str2_idx != 0 {
        return false
    }

    return true
}