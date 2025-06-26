#include <vector>
#include <unordered_set>

using namespace std;


int longestConsecutive(vector<int>& nums) {
    int max_length = 0;
    unordered_set<int> nums_set(nums.begin(), nums.end());
    for (int num: nums_set) {
        if (nums_set.find(num-1) == nums_set.end()) {
            int length = 0;
            while (nums_set.find(num) != nums_set.end()) {
                num++;
                length++;
            }
            max_length = max(max_length, length);
        }
    }
    return max_length;
}
