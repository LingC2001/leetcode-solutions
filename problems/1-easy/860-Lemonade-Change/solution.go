func lemonadeChange(bills []int) bool {
    change := []int{0, 0}
    for _, note := range bills {
        if note == 20 {
            if change[1] > 0 {
                change[0] -= 1 // give $5
                change[1] -= 1 // give $10
            } else {
                change[0] -= 3 // give 3x$5
            }
        } else if note == 10 {
            change[0] -= 1 // give $5
            change[1] += 1 // gain $10
        } else {
            change[0] += 1 // gain $5
        }
        if change[0] < 0 || change[1] < 0 {
            return false
        }
    }
    return true
}