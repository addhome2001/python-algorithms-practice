from linkedList import LinkedList

hash_len = 20

class HashMap:
    def __init__(self):
        self.map = [None for _ in xrange(hash_len)]

    def set(self, key, value):
        hash_key = loselose(key)

        # remove the exist key
        self.remove(key)

        if self.map[hash_key] is None:
            self.map[hash_key] = LinkedList()

        self.map[hash_key].append(ValuePair(key, value))

    def remove(self, key):
        hash_key = loselose(key)
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
        hash_key = loselose(key)
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

def loselose(chars):
    result = 0
    for char in chars:
        result += ord(char)
    return result % hash_len

print('')
print('Separate Chaining Hash Map')
print('-------------')
hash_map = HashMap()
print('Set name: Ben')
hash_map.set('name', 'Ben')
print('Set name: Ray')
hash_map.set('name', 'Ray')
print('Set z: valueZ')
hash_map.set('z', 'valueZ')
print('Set 1I: value1I')
hash_map.set('1I', 'value1I')
print('Get z: {}'.format(hash_map.get('z')))
print('Get 1I: {}'.format(hash_map.get('1I')))
print('Get name: {}'.format(hash_map.get('name')))
print('Remove name')
hash_map.remove('name')
print('Get name: {}'.format(hash_map.get('name')))
