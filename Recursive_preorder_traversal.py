# Problem statement:
# Given the root TreeNode of a binary tree, write a method to 
# populate an integer list with the data of the nodes of the tree, 
# as visited with pre-order traversal.

from typing import List

from TreeNode import TreeNode


class Solution:
    def pre_order(self, root: TreeNode) -> List[int]:
        """
        Returns an integer array with data of nodes
        visited with pre-order traversal.
        :param root: Root TreeNode of the binary tree.
        :return: Integer array containing data of visited nodes.
        """
        
        def tree_walk(root, traversal):
            if root == None:
                return
            traversal.append(root.data)
            tree_walk(root.left, traversal)
            tree_walk(root.right, traversal)
            
        
        traversal = []

        tree_walk(root, traversal)
        
        return traversal
