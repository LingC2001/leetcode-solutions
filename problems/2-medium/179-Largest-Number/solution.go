func largestNumber(nums []int) string {

    // convert to string slice and find maximum length
    numsStr := make([]string, 0)
    for _, val := range nums {
        numsStr = append(numsStr, strconv.Itoa(val))
    }
    
    slices.SortFunc(numsStr, func(a, b string) int {
		return cmp.Compare(b+a, a+b)
	})

    if numsStr[0] == "0" {
        return "0"
    }

    // join all nums in numsStr
    biggestNum := strings.Join(numsStr, "")
    return biggestNum
}