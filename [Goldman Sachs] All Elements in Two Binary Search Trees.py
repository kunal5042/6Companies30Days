# Question: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# Medium
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n + m) time and O(n + m) space
    # where n and m are the number of nodes in both trees respectively
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node, traversal):
            if node is None: return []
            inorder(node.left, traversal)
            traversal.append(node.val)
            inorder(node.right, traversal)
            return traversal
        
        tree1 = inorder(root1, [])
        tree2 = inorder(root2, [])
        
        result = []
        
        idx, jdx = 0, 0
        while idx < len(tree1) and jdx < len(tree2):
            if tree1[idx] < tree2[jdx]:
                result.append(tree1[idx])
                idx += 1
            else:
                result.append(tree2[jdx])
                jdx += 1
                
        while idx < len(tree1):
            result.append(tree1[idx])
            idx += 1
            
        while jdx < len(tree2):
            result.append(tree2[jdx])
            jdx += 1
        
        return result


# January 10, 2023

'''

# Kunal Wadhwa

'''