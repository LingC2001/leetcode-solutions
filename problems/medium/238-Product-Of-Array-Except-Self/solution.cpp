#include <vector>

using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
    
    vector<int> prefix_product(nums.size());
    int current_product = 1;
    for (int i = 0; i < nums.size(); i++) {
        current_product *= nums[i];
        prefix_product[i] = current_product;
    }

    current_product = 1;
    vector<int> suffix_product(nums.size());
    for (int i = nums.size() - 1; i >= 0; i--) {
        current_product *= nums[i];
        suffix_product[i] = current_product;
    }

    vector<int> res(nums.size());
    for (int i = nums.size() - 1; i >= 0; i--) {
        if (i == 0) {
            res[i] = suffix_product[i+1];
        } else if (i == nums.size()-1) {
            res[i] = prefix_product[i-1];
        } else {
            res[i] = prefix_product[i-1]*suffix_product[i+1];
        }
    }

    return res;
}
