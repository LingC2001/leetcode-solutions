#include <vector>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    // binary search for the correct row
    int l = 0;
    int r = matrix.size()-1;
    while (l <= r) {
        int mid = (l+r)/2;
        if (matrix[mid][0] > target) {
            r = mid - 1;
        } else if (matrix[mid][0] < target) {
            l = mid + 1;
        } else {
            return true;
        }
    }        
    // the right pointer will always end at the correct row
    if (r < 0) {
        return false;
    }
    
    int row = r;
    l = 0;
    r = matrix[row].size()-1;

    while (l <= r) {
        int mid = (l+r)/2;
        if (matrix[row][mid] > target) {
            r = mid - 1;
        } else if (matrix[row][mid] < target) {
            l = mid + 1;
        } else {
            return true;
        }
    }

    return false;

}
