import java.util.Stack;

public int[] dailyTemperatures(int[] temperatures) {
    Stack<Integer> idxStack = new Stack<>();
    int[] res = new int[temperatures.length];
    
    for (int currDay = 0; currDay < temperatures.length; currDay++) {
        int currTemp = temperatures[currDay];
        while (!idxStack.isEmpty() && currTemp > temperatures[idxStack.peek()]) {
            int dayIdx = idxStack.pop();
            res[dayIdx] = currDay - dayIdx;
        }
        idxStack.push(currDay);
    }
    
    return res;
}