# Problem statement
# Given the root TreeNode of a binary search tree, 
# return the minimum data value present in the tree.

from TreeNode import TreeNode


class Solution:
    def min_data(self, root: TreeNode) -> int:
        """
        Returns the minimum data value present in the passed
        binary search tree.
        :param root: Root TreeNode of the binary search tree.
        :return: Minimum integer data value in the tree.
        """
        if root.left == None:
            return root.data

        return self.min_data(root.left)
