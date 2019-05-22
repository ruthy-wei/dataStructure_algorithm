class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class BSTree:
    #创建二叉排序树
    def builtTree(self,nlist):
        root=None
        for val in nlist:
            root=self.insert(root,val)
        return root
    #插入节点
    def insert(self,root,val):
        if root == None:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root
    #查找节点
    def query(self,root,val):
        if root.val==None:
            return False
        elif val<root.val:
            return self.query(root.left,val)
        elif val>root.val:
            return self.query(root.right,val)
        elif val==root.val:
            return True
    #查找树的最大值
    def findMax(self,root):
        if root.right:
            return self.findMax(root.right)
        else:
            return root.val
    def findMin(self,root):
        if root.left:
            return self.findMin(root.left)
        else:
            return root.val
    #中序打印二叉树
    def printTree(self, root):
        # 打印二叉搜索树(中序打印，有序数列)
        if root == None:
            return
        self.printTree(root.left)
        print(root.val, end=' ')
        self.printTree(root.right)


if __name__=="__main__":
    List= [17,5,35,2,11,29,38,9,16,8]

    # root=op.builtTree(List)
    root = None
    op = BSTree()
    for val in List:
        root = op.insert(root, val)
    print('中序打印二叉搜索树：', end=' ')
    op.printTree(root)
    print('')
    print('查询树中最大值:', op.findMax(root))
    print('查询树中最小值:', op.findMin(root))
    print('查询树中值为5的节点:', op.query(root, 5))