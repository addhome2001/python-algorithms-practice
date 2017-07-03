# -*- coding: utf-8 -*-
"""字典"""

class Dictionary(object):
    """
    字典類別
    以鍵值對的方式存放資料
    """
    def __init__(self):
        self.items = {}

    def set(self, key, value):
        """
        設置資料
        以key作為儲存位置
        """
        self.items[key] = value

    def remove(self, key):
        """
        移除資料
        以key移除該儲存位置之資料
        """
        if self.has(key):
            del self.items[key]
            return True
        return False

    def has(self, key):
        """
        判斷資料是否存在
        """
        return key in self.items

    def get(self, key):
        """
        獲取資料
        先判斷該筆資料是否存在
        """
        if self.has(key):
            return self.items[key]
        return None

    def clear(self):
        """
        清空字典
        """
        self.items = {}

    def size(self):
        """
        返回該字典大小
        """
        return len(self.items)

    def keys(self):
        """
        返回該字典的所有keys
        """
        return list(self.items)

    def values(self):
        """
        返回該字典的所有values
        """
        return [self.items.get(key) for key in self.keys()]

    def get_items(self):
        """
        返回該字典所有資料
        """
        return self.items

if __name__ == '__main__':
    dic = Dictionary()
    dic.set('name', 'Ben')
    dic.clear()
    dic.set('age', '20')
    dic.set('phone', '1234567')
    dic.set('phones', '2aaa')
    # print(dic.size())
    # print(dic.keys())
    dic.remove('age')
    print(dic.values())
    # print(dic.get_items())
    # print(dic.size())
