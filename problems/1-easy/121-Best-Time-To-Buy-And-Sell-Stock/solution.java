public int maxProfit(int[] prices) {
    int minPrice = prices[0];
    int maxProfit = 0;
    for (int currPrice : prices) {
        int profit = currPrice - minPrice;
        if (profit > maxProfit) {
            maxProfit = profit;
        }
        if (currPrice < minPrice) {
            minPrice = currPrice;
        }
    }
    return maxProfit;
}