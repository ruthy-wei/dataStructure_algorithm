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
        if root==None:
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
    #删除节点
    def delete(self,root,val):
        if root==None:
            return None
        if root.val>val:
            root.left=self.delete(root.left,val)
        if root.val<val:
            root.right=self.delete(root.right,val)
        elif root.val==val:
            if root.left and root.right:
                temp= self.findMin(root.right)
                root.val=temp.val
                root.right = self.delete(root.right,temp.val)
            elif root.left==None and root.right==None:
                root= None
            elif root.left:
                root= root.left
            elif root.right:
                root= root.right
        return root
    #查找树中第K小的数
    def kthSmallest(self, root,k):
        for i in range(1,k):
            root=self.deleteMin(root)
        return self.findMin(root)
    #查找数中最小值
    def findMin(self,root):
        if root.left:
            return self.findMin(root.left)
        else:
            return root.val
    #删除数的最小值
    def deleteMin(self,root):
        if root.left==None:
            if root.right:
                return root.right
            else:
                return None
        root.left=self.deleteMin(root.left)
        return root
    #中序打印二叉树
    def printTree(self, root):
        # 打印二叉搜索树(中序打印，有序数列)
        if root == None:
            return
        self.printTree(root.left)
        print(root.val, end=' ')
        self.printTree(root.right)


if __name__=="__main__":
    List= [5,3,6,2,4,1]

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
    print('查询树中值为2的节点:', op.query(root, 2))
    print('删除树中值为2的节点,打印删除后的树中序遍历:', )
    root=op.delete(root, 2)
    op.printTree(root)
    # print('查询树中第3小值:', op.kthSmallest(root,3))
