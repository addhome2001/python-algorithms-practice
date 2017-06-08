hash_len = 200

class HashMap:
    def __init__(self):
        self.map = [None for _ in range(hash_len)]

    def set(self, key, value):
        self.map[djb2Hash(key)] = value

    def remove(self, key):
        self.map[djb2Hash(key)] = None

    def get(self, key):
        return self.map[djb2Hash(key)]

def djb2Hash(chars):
    hash_key = 5381
    for char in chars:
        result = hash_key * 37 + ord(char)
    return result % 198

hash_map = HashMap()
hash_map.set('Ben', 'ben@example.com')
hash_map.set('Jay', 'jay@example.com')
print(hash_map.get('Ben'))
print(hash_map.get('Jay'))
hash_map.remove('Ben')
print(hash_map.get('Ben'))
print(hash_map.get('Jay'))
