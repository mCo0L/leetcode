# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def findPath(root, target, path):
    if not root:
        return False
    if root.val == target:
        return True
    path.append('L')
    if findPath(root.left, target, path):
        return True
    path.pop()
    
    path.append('R')
    if findPath(root.right, target, path):
        return True
    path.pop()
    
    return False

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        root: TreeNode = [root][0]
        startPath, destPath = [], []
        
        findPath(root, startValue, startPath)
        findPath(root, destValue, destPath)
        
        # Find the common ancestor by comparing paths
        i = 0
        while i < len(startPath) and i < len(destPath) and startPath[i] == destPath[i]:
            i += 1
        
        # Steps to move up from startValue to the common ancestor
        stepsUp = 'U' * (len(startPath) - i)
        # Steps to move down from the common ancestor to destValue
        stepsDown = ''.join(destPath[i:])
        
        return stepsUp + stepsDown

        