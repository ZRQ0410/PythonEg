"""
    二叉树的遍历

1. 使用链式存储，一个Node表示一个树的节点
2. 节点考虑使用两个属性变量分别表示左连接和右连接
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树遍历类
class Bitree:
    def __init__(self, root=None):
        self.root = root

    # 先序遍历
    def preOrder(self, node):
        if node is None:
            return
        print(node.val, end=' ')
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 中序遍历
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.val, end=' ')
        self.inOrder(node.right)

    # 后序遍历
    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.val, end=' ')


if __name__ == "__main__":
    # 根据后序遍历构建二叉树（左右根）
    # B F G D I H E C A （见笔记中二叉树存储例图）
    b = Node('B')
    f = Node('F')
    g = Node('G')
    d = Node('D', f, g)
    i = Node('I')
    h = Node('H')
    e = Node('E', i, h)
    c = Node('C', d, e)
    a = Node('A', b, c)  # 根节点

    # 将a作为遍历的起始位置
    bt = Bitree(a)
    bt.preOrder(bt.root)
    print()
    bt.inOrder(bt.root)
    print()
    bt.postOrder(bt.root)
