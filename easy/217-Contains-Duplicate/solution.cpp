bool containsDuplicate(vector<int>& nums) {
    unordered_set<int> myset;
    for (int num : nums) {
        if (myset.contains(num)) {
            return true;
        } else {
            myset.insert(num);
        }
    }
    return false;
}