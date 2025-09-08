func twoSum(nums []int, target int) []int {
    numMap := make(map[int]int) //using map as a set for now
    diff := 0
    for i, v := range nums {
        diff = target - v
        if val, ok := numMap[diff]; ok {
            return []int{i, val}
        }
        numMap[v] = i
    }
    return []int{}
}