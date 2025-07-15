public boolean searchMatrix(int[][] matrix, int target) {
    int left = 0;
    int right = matrix.length - 1;
    int index = 0;
    

    while (left <= right) {
        index = (right + left) / 2;
        if (matrix[index][0] > target) {
            right = index - 1;
        } else if (matrix[index][matrix[index].length - 1] < target) {
            left = index + 1;
        } else {
            break;
        }
    }
    
    left = 0;
    right = matrix[index].length - 1;
    int inner_index = 0;
    while (left <= right) {
        inner_index = (right + left) / 2;
        if (matrix[index][inner_index] > target) {
            right = inner_index - 1;
        } else if (matrix[index][inner_index] < target) {
            left = inner_index + 1;
        } else { 
            return true;
        } 
    }      
    return false;
}

