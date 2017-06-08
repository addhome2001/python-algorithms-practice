class Dictionary:
    def __init__(self):
        self.items = {}

    def set(self, key, value):
        self.items[key] = value

    def remove(self, key):
        if self.has(key):
            del self.items[key]
            return True
        return False

    def has(self, key):
        return key in self.items

    def get(self, key):
        if self.has(key):
            return self.items[key]
        return None

    def clear(self):
        self.items = {}

    def size(self):
        return len(self.items)

    def keys(self):
        return list(self.items)

    def values(self):
        return map(lambda key: self.get(key), self.keys())

    def getItems(self):
        return self.items

dic = Dictionary()
dic.set('name', 'Ben')
dic.clear()
dic.set('age', '20')
dic.set('phone', '1234567')
print(dic.size())
print(dic.keys())
dic.remove('age')
print(dic.values())
print(dic.getItems())
print(dic.size())
