#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> res = {};

    int i = 0;
    while (i < nums.size()-2) {
        long long target = 0 - nums[i];
        int j = i+1;
        int k = nums.size()-1;
        while (j < k) {
            int sum = nums[j] + nums[k];
            if (sum > target) {
                // decrement k skipping dupes
                k--;
            } else if (sum < target) {
                // increment j skipping dupes
                j++;
            } else {
                //store solution
                res.push_back({nums[i], nums[j], nums[k]});
                // increment both to new nums,
                j++;
                while ((j < k) && (nums[j] == nums[j-1])) j++;
                k--;
                while ( (j < k) && (nums[k] == nums[k+1])) k--;
            }
        }
        // increment i skipping dupes
        i++;
        while ((i < nums.size()-2) && (nums[i] == nums[i-1])) i++;
    }
    return res;
}

