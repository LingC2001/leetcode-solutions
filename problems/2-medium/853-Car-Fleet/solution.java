import java.util.Arrays;
import java.util.Stack;

class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        Integer[] indices = new Integer[n];

        for (int i = 0; i < n; i++) {
            indices[i] = i;
        }

        Arrays.sort(indices, (a, b) -> position[b] - position[a]);

        Stack<Double> stack = new Stack<>();

        for (int i : indices) {
            double fleet_time = (double)(target - position[i]) / speed[i];

            if (stack.isEmpty() || fleet_time > stack.peek()) {
                stack.push(fleet_time);
            }
        }

        return stack.size();
    }
}