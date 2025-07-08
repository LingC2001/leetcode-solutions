public int evalRPN(String[] tokens) {
    Stack<Integer> stack = new Stack<>();
    Set<String> operators = Set.of("+", "-", "*", "/");

    for (String token : tokens) {
        if (operators.contains(token)) {
            int right = stack.pop();
            int left = stack.pop();

            switch (token) {
                case "+" -> stack.push(left + right);
                case "-" -> stack.push(left - right);
                case "*" -> stack.push(left * right);
                case "/" -> stack.push(left / right); 
            }
        } else {
            stack.push(Integer.parseInt(token));
        }
    }

    return stack.peek();
}

