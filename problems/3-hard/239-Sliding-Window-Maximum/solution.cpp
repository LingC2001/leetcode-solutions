#include <vector>
#include <deque>
using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<int> max_dq;
    vector<int> max_sliding_window;
    int l = 0;
    int r = 0;
    while (r < nums.size()) {
        // shrink left by if length == k
        if ( (r-l) == k ) {
            if (max_dq.front() == nums[l]) {
                max_dq.pop_front();
            }
            l += 1;
        }

        // increase right by 1
        while (!max_dq.empty() && max_dq.back() < nums[r]) {
            max_dq.pop_back();
        }
        max_dq.push_back(nums[r]);
        r += 1;

        // append to answer list if length == k
        if ( (r-l) == k) {
            max_sliding_window.push_back(max_dq.front());
        }

    }
    
    return max_sliding_window;
}
