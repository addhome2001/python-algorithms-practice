# -*- coding: utf-8 -*-
"""二分搜尋樹"""

class Node(object):
    """
    節點類別
    存放左和右節點的參考
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree(object):
    """
    二分搜尋樹類別
    存放根節點的參考
    """
    def __init__(self):
        self.root = None

    def insert_node(self, node, new_node):
        """
        插入節點方法
        鍵大於當前節點的鍵，將新元素放到左側子節點
        鍵小於當前節點的鍵，將新元素放到右側子節點
        """
        if node.key > new_node.key:
            if node.left:
                self.insert_node(node.left, new_node)
            else:
                node.left = new_node
        else:
            if node.right:
                self.insert_node(node.right, new_node)
            else:
                node.right = new_node

    def insert(self, key):
        """
        插入方法
        如果根節點已存在，呼叫插入節點方法
        不存在則將新節點設為根節點
        """
        new_node = Node(key)

        if self.root:
            self.insert_node(self.root, new_node)
        else:
            self.root = new_node

    def exist_node(self, node, key):
        """
        是否存在某個鍵方法
        存在返回true
        不存在返回false
        """

        if not node:
            return False

        if node.key > key:
            return self.exist_node(node.left, key)
        elif node.key < key:
            return self.exist_node(node.right, key)
        return True

    def exist(self, key):
        """
        是否存在某個鍵
        """
        return self.exist_node(self.root, key)

    def in_order_traverse_node(self, node, operator):
        """
        中序遍歷節點方法
        由最小節點訪問到最大節點
        順序是左 -> 當前節點 -> 右
        """
        if node:
            self.in_order_traverse_node(node.left, operator)
            operator(node.key)
            self.in_order_traverse_node(node.right, operator)

    def in_order_traverse(self, operator):
        """
        中序遍歷
        """
        self.in_order_traverse_node(self.root, operator)

    def pre_order_traverse_node(self, node, operator):
        """
        先序遍歷節點方法
        先訪問當前節點，再訪問左側節點，最後是右側節點,
        順序是當前節點 -> 左 -> 右
        """
        if node:
            operator(node.key)
            self.pre_order_traverse_node(node.left, operator)
            self.pre_order_traverse_node(node.right, operator)

    def pre_order_traverse(self, operator):
        """
        先序遍歷
        """
        self.pre_order_traverse_node(self.root, operator)

    def post_order_traverse_node(self, node, operator):
        """
        後序遍歷方法
        先訪問左側節點，再訪問右側節點，最後是當前節點
        順序是左 -> 右 -> 當前節點
        """
        if node:
            self.post_order_traverse_node(node.left, operator)
            self.post_order_traverse_node(node.right, operator)
            operator(node.key)

    def post_order_traverse(self, operator):
        """
        後序遍歷
        """
        self.post_order_traverse_node(self.root, operator)

    def min_node(self, node):
        """
        找到最小節點方法
        順著最左側尋找，即為最小值
        """
        if node and node.left:
            return self.min_node(node.left)
        return node

    def min_node_key(self, node):
        """
        找到最小值方法
        順著最左側尋找，即為最小值
        """
        return self.min_node(node).key

    def find_min(self):
        """
        找到最小值
        """
        return self.min_node_key(self.root)

    def max_node(self, node):
        """
        找到最大值方法
        順著最右側尋找，即為最大值
        """
        if node and node.right:
            return self.max_node(node.right)
        return node.key

    def find_max(self):
        """
        找到最大值
        """
        return self.max_node(self.root)

    def remove_node(self, node, key):
        """
        刪除某個鍵，有以下情況：
        為葉節點：將該節點設為None並返回
        只有單側有子節點：將該節點替換成子節點
        兩側都有節點：將該節點替換成右側中的最小子節點
        """
        if not node:
            return None

        if node.key > key:
            node.left = self.remove_node(node.left, key)
        elif node.key < key:
            node.right = self.remove_node(node.right, key)
        else:
            if not node.left and not node.right:
                node = None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                # 獲取右側中的最小子節點，並賦值給當前節點
                min_node = self.min_node(node.right)
                node = min_node
                # 刪除原來在右側中的最小子節點
                node.right = self.remove_node(node.right, min_node.key)
        return node

    def remove(self, key):
        """
        刪除某個鍵
        賦值給結點是因為已改變節點參考
        """
        self.root = self.remove_node(self.root, key)

if __name__ == '__main__':
    def print_result(result):
        """print function"""
        print(result)
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
    print("中序遍歷")
    tree.in_order_traverse(print_result)
    print("先序遍歷")
    tree.pre_order_traverse(print_result)
    print("後序遍歷")
    tree.post_order_traverse(print_result)
    print("找到最小值")
    print(tree.find_min())
    print("找到最大值")
    print(tree.find_max())
    print("是否存在某個鍵")
    print(tree.exist(18))
