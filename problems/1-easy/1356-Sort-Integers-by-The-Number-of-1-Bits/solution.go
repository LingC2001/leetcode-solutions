func sortByBits(arr []int) []int {

    // sort by comparing number of 1 bits
    slices.SortFunc(arr, func(a, b int) int {
        onesCountA := bits.OnesCount(uint(a))
        onesCountB := bits.OnesCount(uint(b))
        
        if onesCountA > onesCountB {
            return 1
        } else if onesCountA < onesCountB {
            return -1
        }

        if a < b {
            return -1
        } else if b < a{
            return 1
        }
        return 0

	})

    return arr

}