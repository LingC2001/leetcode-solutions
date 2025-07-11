public int maxArea(int[] height) {
    int l = 0;
    int r = height.length - 1;
    int maxWater = 0;
    
    while (l < r) {
        // Calculate water
        int water = Math.min(height[l], height[r]) * (r - l);
        if (water > maxWater) {
            maxWater = water;
        }
        
        // Always move the shorter line to search for more water
        if (height[l] <= height[r]) {
            l++;
        } else {
            r--;
        }
    }
    
    return maxWater;
}