class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for(String ch : tokens ){
            switch (ch){
                case "+":
                    stack.push(stack.pop() + stack.pop());
                    break;                    
                case "-":
                    int op2 = stack.pop();
                    int op1 = stack.pop();
                    stack.push(op1 - op2);
                    break;
                case "*":
                    stack.push(stack.pop() * stack.pop());
                    break;
                case "/":
                    int divisor = stack.pop();
                    int divident = stack.pop();
                    stack.push(divident / divisor);
                    break;
                default:
                    stack.push(Integer.parseInt(ch));
            }
        }
        return stack.pop();        
    }
}