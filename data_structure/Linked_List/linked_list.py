# -*- coding: utf-8 -*-
"""鏈結串連"""

class Node(object):
    """
    節點類別
    並存放下個節點的參考
    """
    def __init__(self, element):
        self.element = element
        self.next = None

class LinkedList(object):
    """
    鏈結串連類別
    存放頭節點的參考
    """
    def __init__(self):
        self.length = 0
        self.head = None

    def append(self, element):
        """
        新增節點至尾部
        如該串連實例不存在任何節點
        則將新節點新增為實例的頭和尾
        如該串連實例已存在節點
        則將該新節點新增至實例尾部
        """
        node = Node(element)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node
        self.length += 1

    def insert(self, element, position):
        """
        新增節點至某位置
        位置參數為0，則將新節點插入至頭部
        如不為0，則插入至該index的前一個位置
        """
        if isinstance(position, int) and position <= self.length:
            node = Node(element)
            current = self.head
            index = 0

            if position == 0:
                self.head = node
                node.next = current
            else:
                while index < position:
                    prev = current
                    current = current.next
                    index += 1

                prev.next = node
                node.next = current

            self.length += 1
            return True
        else:
            return False

    def get_head(self):
        """
        獲取頭部節點
        """
        return self.head

    def remove(self, element):
        """
        移除節點
        必須先查找到該筆節點的index
        在對該index進行移除
        """
        index = self.index_of(element)
        return self.remove_at(index)

    def index_of(self, element):
        """
        查找節點的index
        不存在則返回-1
        """
        current = self.head
        index = -1

        while current:
            index += 1
            if current.element == element:
                return index
            current = current.next

        return -1

    def remove_at(self, position):
        """
        移除該index的節點
        如位置為0，則對頭部進行移除
        如位置為最後一位，則對尾部進行移除
        否則對該index進行查詢，並在移除後返回該節點
        """
        if self.length > 0 and position >= 0 and position <= self.length:
            current = self.head
            index = 0

            if position == 0:
                self.head = current.next
            else:
                while index < position:
                    prev = current
                    current = current.next
                    index += 1
                prev.next = current.next

            self.length -= 1
            return current.element
        else:
            return None

    def is_empty(self):
        """
        判斷該實例是否存在節點
        """
        if self.length == 0:
            return True
        return False

    def size(self):
        """
        返回節點長度
        """
        return self.length

    def __str__(self):
        """
        複寫print方法
        """
        current = self.head
        string = ''
        while current:
            string += '{} '.format(current.element)
            current = current.next
        return string

if __name__ == '__main__':
    print('Linked List')
    print('-------------')
    linked_list = LinkedList()
    linked_list.remove_at(0)
    linked_list.append('Ben')
    linked_list.append('Jam')
    linked_list.remove('Hai')
    linked_list.insert('Juice', 2)
    linked_list.insert('Abbey', 3)
    linked_list.remove_at(2)
    linked_list.remove_at(0)
    print('Index of Abbey: {}'.format(linked_list.index_of('Abbey')))
    print('Index of Eva: {}'.format(linked_list.index_of('Eva')))
    print('Size: {}'.format(linked_list.size()))
    print('Mebmers: {}'.format(linked_list))
