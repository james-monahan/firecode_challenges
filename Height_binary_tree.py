# Problem statement
# Given the root TreeNode of a binary tree, write a method return its height. 
# An empty tree has a height of 0 while a single node tree has a height of 1.


from TreeNode import TreeNode
class Solution:
    def get_height(self, root: TreeNode) -> int:
        """
        Returns the height of the binary tree.
        :param root: Root node of the binary tree.
        :return: Integer height of the tree.
        """
        def tree_walk(root, counter):
            if root == None:
                return 
            counter+=1
            tree_walk(root.left, counter)
            tree_walk(root.right, counter)
            height.append(counter)
            
        counter = 0
        height = [0]
        
        tree_walk(root, counter)
        
        return max(height)
###################################
#optimal
        if root is None:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))
