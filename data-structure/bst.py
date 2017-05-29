# -*- coding: utf-8 -*-

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        # 根節點
        self.root = None

    # 插入方法
    # 如果根節點已存在，呼叫插入節點方法
    # 不存在則將新節點設為根節點
    def insert(self, key):
        newNode = Node(key)

        if self.root:
            self.insertNode(self.root, newNode)
        else:
            self.root = newNode

    # 插入節點方法
    # 鍵大於當前節點的鍵，將新元素放到左側子節點
    # 鍵小於當前節點的鍵，將新元素放到右側子節點
    def insertNode(self, node, newNode):
        if node.key > newNode.key:
            if node.left:
                self.insertNode(node.left, newNode)
            else:
                node.left = newNode
        else:
            if node.right:
                self.insertNode(node.right, newNode)
            else:
                node.right = newNode

    # 是否存在某個鍵
    def exist(self, key):
        return self.existNode(self.root, key)

    # 是否存在某個鍵方法
    # 存在返回true
    # 不存在返回false
    def existNode(self, node, key):
        if not node:
            return False

        if node.key > key:
            return self.existNode(node.left, key)
        elif node.key < key:
            return self.existNode(node.right, key)
        else:
            return True

    # 中序遍歷
    def inOrderTraverse(self, operator):
        self.inOrderTraverseNode(self.root, operator)

    # 中序遍歷節點方法
    # 由最小節點訪問到最大節點
    # 順序是左 -> 當前節點 -> 右
    def inOrderTraverseNode(self, node, operator):
        if node:
            self.inOrderTraverseNode(node.left, operator)
            operator(node.key)
            self.inOrderTraverseNode(node.right, operator)

    # 先序遍歷
    def preOrderTraverse(self, operator):
        self.preOrderTraverseNode(self.root, operator)

    # 先序遍歷節點方法
    # 先訪問當前節點，再訪問左側節點，最後是右側節點,
    # 順序是當前節點 -> 左 -> 右
    def preOrderTraverseNode(self, node, operator):
        if node:
            operator(node.key)
            self.preOrderTraverseNode(node.left, operator)
            self.preOrderTraverseNode(node.right, operator)

    # 後序遍歷
    def postOrderTraverse(self, operator):
        self.postOrderTraverseNode(self.root, operator)

    # 後序遍歷方法
    # 先訪問左側節點，再訪問右側節點，最後是當前節點
    # 順序是左 -> 右 -> 當前節點
    def postOrderTraverseNode(self, node, operator):
        if node:
            self.postOrderTraverseNode(node.left, operator)
            self.postOrderTraverseNode(node.right, operator)
            operator(node.key)

    # 找到最小值
    def min(self):
        return self.minNodeKey(self.root)

    # 找到最小節點方法
    # 順著最左側尋找，即為最小值
    def minNode(self, node):
        if node and node.left:
            return self.minNode(node.left)
        return node

    # 找到最小值方法
    # 順著最左側尋找，即為最小值
    def minNodeKey(self, node):
        return self.minNode(node).key

    # 找到最大值
    def max(self):
        return self.maxNode(self.root)

    # 找到最大值方法
    # 順著最右側尋找，即為最大值
    def maxNode(self, node):
        if node and node.right:
            return self.maxNode(node.right)
        return node.key

    # 刪除某個鍵
    # 賦值給結點是因為已改變節點參考
    def remove(self, key):
        self.root = self.removeNode(self.root, key)

    # 刪除某個鍵方法，鍵有幾種情況：
    # 為葉節點：將該節點設為None並返回
    # 只有單側有子節點：將該節點替換成子節點
    # 兩側都有節點：將該節點替換成右側中的最小子節點
    def removeNode(self, node, key):
        if not node:
            return None

        if node.key > key:
            node.left = self.removeNode(node.left, key)
            return node
        elif node.key < key:
            node.right = self.removeNode(node.right, key)
            return node
        else:
            if not node.left and not node.right:
                node = None
                return node
            elif not node.left:
                node = node.right
                return node
            elif not node.right:
                node = node.left
                return node
            else:
                # 獲取右側中的最小子節點，並賦值給當前節點
                minNode = self.minNode(node.right)
                node = minNode
                # 刪除原來在右側中的最小子節點
                node.right = self.removeNode(minNode.key)
                return node

tree = BinarySearchTree()
# 插入鍵操作
tree.insert(11)
tree.insert(7)
tree.insert(15)
tree.insert(5)
tree.insert(3)
tree.insert(9)
tree.insert(8)
tree.insert(10)
tree.insert(13)
tree.insert(12)
tree.insert(14)
tree.insert(20)
tree.insert(18)
tree.insert(25)
tree.insert(6)
# 中序遍歷
tree.inOrderTraverse(print)
# 先序遍歷
tree.preOrderTraverse(print)
# 後序遍歷
tree.postOrderTraverse(print)
# 找到最小值
print(tree.min())
# 找到最大值
print(tree.max())
# 是否存在某個鍵
print(tree.exist(18))
