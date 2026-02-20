func minimumRecolors(blocks string, k int) int {
    // count first k blocks
    black_count := 0
    max_black_in_interval := 0
    for i := 0; i < k; i++ {
        if blocks[i] == 'B' {
            black_count++
        }
        if black_count > max_black_in_interval {
            max_black_in_interval = black_count
        }
    }

    // slide window size of k and find window with the most amount of blacks
    for i := k; i < len(blocks); i++ {
        if blocks[i] == 'B' {
            black_count++
        }
        if blocks[i-k] == 'B' {
            black_count--
        }
        if black_count > max_black_in_interval {
            max_black_in_interval = black_count
        }
    }

    return k - max_black_in_interval
}