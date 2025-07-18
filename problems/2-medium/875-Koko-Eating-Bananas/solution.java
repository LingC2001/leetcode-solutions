public int minEatingSpeed(int[] piles, int h) {
    int low = 1;
    int high = getMax(piles);
    
    while(high > low) {
        int mid = low + (high - low)/2;
        int hours = countHours(piles, mid);
        if(hours > h) {
            low  = mid +1;
        } else {
            high = mid;
        }
    }

    return low;
}

public int countHours(int[] piles, int k) {
    int count = 0;
    for(int pile : piles) {
        count += (pile+k-1)/k;
    }
    return count;
}

private static int getMax(int[] piles) {
    int max = 0;
    for (int pile : piles) {
        if (pile > max) {
            max = pile;
        }
    }
    return max;
}
