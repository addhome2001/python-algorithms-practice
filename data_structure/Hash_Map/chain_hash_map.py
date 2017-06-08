import sys, os
sys.path.insert(0, os.path.abspath('..'))
from Linked_List.linked_list import LinkedList

hash_len = 100

class HashMap(object):
    def __init__(self):
        self.map = [None for _ in range(hash_len)]

    def set(self, key, value):
        hash_key = djb2Hash(key)

        # remove the exist key
        self.remove(key)

        if self.map[hash_key] is None:
            self.map[hash_key] = LinkedList()

        self.map[hash_key].append(ValuePair(key, value))

    def remove(self, key):
        hash_key = djb2Hash(key)
        map_pos = self.map[hash_key]

        if map_pos is not None:
            current = map_pos.getHead()

            while (current.next):
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
        hash_key = djb2Hash(key)
        map_pos = self.map[hash_key]

        if map_pos is not None:
            current = map_pos.getHead()

            while (current.next):
                if current.element.key == key:
                    return current.element.value
                current = current.next

            if current.element.key == key:
                return current.element.value

        return map_pos

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
