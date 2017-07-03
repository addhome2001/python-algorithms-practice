# -*- coding: utf-8 -*-
"""分離鏈結"""

if __name__ == '__main__':
    import os
    import sys
    DIR_PATH = os.path.dirname(os.path.join(os.getcwd(), __file__))
    sys.path.append(os.path.normpath(os.path.join(DIR_PATH, '..')))
    from Linked_List.linked_list import LinkedList
else:
    from ..Linked_List.linked_list import LinkedList

HASH_RANGE = 100

class ValuePair(object):
    """
    鍵值對類別
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        """複寫print方法"""
        return "key: {}, value: {}".format(self.key, self.value)

def djb2_hash(chars):
    """djb2 hash"""
    hash_key = 5381
    for char in chars:
        result = hash_key * 37 + ord(char)
    return result % (HASH_RANGE - 3)

class HashMap(object):
    """
    分離鏈結Hash表類別
    利用LinkedList存取相同Hash的資料
    """
    def __init__(self):
        """
        初始化表陣列
        可依資料量定義最大範圍量
        """
        self.map = [None for _ in range(HASH_RANGE)]

    def set(self, key, value):
        """
        新增資料
        新增資料前，先以key進行清除以免寫入重複資料
        以key的hash值作為表的index
        不存在該hash表的LinkedList則創建
        """
        hash_key = djb2_hash(key)

        self.remove(key)

        if self.map[hash_key] is None:
            self.map[hash_key] = LinkedList()

        self.map[hash_key].append(ValuePair(key, value))

    def remove(self, key):
        """
        刪除資料
        刪除資料前，先判斷該hash值是否存在
        如不存在該hash值，並返回False
        存在則操作該index中的LinkedList，並返回True
        並在刪除完畢後檢查該LinkedList是否為空
        """
        hash_key = djb2_hash(key)
        map_pos = self.map[hash_key]

        if map_pos is not None:
            current = map_pos.getHead()

            while current.next:
                if current.element.key == key:
                    map_pos.remove(current.element)
                current = current.next

            if current.element.key == key:
                map_pos.remove(current.element)

            if map_pos.isEmpty():
                self.map[hash_key] = None

            return True

        return False

    def get(self, key):
        """
        獲取資料
        獲取資料前，先判斷該hash值是否存在
        如不存在該hash值，返回None
        存在則操作該index中的LinkedList
        並返回該key對應的值
        """
        hash_key = djb2_hash(key)
        map_pos = self.map[hash_key]

        if map_pos is not None:
            current = map_pos.getHead()

            while current.next:
                if current.element.key == key:
                    return current.element.value
                current = current.next

            if current.element.key == key:
                return current.element.value

        return map_pos

if __name__ == '__main__':
    print('')
    print('Separate Chaining Hash Map')
    print('-------------')
    hash_map = HashMap()
    print('Set Ben')
    hash_map.set('Ben', 'Ben@example.com')
    print('Set Ray')
    hash_map.set('Ray', 'Ray@example.com')
    print('Set z: valueZ')
    hash_map.set('z', 'valueZ')
    print('Set 1I: value1I')
    hash_map.set('1I', 'value1I')
    print('Get z: {}'.format(hash_map.get('z')))
    print('Get 1I: {}'.format(hash_map.get('1I')))
    print('Get Ben: {}'.format(hash_map.get('Ben')))
    print('Change Ben\'s email')
    hash_map.set('Ben', 'Ben@example2.com')
    print('Remove Ray')
    hash_map.remove('Ray')
    print('Get Ray: {}'.format(hash_map.get('Ray')))
    print('Get Ben: {}'.format(hash_map.get('Ben')))
