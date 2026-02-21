Use a pointer to keep track of which group you are up to. Then notice that the next set of groups must always be opposite number as the current last group.

At the end, since every iteration we may add 1 or 2 numbers, we check whether or not the length went past n, and whether we should subtract 1 from the counter.

Trick: since we always want a 1 after 2s and a 2 after 1s, we can get the opposite number by doing 3-1 -> 2, and 3-2 -> 1.