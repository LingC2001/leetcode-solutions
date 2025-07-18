#include <vector>
#include <algorithm>
using namespace std;

double calculateHours(vector<int>* piles, int k);

int minEatingSpeed(vector<int>& piles, int h) {
    int l = 1;
    int r = *max_element(piles.begin(), piles.end());
    int ans = r;

    while (l <= r) {
        int k = (l+r)/2;
        double hours = calculateHours(&piles, k);

        if (hours <= h) {
            ans = k;
            r = k-1;
        } else {
            l = k+1;
        }
    }

    return ans;
}

double calculateHours(vector<int>* piles, int k) {
    double hours = 0;
    for (double pile : (*piles)) {
        hours += ceil((double)pile/k);
    }
    return hours;
}
