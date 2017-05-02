class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, data):
        temp = Node(data)
        if self.size == 0:
            self.head = temp
            self.size += 1
        else:
            temp.next = self.head
            self.head = temp
            self.size += 1

    def pop(self):
        if self.size > 0:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data
        else:
            raise IndexError("Stack is empty")

    def __len__(self):
        return self.size

    def __repr__(self):
        a = 'Empty'
        if self.size == 1:
            return 'Top'+'('+str(self.head.data) + ')'
        elif self.size == 0:
            return a
        else:
            current = self.head
            c = 0
            while current:
                if c == 0:
                    a = 'Top' + '(' + str(current.data) + ')'
                    c += 1
                    current = current.next
                else:
                    a += '-' + str(current.data)
                    current = current.next
            return a

    def __contains__(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
        raise StopIteration

    def extend(self, data):
        for i in data:
            self.push(i)

    def index(self, data):
        current = self.head
        i = self.size - 1
        while current:
            if current.data == data:
                return i
            else:
                current = current.next
                i -= 1
        return False
