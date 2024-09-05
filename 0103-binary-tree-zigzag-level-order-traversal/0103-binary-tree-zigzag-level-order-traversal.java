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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        Deque<TreeNode> queue = new ArrayDeque<>();
        List<List<Integer>> result = new ArrayList<>();
        
        if(root == null){
            return result;
        }
        queue.add(root);
        Boolean isReverse = true;
        while(queue.size() > 0){
            int levelSize = queue.size();
            List<Integer> level = new ArrayList<>();
            TreeNode node;
            while(levelSize > 0){
                node = queue.removeFirst();
                if(node.left != null){
                    queue.add(node.left);
                }
                if(node.right != null){
                    queue.add(node.right);
                }
                level.add(node.val);
                levelSize--;
            }
            if(isReverse){
                isReverse = false;
            }else{
                isReverse = true;
                Collections.reverse(level);
            }
            result.add(level);
        }
        return result;        
    }
}