"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of 
two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor 
is defined between two nodes v and w as the lowest node in T that has both v and w 
as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another 
example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself 
according to the LCA definition.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.inorder_list = []
        self.postorder_list = []
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        else:
            self.inorder_traversal(root)
            self.postorder_traversal(root)
            #get the positions of node1 and node2 in the inorder traversal of the tree
            index_node1 = self.inorder_list.index(p.val)
            index_node2 = self.inorder_list.index(q.val)
            
            if index_node1 < index_node2:
                between_elems = self.inorder_list[index_node1 : index_node2 + 1]
            else:
                between_elems = self.inorder_list[index_node2 : index_node1 + 1]
        
    
            lca_elem = self.find_elem_max_index(between_elems)
    
            return lca_elem

    def find_elem_max_index(self, between_elems):
        max_index = -1
        elem = None
        for entries in between_elems:
            elem_index = self.postorder_list.index(entries)
            if elem_index > max_index:
                max_index = elem_index
                elem = entries
        return elem
        
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            self.inorder_list.append(node.val)
            self.inorder_traversal(node.right)
            
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            self.postorder_list.append(node.val)
            
    