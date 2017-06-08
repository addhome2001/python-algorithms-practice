class Set():
    def __init__(self):
        self.items = {}

    def add(self, value):
        if not self.has(value):
            self.items[value] = value
            return True

        return False

    def remove(self, value):
        if value in self.items:
            del self.items[value]
            return True

        return False

    def has(self, value):
        return value in self.items

    def clear(self):
        self.items = {}

    def size(self):
        return len(self.items)

    def values(self):
        result = ()
        for value in self.items:
            result += (value,)

        return result

new_set = Set()
print(new_set.size())
new_set.add("Ben")
new_set.add("Ken")
new_set.add("Sam")
new_set.add("Hai")
print(new_set.size())
print(new_set.values())
new_set.remove("Ben")
print(new_set.values())
