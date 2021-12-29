# Problem statement
# Given the root TreeNode of a binary tree, write a method to iteratively traverse 
# the tree and return its nodes' integer data as a list. The output list should 
# have the data ordered as visited with pre-order traversal, wherein the node is 
# itself processed first, followed its left and right subtrees.

from typing import List
from TreeNode import TreeNode
from collections import deque


class Solution:
    def pre_order(self, root: TreeNode) -> List[int]:
        """
        Returns a list of integers depicting the data
        of the nodes of the input tree, traversed with
        pre-order iterative traversal.
        :param root: Root node of the binary tree.
        :return: List of node data.
        """
        if root == None:
            return []
            
        stack = deque()
        stack.append(root)
        traversal = []
        
        while len(stack) > 0 and root is not None:
            node = stack.pop()
            traversal.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

                
        return traversal
