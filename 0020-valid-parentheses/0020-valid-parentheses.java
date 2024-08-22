
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char current : s.toCharArray()) {
            if (current == '(' || current == '{' || current == '[') {
                stack.push(current);
            } else {
                if (stack.isEmpty()) return false;
                char lastOpened = stack.pop();
                if ((current == ')' && lastOpened != '(') ||
                    (current == '}' && lastOpened != '{') ||
                    (current == ']' && lastOpened != '[')) {
                    return false;
                }
            }
        }
        
        return stack.isEmpty();
    }
}