# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return []
            
            # If it's a leaf node
            if not node.left and not node.right:
                return [1]
            
            # Get the distances from left and right subtrees
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Count good pairs
            nonlocal count
            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= distance:
                        count += 1
            
            # Collect all distances and increment by 1 for the current node
            all_distances = [d + 1 for d in left_distances + right_distances]
            
            return all_distances
    
        count = 0
        dfs(root)
        return count
            