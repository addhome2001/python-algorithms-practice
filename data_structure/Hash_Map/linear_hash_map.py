hash_len = 100

class HashMap:
    def __init__(self):
        self.map = {}

    def set(self, key, value):
        hash_key = djb2Hash(key)

        while (hash_key in self.map):
            if self.map[hash_key].key == key:
                break
            hash_key += 1

        self.map[hash_key] = ValuePair(key, value)

    def get(self, key):
        hash_key = djb2Hash(key)

        while (hash_key in self.map):
            if self.map[hash_key].key == key:
                return self.map[hash_key].value
            hash_key += 1

        return None

    def remove(self, key):
        hash_key = djb2Hash(key)

        while (hash_key in self.map):
            if self.map[hash_key].key == key:
                del self.map[hash_key]
                return True
            hash_key += 1

        return False

class ValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "key: {}, value: {}".format(self.key, self.value)

def djb2Hash(chars):
    hash_key = 5381
    for char in chars:
        result = hash_key * 37 + ord(char)
    return result % 98

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
