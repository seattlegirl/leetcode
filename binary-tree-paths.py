"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res=[]
        if not root:
            return res
        if not root.left and not root.right:
            res.append(str(root.val))
            return res
        for path in self.binaryTreePaths(root.left):
            res.append(str(root.val)+'->'+path)
        for path in self.binaryTreePaths(root.right):
            res.append(str(root.val)+'->'+path)
        return res

# if __name__ == "__main__":
#     print Solution().binaryTreePaths()
