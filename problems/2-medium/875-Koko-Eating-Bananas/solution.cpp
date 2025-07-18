#include <vector>
#include <algorithm>
using namespace std;

bool eatable(vector<int>* piles, int k, int h);

int minEatingSpeed(vector<int>& piles, int h) {
    int l = 1;
    int r = *max_element(piles.begin(), piles.end());
    int ans = r;

    while (l <= r) {
        int k = (l+r)/2;
        if (eatable(&piles, k, h)) {
            ans = k;
            r = k-1;
        } else {
            l = k+1;
        }
    }
    return ans;
}

bool eatable(vector<int>* piles, int k, int h) {
    double hours = 0;
    for (double pile : (*piles)) {
        hours += ceil((double)pile/k);
    }
    return (hours <= h);
}
