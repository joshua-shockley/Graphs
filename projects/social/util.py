
# Note: This Queue class is sub-optimal. Why?


class Queue():
    def __init__(self):
        self.queue = []

    def __str__(self):
        output = ''
        for i in self.queue:
            output += f" {i}, "
        return output

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)
