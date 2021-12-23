
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
        node_stack = deque()
        node_stack.append(root)
        node_sum = 0
        
        if not root:
            return 0
        
        while len(node_stack) > 0:
            node = node_stack.popleft()
            node_sum += node.data
            if node.left:
                node_stack.append(node.left)
            if node.right:
                node_stack.append(node.right)
            
        return node_sum
            
