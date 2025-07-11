public int[] productExceptSelf(int[] nums) {
    int n = nums.length;
    int[] prefixProduct = new int[n];
    int[] suffixProduct = new int[n];
    int[] res = new int[n];
    
    // Calculate prefix products
    int currentProduct = 1;
    for (int i = 0; i < n; i++) {
        currentProduct *= nums[i];
        prefixProduct[i] = currentProduct;
    }
    
    // Calculate suffix products
    currentProduct = 1;
    for (int i = n - 1; i >= 0; i--) {
        currentProduct *= nums[i];
        suffixProduct[i] = currentProduct;
    }
    
    // Calculate result
    for (int i = 0; i < n; i++) {
        if (i == 0) {
            res[i] = suffixProduct[i + 1];
        } else if (i == n - 1) {
            res[i] = prefixProduct[i - 1];
        } else {
            res[i] = prefixProduct[i - 1] * suffixProduct[i + 1];
        }
    }
    
    return res;
}