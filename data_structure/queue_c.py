# -*- coding: utf-8 -*-
"""列隊"""

class Queue(object):
    """
    列隊類別
    為先進先出的資料結構
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        新增資料
        從尾部入列資料
        """
        self.items.append(item)

    def dequeue(self):
        """
        移除資料
        從頭部出列資料
        """
        if not self.is_empty():
            return self.items.pop(0)
        return False

    def front(self):
        """
        返回最先入隊的資料
        """
        if self.is_empty():
            return self.items[0]
        return False

    def clear(self):
        """
        清空該列隊實例
        """
        self.items = []

    def size(self):
        """
        返回列隊大小
        """
        return len(self.items)

    def is_empty(self):
        """
        判斷列隊長度是否等於小於0
        """
        return self.size() <= 0

    def preview(self):
        """
        列舉出列隊資料
        """
        for item in self.items:
            print(item)

# practice
class PriorityItem(object):
    """
    優先列隊項目類別
    額外存放了優先等級
    """
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def get_item(self):
        """
        返回該項目
        """
        return self.item

    def get_priority(self):
        """
        返回該項目的優先等級
        """
        return self.priority

class PriorityQueue(Queue):
    """
    優先列隊類別
    繼承自普通列隊類別
    """
    def __init__(self):
        Queue.__init__(self)

    def enqueue(self, item, priority=0):
        """
        推入資料至列隊
        優先等級的排序為，數字越大越前面
        """
        if self.is_empty():
            return self.items.append(PriorityItem(item, priority))

        for i in range(0, self.size()):
            if priority > self.items[i].get_priority():
                self.items[i:i] = [PriorityItem(item, priority)]
                break
        else:
            self.items.append(PriorityItem(item, priority))

    def preview(self):
        """
        覆蓋print方法
        """
        for item in self.items:
            print('Item: {}, Priority: {}'.format(
                item.get_item(), item.get_priority()
            ))

def hot_potato(members, number):
    """
    傳遞練習
    每次遍歷項目時，數字都減一
    當數字為0時，將該位置的項目出列
    直到剩下一個玩家為止
    """
    queue = Queue()

    for member in members:
        queue.enqueue(member)

    while queue.size() is not 1:
        counter = number
        while counter > 0:
            counter -= 1
            queue.enqueue(queue.dequeue())

        print("{} get out.".format(queue.dequeue()))

    print("{} is winner!".format(queue.dequeue()))

if __name__ == '__main__':
    print('Normal Queue')
    print('-------------')
    normal_queue = Queue()
    normal_queue.enqueue("Han")
    normal_queue.enqueue("Jackie")
    normal_queue.enqueue("Oda")
    normal_queue.enqueue("Sabra")
    normal_queue.preview()
    print('')
    print('Priority Queue')
    print('-------------')
    prio_queue = PriorityQueue()
    prio_queue.enqueue("Jay", 3)
    prio_queue.enqueue("Abbey")
    prio_queue.enqueue("Kevin", 3)
    prio_queue.enqueue("Ben", 1)
    prio_queue.enqueue("Sam", 4)
    prio_queue.enqueue("Hai", 3)
    prio_queue.enqueue("Ken", 2)
    prio_queue.preview()
    print('')
    print('Hot Potato')
    print('-------------')
    hot_potato(['Jay', 'Abbey', 'Kevin', 'Ben', 'Sam', 'Hai', 'Ken'], 7)
