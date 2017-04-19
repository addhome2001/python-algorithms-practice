class Node():
    def __init__(self, element):
        self.element = element
        self.next = None

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def append(self, element):
        node = Node(element)

        if self.head == None:
            self.head = node
        else:
            current = self.head
            while (current.next):
                current = current.next

            current.next = node
        self.length += 1

    def insert(self, element, position):
        if type(position) == int and position <= self.length:
            node = Node(element)
            current = self.head
            index = 0

            if position == 0:
                self.head = node
                node.next = current
            else:
                while (index < position):
                    prev = current
                    current = current.next
                    index += 1

                prev.next = node
                node.next = current
            self.length += 1
            return True
        else:
            return False

    def getHead(self):
        return self.head

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
            else:
                while (index < position):
                    prev = current
                    current = current.next
                    index += 1
                prev.next = current.next
                return current
        else:
            return None

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def size(self):
        return self.length

    # string
    def toString(self):
        current = self.head
        string = ''
        while (current):
            string += '{} '.format(current.element)
            current = current.next
        return string

linked_list = LinkedList()
linked_list.removeAt(0)
linked_list.append('Ben')
linked_list.append('Jam')
linked_list.remove('Hai')
linked_list.insert('Juice', 2)
linked_list.insert('Abbey', 3)
linked_list.removeAt(2)
print('Index of Abbey: {}'.format(linked_list.indexOf('Abbey')))
print('Index of Eva: {}'.format(linked_list.indexOf('Eva')))
print(linked_list.toString())
