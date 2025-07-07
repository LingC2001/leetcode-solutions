public boolean isValid(String s) {
    Stack<Character> myStack = new Stack<>();

    Map<Character, Character> map = new HashMap<>();
    map.put(')', '(');
    map.put('}', '{');
    map.put(']', '[');

    for (int i = 0; i < s.length(); i++) {
        char character = s.charAt(i);
        if (!map.containsKey(character)) {
            myStack.push(character);
        } else {
            if (!myStack.isEmpty() && myStack.peek() == map.get(character)) {
                myStack.pop();
            } else {
                return false;
            }
        }
    }

    return myStack.isEmpty();
}

