#include <vector>
using namespace std;

int findMin(vector<int>& nums) {
    int l = 0;
    int r = nums.size()-1;
    
    while (l < r) {
        int mid = (l+r)/2;
        if (nums[mid] < nums[r]) { // if middle < right, right side is sorted, ans on the left side (or first num of right)
            r = mid;
        } else { 
            l = mid+1;
        }
    }
    return nums[r];
}
