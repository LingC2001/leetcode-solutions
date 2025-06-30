#include <vector>
using namespace std;

int maxProfit(vector<int>& prices) {
    int min_price = prices[0];
    int max_profit = 0;
    for (int curr_price : prices) {
        int profit = curr_price - min_price;
        if (profit > max_profit) {
            max_profit = profit;
        }
        if (curr_price < min_price) {
            min_price = curr_price;
        }
    }
    return max_profit;
}