class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
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
        for x in self.items:
            print(x)

# practice
def priorityItem(item, priority):
    return {
        "item": item,
        "priority": priority
    }

class PriorityQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def enqueue(self, item, priority=0):
        if self.isEmpty():
           return self.items.append(priorityItem(item, priority))

        for i in range(0, self.size()):
            if (priority > self.items[i].get('priority')):
                self.items[i:i] = [priorityItem(item, priority)]
                break
        else:
            self.items.append(priorityItem(item, priority))


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
