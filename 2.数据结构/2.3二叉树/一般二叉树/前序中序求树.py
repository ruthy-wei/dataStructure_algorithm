class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    #前序中序====》树
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            flag = TreeNode(pre[0])
            flag.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0]) + 1], tin[:tin.index(pre[0])])
            flag.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])
        return flag

    # 后序中序====》树
    def reConstructBinaryTree2(self,tin,beh):
        if len(beh)== 0:
            return None
        elif len(beh)== 1:
            return beh[-1]
        else:
            flag=TreeNode(beh[-1])
            flag.left=self.reConstructBinaryTree2(tin[:tin.index(beh[-1])],beh[tin.index(beh[-1])+1:])
            flag.right=self.reConstructBinaryTree2(tin[tin.index(beh[-1])+1:],beh[tin.index(beh[-1]):-1])