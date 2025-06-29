#include <vector>
using namespace std;

int maxArea(vector<int>& height) {
    int l = 0;
    int r = height.size()-1;
    int max_water = 0;
    while (l < r) {
        // calculate water
        int water = min(height[l], height[r])*(r-l);
        if (water > max_water) {
            max_water = water;
        }

        // always move the shorter line to search for more water
        if (height[l] <= height[r]) {
            l++;
        } else {
            r--;
        }
    }
    return max_water;
}
