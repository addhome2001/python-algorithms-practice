hash_len = 20

class HashMap:
    def __init__(self):
        self.map = [None for _ in xrange(hash_len)]

    def set(self, key, value):
        self.map[loselose(key)] = value

    def remove(self, key):
        self.map[loselose(key)] = None

    def get(self, key):
        return self.map[loselose(key)]

def loselose(chars):
    result = 0
    for char in chars:
        result += ord(char)
    return result % hash_len

hash_map = HashMap()
hash_map.set('name', 'Ben')
hash_map.set('age', 20)
print(hash_map.get('name'))
print(hash_map.get('age'))
hash_map.remove('name')
print(hash_map.get('name'))
print(hash_map.get('age'))
