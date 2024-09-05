/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        Deque<TreeNode> queue = new ArrayDeque<>();
        List<Double> result = new ArrayList<>();
        
        if(root == null){
            return result;
        }
        queue.add(root);
        while(queue.size() > 0){
            int levelSize = queue.size();
            int size = queue.size();
            TreeNode node;
            double sum = 0;
            while(levelSize > 0){
                node = queue.removeFirst();
                if(node.left != null){
                    queue.add(node.left);
                }
                if(node.right != null){
                    queue.add(node.right);
                }
                sum += node.val;
                levelSize--;
            }
            result.add(sum / size);
        }
        return result;
        
    }
}