public int minEatingSpeed(int[] piles, int h) {
    
    int left = 1;
    int right = getMax(piles);

    int min_eat = right;

    while (left <= right) {
        int num_eat = (right + left) / 2;
        long current_time = koko_kram_k(piles, num_eat);
        if (current_time <= h && num_eat < min_eat) {
            min_eat = num_eat;
            right = num_eat - 1;
        } else {
            left = num_eat + 1;
        }
            
    }

    return min_eat;
}

private long koko_kram_k(int[] piles, int k) {
    long time = 0;

    for (int i = 0; i < piles.length; i++) {
        time += Math.ceilDiv(piles[i], k);
    }

    return time;
}

private int getMax(int[] piles) {
    int max = piles[0];
    for (int pile : piles) {
        if (pile > max) {
            max = pile;
        }
    }
    return max;
}
