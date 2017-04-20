class Node():
    def __init__(self, element):
        self.element = element
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def append(self, element):
        node = Node(element)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            current = self.head
            while (current.next):
                current = current.next

            node.prev = current
            current.next = node
            self.tail = node

        self.length += 1

    def insert(self, element, position):
        if type(position) == int and position < self.length:
            node = Node(element)
            current = self.head
            index = 0

            if position == 0:
                if current is None:
                    self.head = node
                    self.tail = node
                else:
                    node.next = current
                    self.head = node

            else:
                while (index < position):
                    prev = current
                    current = current.next
                    index += 1

                prev.next = node
                current.prev = node
                node.prev = prev
                node.next = current

            self.length += 1
            return True
        else:
            return False

    def getHead(self):
        return self.head.element

    def getTail(self):
        return self.tail.element

    def remove(self, element):
        index = self.indexOf(element)
        return self.removeAt(index)

    def indexOf(self, element):
        current = self.head
        index = -1

        while (current):
            index += 1
            if current.element == element:
                return index
            current = current.next

        return -1

    def removeAt(self, position):
        if self.length > 0 and position >= 0 and position <= self.length:
            current = self.head
            index = 0

            if position == 0:
                self.head = current.next

                if self.length == 1:
                    self.tail = None
                else:
                    self.head.prev = None

            elif position == self.length - 1:
                current = self.tail
                current.prev.next = current.next
                self.tail = current.prev

            else:
                while (index < position):
                    prev = current
                    current = current.next
                    index += 1
                prev.next = current.next
                current.next.prev = prev

            self.length -= 1
            return current.element
        else:
            return None

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def size(self):
        return self.length

    def toString(self):
        current = self.head
        string = ''
        while (current):
            string += '{} '.format(current.element)
            current = current.next
        return string

linked_list = DoubleLinkedList()
linked_list.removeAt(3)
linked_list.append('Ben')
linked_list.append('Jam')
linked_list.remove('Hai')
linked_list.insert('Juice', 1)
linked_list.insert('Acid', 0)
linked_list.insert('Abbey', 2)
linked_list.removeAt(1)
print('Index of Abbey: {}'.format(linked_list.indexOf('Abbey')))
print('Index of Eva: {}'.format(linked_list.indexOf('Eva')))
print('Size: {}'.format(linked_list.size()))
print('Head: {}'.format(linked_list.getHead()))
print('Tail: {}'.format(linked_list.getTail()))
print('Mebmers: {}'.format(linked_list.toString()))
