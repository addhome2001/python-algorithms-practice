# -*- coding: utf-8 -*-
"""線性查找"""

HASH_LEN = 100

class HashMap(object):
    """
    線性查找Hash表類別
    利用Hash值進行儲存，如該Hash值已存在其他資料
    則將該Hash值加一，直到該值的儲存位置為空
    """
    def __init__(self):
        self.map = {}

    def set(self, key, value):
        """
        新增資料
        以key的hash值作為表的index
        如該Hash已存在，但不同於插入的key
        則將該Hash值加一，並持續尋找
        如該key已存在，則進行覆蓋
        """
        hash_key = djb2_hash(key)

        while hash_key in self.map:
            if self.map[hash_key].key == key:
                break
            hash_key += 1

        self.map[hash_key] = ValuePair(key, value)

    def get(self, key):
        """
        獲取資料
        以key的hash值作為表的index
        如果欲尋找的Hash值的位置的key相同則返回
        不相同則將該Hash值加一，並繼續尋找
        """
        hash_key = djb2_hash(key)

        while hash_key in self.map:
            if self.map[hash_key].key == key:
                return self.map[hash_key].value
            hash_key += 1

        return None

    def remove(self, key):
        """
        移除資料
        以key的hash值作為表的index
        如果欲尋找的Hash值的位置的key相同則設為None，並返回True
        不相同則將該Hash值加一，並繼續尋找
        """
        hash_key = djb2_hash(key)

        while hash_key in self.map:
            if self.map[hash_key].key == key:
                del self.map[hash_key]
                return True
            hash_key += 1

        return False

class ValuePair(object):
    """
    鍵值對類別
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "key: {}, value: {}".format(self.key, self.value)

def djb2_hash(chars):
    """djb2 hash"""
    hash_key = 5381
    for char in chars:
        result = hash_key * 37 + ord(char)
    return result % 98

if __name__ == '__main__':
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
