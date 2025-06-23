#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> my_map;
    for (int i = 0; i < nums.size(); i++) {
        int diff = target - nums[i];
        if (my_map.find(diff) != my_map.end()) {
            return {my_map[diff], i};
        } 
        my_map[nums[i]] = i;
    }
    return {};
}