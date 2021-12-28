
# Problem statement
# Given the root TreeNode of a binary tree, write a method to 
# return the sum of the data values of all nodes in the tree.

from collections import deque

from TreeNode import TreeNode


class Solution:
    def sum_nodes(self, root: TreeNode) -> int:
        """
        Returns the sum of all nodes' data in the tree.
        :param root: Root TreeNode of the tree.
        :return: Sum of all nodes' data.
        """
        que = deque()
        que.append(root)
        tree_sum = 0
        
        while len(que) > 0 and root is not None:
            node = que.popleft()
            if node.left:
                que.append(node.left) 
            if node.right:    
                que.append(node.right)
            tree_sum += node.data
            
        return tree_sum
