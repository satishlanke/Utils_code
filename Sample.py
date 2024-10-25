import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class BinaryTreeWidth {
    public int widthOfBinaryTree(TreeNode root) {
        if (root == null) return 0;

        int maxWidth = 0;
        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(root, 0)); // Initialize queue with root node and position 0

        while (!queue.isEmpty()) {
            int size = queue.size();
            int minPosition = queue.peek().position; // Position of the leftmost node in the level
            int first = 0, last = 0;

            for (int i = 0; i < size; i++) {
                Pair current = queue.poll();
                TreeNode node = current.node;
                int pos = current.position - minPosition; // Normalize position to avoid overflow

                if (i == 0) first = pos; // Position of the first node in the level
                if (i == size - 1) last = pos; // Position of the last node in the level

                if (node.left != null) queue.offer(new Pair(node.left, 2 * pos));
                if (node.right != null) queue.offer(new Pair(node.right, 2 * pos + 1));
            }
            maxWidth = Math.max(maxWidth, last - first + 1);
        }

        return maxWidth;
    }

    private class Pair {
        TreeNode node;
        int position;

        Pair(TreeNode node, int position) {
            this.node = node;
            this.position = position;
        }
    }

    // Helper function to build tree from input list
    public static TreeNode buildTree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("null")) return null;

        TreeNode root = new TreeNode(Integer.parseInt(values.get(0)));
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int i = 1;

        while (i < values.size()) {
            TreeNode current = queue.poll();
            if (current != null) {
                if (i < values.size() && !values.get(i).equals("null")) {
                    current.left = new TreeNode(Integer.parseInt(values.get(i)));
                    queue.offer(current.left);
                }
                i++;

                if (i < values.size() && !values.get(i).equals("null")) {
                    current.right = new TreeNode(Integer.parseInt(values.get(i)));
                    queue.offer(current.right);
                }
                i++;
            }
        }

        return root;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BinaryTreeWidth treeWidth = new BinaryTreeWidth();

        System.out.println("Enter tree nodes in level order (use 'null' for missing nodes), separated by commas:");
        String input = scanner.nextLine();
        List<String> values = Arrays.asList(input.split(","));

        TreeNode root = buildTree(values);

        int maxWidth = treeWidth.widthOfBinaryTree(root);
        System.out.println("Maximum width: " + maxWidth);
    }
}