/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<Integer> postorder(Node root) {
        Stack<Node> stack = new Stack<>();
        List<Integer> result = new ArrayList<>();
        if(root == null){
            return result;
        }
       stack.push(root);
        while(stack.size() > 0){
            Node current = stack.pop();
            result.add(current.val);
            for(Node child: current.children){
                stack.push(child);
            }
        }
        Collections.reverse(result);
        return result;
    }
}