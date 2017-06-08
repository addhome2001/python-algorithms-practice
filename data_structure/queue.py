class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return False

    def front(self):
        if self.isEmpty():
            return self.items[0]
        return False

    def clear(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() <= 0

    def preview(self):
        for item in self.items:
            print(item)

# practice
class PriorityItem:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def get_item(self):
        return self.item

    def get_priority(self):
        return self.priority

class PriorityQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def enqueue(self, item, priority=0):
        if self.isEmpty():
            return self.items.append(PriorityItem(item, priority))

        for i in range(0, self.size()):
            if (priority > self.items[i].get_priority()):
                self.items[i:i] = [PriorityItem(item, priority)]
                break
        else:
            self.items.append(PriorityItem(item, priority))

    def preview(self):
        for item in self.items:
            print('Item: {}, Priority: {}'.format(
                item.get_item(), item.get_priority()
            ))

def hotPotato(members, number):
    queue = Queue()

    for member in members:
        queue.enqueue(member)

    while (queue.size() is not 1):
        counter = number
        while (counter > 0):
            counter -= 1
            queue.enqueue(queue.dequeue())

        print("{} get out.".format(queue.dequeue()))

    print("{} is winner!".format(queue.dequeue()))

print('Normal Queue')
print('-------------')
normal_queue = Queue()
normal_queue.enqueue("Han")
normal_queue.enqueue("Jackie")
normal_queue.enqueue("Oda")
normal_queue.enqueue("Sabra")
normal_queue.preview()
print('')
print('Priority Queue')
print('-------------')
prio_queue = PriorityQueue()
prio_queue.enqueue("Jay", 3)
prio_queue.enqueue("Abbey")
prio_queue.enqueue("Kevin", 3)
prio_queue.enqueue("Ben", 1)
prio_queue.enqueue("Sam", 4)
prio_queue.enqueue("Hai", 3)
prio_queue.enqueue("Ken", 2)
prio_queue.preview()
print('')
print('Hot Potato')
print('-------------')
members = ['Jay', 'Abbey' ,'Kevin' ,'Ben' ,'Sam', "Hai", "Ken"]
hotPotato(members, 7)
