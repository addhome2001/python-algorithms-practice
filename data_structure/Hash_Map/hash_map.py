# -*- coding: utf-8 -*-
"""湊雜表"""

HASH_RANGE = 200

class HashMap(object):
    """
    湊雜表類別
    """
    def __init__(self):
        self.map = [None for _ in range(HASH_RANGE)]

    def set(self, key, value):
        """
        新增資料
        以key的hash值作為表的index
        """
        self.map[djb2_hash(key)] = value

    def remove(self, key):
        """
        刪除資料
        以key的hash值作為表的index
        並將之設置為None
        """
        self.map[djb2_hash(key)] = None

    def get(self, key):
        """
        獲取資料
        """
        return self.map[djb2_hash(key)]

def djb2_hash(chars):
    """djb2 hash"""
    hash_key = 5381
    for char in chars:
        result = hash_key * 37 + ord(char)
    return result % 198

if __name__ == '__main__':
    hash_map = HashMap()
    hash_map.set('Ben', 'ben@example.com')
    hash_map.set('Jay', 'jay@example.com')
    print(hash_map.get('Ben'))
    print(hash_map.get('Jay'))
    hash_map.remove('Ben')
    print(hash_map.get('Ben'))
    print(hash_map.get('Jay'))
