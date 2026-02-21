func magicalString(n int) int {
    if n <= 3 {
        return 1
    }
    s := []int{1, 2, 2}
    ptr := 2
    one_counter := 1
    var prev int

    for len(s) < n {
        prev = s[len(s)-1]
        for i := 0; i < s[ptr]; i++ {
            if prev == 1 {
                s = append(s, 2)
            } else {
                s = append(s, 1)
                one_counter += 1
            }
        }
        ptr += 1
    }

    if len(s) > n {
        if s[len(s)-1] == 1 {
            one_counter -= 1
        }
    }

    return one_counter

}