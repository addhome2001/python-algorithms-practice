# -*- coding: utf-8 -*-
"""集合"""

class Set(object):
    """
    集合類別
    為一組不同物件之集合
    """
    def __init__(self):
        self.items = {}

    def add(self, value):
        """
        新增資料
        存在則返回False
        不存在則新增
        """
        if not self.has(value):
            self.items[value] = value
            return True

        return False

    def remove(self, value):
        """
        移除資料
        不存在則返回False
        存在則移除該筆資料
        """
        if value in self.items:
            del self.items[value]
            return True

        return False

    def has(self, value):
        """
        判斷是否存在該筆資料
        """
        return value in self.items

    def clear(self):
        """
        清除該集合
        """
        self.items = {}

    def size(self):
        """
        返回集合的長度
        """
        return len(self.items)

    def values(self):
        """
        將集合的值存放至Tuple
        並返回
        """
        result = ()
        for value in self.items:
            result += (value,)

        return result

if __name__ == '__main__':
    new_set = Set()
    print(new_set.size())
    new_set.add("Ben")
    new_set.add("Ken")
    new_set.add("Sam")
    new_set.add("Hai")
    print(new_set.size())
    print(new_set.values())
    new_set.remove("Ben")
    print(new_set.values())
