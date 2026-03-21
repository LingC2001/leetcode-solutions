func numJewelsInStones(jewels string, stones string) int {
    jewels_set := make(map[rune]struct{})
    for _, j := range(jewels) {
        jewels_set[j] = struct{}{}
    }

    num_stone_jewels := 0
    for _, s := range(stones) {
        if _, ok := jewels_set[s]; ok {
            num_stone_jewels++
        }
    }

    return num_stone_jewels
}
