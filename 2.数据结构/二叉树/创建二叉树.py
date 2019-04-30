#根据前序遍历和后续遍历重建二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        pos = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:1 + pos], tin[:pos])
        root.right = self.reConstructBinaryTree(pre[pos + 1:], tin[pos + 1:])
        return root

tree=Solution()
list=tree.reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
print(list)